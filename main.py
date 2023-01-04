import os
import numpy as np
import re

def read_config_file(configpath):

    with open('kindle8.txt', 'r', encoding='utf-8') as f:
        file_content = f.read().split('\n')

    title_list = []


    for count, i in enumerate(file_content):
        if re.match('==========', i):
            title_list.append(i[count+1])

        if re.match('-', i.strip()):
            # Seite rausziehen

# wäre es nicht besser re.match('===') nach Zeile suchen zu Lassen
# die ein neues Zitat darstellt, und dann in eine Schleife zu gehen um
# wirklich nur dieses Zitat mit Infos rauszuziehen und es nicht zu vermischen
# wie wärs mit einem dictionary?

#txt nicht nach \n splitten, sondern nach = Folge, als jedes Element ist ein Zitat
#dann Titel (Anfang bis "-"), Seite (nach "Position") und Zitat ('"' bis '"') extr.


    return






if __name__ == "__main__":

    configpath = os.path.join('kindle.txt')
    read_config_file(configpath)
