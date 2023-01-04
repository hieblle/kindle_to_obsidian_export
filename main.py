import os
import numpy as np
import re

def read_config_file(configpath):

    with open('kindle8.txt', 'r', encoding='utf-8') as f:
        file_content = f.read().split('\n')

    title_list = []


    for count, i in enumerate(file_content):
        if re.match('==========', i) and count <= 100:
            # found new marking
            # 1. check if new book, else add note to existing file
            # 2. if new one: create new file
            # 3. extract metadata and text

            title = file_content[count+1][:20] + ".txt"
            metadata = file_content[count+2]
            
            # extract text for insert_content function
            for j in range(count+1, len(file_content)):
                if re.match('==========', file_content[j]):
                    break
            text = file_content[count+4 : j]
     
    

            # check for existence of book file, else: create new one
            if len(title_list) != 0 and file_content[count+1] == title_list[len(title_list) - 1]:
                # same title as before, add to existing file
                # don't create, just write ('a' for writing, append to the end of the file)
                insert_content(title, 'a', metadata, text)
            else:
                # new book. create new file, then add note
                title_list.append(file_content[count+1])
                # create and write ('x' for exclusive creation, failing if file exists already)
                    # extract metadata first (title, author)
                    # check if title is a valid filename
                insert_content(title, 'x', metadata, text)


                    
        
        else:
            continue



    return ('Import successful')


def insert_content(title, indicator, metadata, text):

    marking = ""
    for line in text:
        marking += line

    with open(title, indicator) as current_book:
        current_book.write(marking + '\n' + metadata + '\n\n') 




#txt nicht nach \n splitten, sondern nach = Folge, als jedes Element ist ein Zitat
#dann Titel (Anfang bis "-"), Seite (nach "Position") und Zitat ('"' bis '"') extr.



# to-do:
# extract title and author, metadata 
# change slicing to correct title 
# extremfälle vorbeugen: anfang und ende





if __name__ == "__main__":

    configpath = os.path.join('kindle.txt')
    print(read_config_file(configpath))



# 2022 Update:
# loop over each line, create new txt file for a book, then add all following markings and notes
# repeat over all books (1 file per book)

# Variablen festlegen (autor, titel etc) -> alles aus Metadaten für späteres Template