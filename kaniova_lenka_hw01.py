import json

with open('alice.txt', encoding='utf-8') as file:
    text = file.read()
    
text_without_spaces = text.replace(' ', '')
text_without_enters = text_without_spaces.replace('\n', '')

dictionary = {}
for character in text_without_enters.lower():
    if character in dictionary:
        dictionary[character] += 1
    else:
        dictionary[character] = 1

with open('hw01_output.json', "w", encoding='utf-8') as file:
        json.dump(dictionary, file, indent=4, sort_keys=True,
                  ensure_ascii=False)    