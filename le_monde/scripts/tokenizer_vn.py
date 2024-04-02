from pyvi import ViTokenizer

def tokenize_vn(text):
    try:
        # Tokenize the input text
        result = ViTokenizer.tokenize(text).split()
        return result

    except Exception as e:
        print(f"An error occurred during tokenization: {e}")
        return None
