from selenium import webdriver

# Ouvrir le site web de Google dans un navigateur
driver = webdriver.Firefox()
driver.get("https://www.google.com")

# Fermer le navigateur
driver.quit()
