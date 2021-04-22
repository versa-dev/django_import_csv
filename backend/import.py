#!/usr/bin/env python

"""
    Script to import data from .csv file to Model Database DJango
    To execute this script run: 
                                1) manage.py shell
                                2) exec(open('file_name.py').read())
"""

import csv, uuid
from myapp.models import Pokemon 

CSV_PATH = '../Pokemon.csv'      # Csv file path  


with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar=';')
    for index, row in enumerate(spamreader, start=1):
        
        temp = list(row[0].split(","))
        if index != 1:
            Pokemon.objects.create(
                name=temp[1],
                type_1=temp[2],
                type_2=temp[3],
                total=temp[4],
                hp=temp[5],
                attack=temp[6],
                defense=temp[7],
                sp_atk=temp[8],
                sp_def=temp[9],
                speed=temp[10],
                generation=temp[11],
                legendary=temp[12]
            )