# This python file takes an exported Ricochet Cosigners Tab and
# returns a dictionary for each cosigner with name and ID.
# In this case the file we read from is called "cosigners.csv"
import csv

def getCosignerNumbers():
    cosigners = {"000": "Store Inventory"}
    #read from csv file to add to dictionary
    with open("cosigners.csv", 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if(i == 0):
                continue
            cosigners[row[0]] = row[1] + " " + row[2]
    return cosigners