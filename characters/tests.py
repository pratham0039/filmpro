from django.test import TestCase

import fitz  # PyMuPDF
import re
import pandas as pd

def remove_common_keys(dict1, dict2):
    for key in list(dict2.keys()):
        if key in dict1:
            del dict2[key]

def has_lowercase_word(line):
    words = line.split()  # Split the line into words
    for word in words:
        if any(char.islower() for char in word):
            return True
        if word=='-':
            return True
    return False
def extract_scenes_from_text(text):
    # Define the regular expression pattern to match scene headings
    scene_pattern = r'(?:EXT\.|INT\.|I/E\.|TRANSITION\:|\\CUT TO\\:|INT/EXT\.)\s*.*?(?=EXT\.|INT\.|I/E\.|TRANSITION\:|\\CUT TO\\:|INT/EXT\.|$)'
    # Use regex to find all scenes based on the pattern
    scenes = re.findall(scene_pattern, text, re.DOTALL | re.IGNORECASE)

    return scenes

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text("text")
    doc.close()
    return text

def find_words_with_all_caps_and_no_symbols(line):
    words = line.split()
    capital_words = []

    for word in words:
        # Use a regular expression to check if the word consists of capital letters only and has no symbols
        if re.match(r'^[A-Z]*$', word) and not re.search(r'[!@#$%^&*(),.?":{}|<>]', word):
            capital_words.append(word)

    return capital_words
      
   
def process_pdf(pdf_path):
    df = pd.read_csv("final_film (1).csv")
    df.drop(df.index, inplace=True)

    print(df.head())
    
    word_freq2 = {}
    pdf_path = pdf_path  # Replace with the actual path to your PDF file
    extracted_text = extract_text_from_pdf(pdf_path)

    lines = extracted_text.split('\n')
    word_freq = {}
    scenes = extract_scenes_from_text(extracted_text)
    for line in lines:
        if has_lowercase_word(line):
            continue
        else:
            capital = find_words_with_all_caps_and_no_symbols(line)
            character = ""
            for c in capital:
              character = character + c

              if character != " " or character != "":
                if character in word_freq:
                  word_freq[character] += 1
                else:
                  word_freq[character] = 1
    
    for idx, scene in enumerate(scenes, start=1):
        # Extract the description part of the scene

        scene_without_spaces = "".join(scene.split())

        # Search for character names in the scene description


        scene_description = scene.split("\n")[0]
        scene_script = None
        try:
          sceneno = scene.split("\n")[1]

        except:
          continue
        lines = scene_description.split('\n')
        for line in lines:
            if has_lowercase_word(line):
              continue
            else:
              capital = find_words_with_all_caps_and_no_symbols(line)
              character = ""
              for c in capital:
                character = character + c

            if character != " " or character != "":
              if character in word_freq2:
                word_freq2[character] += 1
              else:
                word_freq2[character] = 1
    remove_common_keys(word_freq2, word_freq)
    print(word_freq2)

    excluded_words = ['PLAY', 'CUT', 'FORADTEAM', 'FOR','FORAD']
    filtered_word_counts = {word: count for word, count in word_freq.items() if count >= 8 and word not in excluded_words}
    
    keys_to_remove = []
    for key2 in filtered_word_counts.keys():
        for key1 in word_freq2.keys():
            if key2 in key1:
                keys_to_remove.append(key2)
    print(keys_to_remove)
    for key in set(keys_to_remove):
        filtered_word_counts.pop(key)
    print(filtered_word_counts)



    for idx, scene in enumerate(scenes, start=1):
    # Extract the description part of the scene
        
        scene_without_spaces = "".join(scene.split())
        charactersss = []

        for word, frequency in filtered_word_counts.items():
        # Convert both the word and paragraph to lowercase for a case-insensitive search
            word = word.lower()
            scene_without_spaces_lower = scene_without_spaces.lower()


        # Count the occurrences of the word


            if word in scene_without_spaces_lower:
              charactersss.append(word)
        # Search for character names in the scene description







        # Extract time of day, location, and place from the summary
        time_of_day_list = []
        location_list = []
        place_list = []
        pattern = r"(EXT|INT|I/E|INT/EXT)\s*\.\s*(.*?)\s*-\s*(\w+(?:\s+\w+)*)"
        match = re.match(pattern, scene_description)
        if match:
            location = match.group(1)
            place = match.group(2)
            time_of_day = match.group(3)
            time_of_day_list.append(time_of_day)
            location_list.append(location)
            place_list.append(place)
        for time_of_day, location, place in zip(time_of_day_list, location_list, place_list):
            new_row = {'SC': sceneno, 'INT/EXT': location, 'DAY/NIGHT': time_of_day, 'LOCATION':place, 'DESCRIPTION': scene, 'CAST ID' : charactersss}
            df = df._append(new_row, ignore_index=True)
            #print(f"Scene {sceneno}:\nTime of Day: {time_of_day}\nLocation: {location}\nPlace: {place}\n {scene_script}\n character = {charactersss}")


    #for word, frequency in word_freq2.items():
       #print(f"{word}: {frequency}")

    print(df)
    df.to_csv('film2.csv', index=False)




process_pdf('Jersey Script (1).pdf')

