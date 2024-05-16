# QuickTranslate (C) github.com/jordanisadev

# Importing necessary libraries
from googletrans import Translator
import os

# Defining banner variables
banner = r'''
   ____        _      _ _______                  _       _       
  / __ \      (_)    | |__   __|                | |     | |      
 | |  | |_   _ _  ___| | _| |_ __ __ _ _ __  ___| | __ _| |_ ___ 
 | |  | | | | | |/ __| |/ / | '__/ _` | '_ \/ __| |/ _` | __/ _ \
 | |__| | |_| | | (__|   <| | | | (_| | | | \__ \ | (_| | ||  __/
  \___\_\\__,_|_|\___|_|\_\_|_|  \__,_|_| |_|___/_|\__,_|\__\___|
                                                                 
 - QuickTranslate (C) Artemis 2024 | Github: jordanisadev
'''

# Creating functions to translate and handle
def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    os.system('cls')
    print(banner)
    while True:
        print("\nEnter the text you want to translate")
        text = input('>> ')
        print("\nSelect the language ('en' for English, 'id' for Indonesia)")
        target_language = input()
        translated_text = translate_text(text, target_language)
        print(f"\nTranslated text => {translated_text}")

# Run all the functions defined
if __name__ == "__main__":
    main()
