#!/bin/python3

import csv
import pandas as pd
import subprocess

import sys


df = pd.read_csv("dataset2.tsv", delimiter='\t')
print(df.TEXT)


NE = ["ne", "n'"]
NEGATION = ['pas', 'rien', 'jamais', 'point', 'guère', 'plus', 'ni', 'nul', 'aucun', 'personne', 'que', 'nulle', 'aucunement', 'nullement'] #'sans': négation incomplète

# Temps des verbes dans tree tagger
TEMPS = []

def tree_tag():
	stop = 0
	FIN = 1000
	for prof_insee, (niv_etudes, text) in zip(df.PROF_INSEE, zip(df.NIV_ETUDES, df.TEXT)):
		#print("text=", text)
		#print("niv_etudes=", niv_etudes)
		#print("prof_insee=", prof_insee)
		process_echo = subprocess.Popen(["echo", text], stdout=subprocess.PIPE)
		process_tree_tagger = subprocess.Popen("./cmd/tree-tagger-french", stdin=process_echo.stdout, stdout=subprocess.PIPE)
		output, _ = process_tree_tagger.communicate()

		yield output.decode('utf-8')
		stop += 1
		if stop == FIN:
			break


def extract_verb_pos(tokens):
    for tok_n, tok in enumerate(tokens):
        form = tok[0]
        POS = tok[1].split(':')[0]
        if POS == 'VER':
            verb = form
            tense = tok[1].split(':')[1]  # Extract tense from POS tag
            print("VERBE:", verb, "TEMPS:", tense)

def process_sentence(phrase):
	# negation
	print(phrase)
	tokens = phrase.split('\n')
	tokens = [t.split('\t') for t in tokens if len(t) > 0] # découpage des lignes de la sortie tree tagger
	
	#prev_negation = 0 # négation précédente pour ne pas aller chercher des 'ne' trop loin si il y a deux négations dans une phrase
	
	for tok_n, tok in enumerate(tokens):
		print("tok = ", tok)
		form = tok[0]
		POS = tok[1].split(':')[0]
		if POS == 'VER':
			TEMPS = tok[1].split(':')[1]
			print("verbe:", tok, "temps:", TEMPS)
		if POS == 'ADV':
			if form in NEGATION:
				print("adverbe:", tok, phrase)
				# Récupérer le ne. Si il y a un ne, vérifier ce qu'il y a entre les deux.
				# Ce qu'il peut y avoir entre les deux:
				# le (montée du clitique) (le, la: je ne la mange pas)
				# un verbe
				# un adverbe : j'aime vraiment pas
				ne = False
				print(tokens[0:tok_n])
				print("###### TOK_n = ", tok_n)
				sub_tokens = tokens[0:tok_n]
				print("sub tokens:", sub_tokens)
				between = []
				tok_ne, tok_ne_n = None, None
				for tok2_n, tok2 in enumerate(sub_tokens[::-1]): # part de l'adverbe et remonte (ordre inversé)
					print("boucle interne:", tok2_n, tok2)
					if tok2[0] in NE:
						print("NE trouvé", tok2[0])
						tok_ne, tok_ne_n = tok2, tok2_n
						break
						# ce qu'il y a entre les deux:
					else:
						between.append(tok2)
				print("between:", between)
				# Vérifier qu'il n'y a pas autre chose que des VER, ADV, et PRO:PER (clitique)
				for tok2 in between:
					print(tok2)
					POS = tok2[1]
					ne_relie = True
					if POS[0:3] not in ['ADV', 'VER']:
						if POS != 'PRO:PER':
							#ce 'ne' n'est pas relié à la négation
							ne_relie = False
				if ne_relie:
					print("Le ne est bien relié.")

				
				

def main():
	for phrase in tree_tag():
		tokens = phrase.split('\n')
		tokens = [t.split('\t') for t in tokens if len(t) > 0]
		extract_verb_pos(tokens)  # Appel de la fonction pour extraire les POS des verbes
		process_sentence(phrase)
if __name__ == "__main__":
	main()

# Si le mot est dans la liste NEGATION et qu'il a pour POS == ADV, alors c'est un marqueur de négation

