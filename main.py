from random import *
import os
import csv

sample_csv = "Prenoms.csv"

# nb = int(input("Combien de comptes ? "))
# os.remove("account.txt")
# file = open("account.txt", "a+")
# file.close

with open(sample_csv, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line)