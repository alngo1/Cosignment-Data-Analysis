# This python file takes exports from Ricochet's Expanded Sales
# Detail Report, cleans the data, adds vendor by id, sorts by
# vendors, and outputs into "cleaned.csv".

import csv
import getCosignerNumbers

#Class to organize data into Sale Item Objects
class SaleItem:
    # string, string, float, float
    def __init__(self, SKU, product, price, QTY, cosigner):
        self.SKU = SKU
        self.product = product
        self.price = price
        self.QTY = QTY
        self.date = ""
        self.cosigner = cosigner

    def __str__(self):
        return f"{self.SKU},{self.product},{self.price},{self.QTY}"
    
    def setDate(self, date):
        self.date = date

# Function that lwk does too much
def createCleanedCSV():
    # create a dictionary to store SaleItem objects {productName: SaleItem}
    saleItems = {}
    # get the list of cosigner names
    cosigners = getCosignerNumbers.getCosignerNumbers()
    # read from csv file to add to dictionary
    with open("Sales Report 09_26_2025 (expanded).csv", 'r', newline='', errors="ignore") as csvfile:
        reader = csv.reader(csvfile)

        currentDate = ""
        # loop through each row in csv
        for row in reader:
            # in the data, every row's first member, row[0], 
            # is different. if its the sale number (i.e. 19200) 
            # it can be turned into a number. here we do try 
            # that to differentiate it from the strings
            try:
                saleNumber = int(row[0])
            except:
                saleNumber = ""
                pass

            # if first member is a number this row also has
            # the date in row[1] so store it.
            if(type(saleNumber) is int):
                currentDate = row[1]
            # else if first member is a string, not empty, and
            # first character in string is an apostrophe it matches
            # the SKU# (i.e. '000001), so we can use this row to
            # make SaleItems
            elif(type(row[0]) is str and len(row[0]) > 1 and row[0][0] == "'"):
                # if this item is in our dictionary just add
                # it's QTY
                if(row[1] in saleItems):
                    saleItems[row[1]].QTY += int(float(row[4]))
                # else create a new SaleItem,
                # set its date and add it to our dictionary.
                else:
                    newItem = SaleItem(row[0][1:], row[1], float(row[2]), int(float(row[4])), cosigners[row[0][1:4]])
                    newItem.date = currentDate
                    saleItems[row[1]] = newItem
    

    #write saleItems to new csv file
    with open("cleaned.csv", "w", newline='') as csvfile:
        
        writer = csv.writer(csvfile)
        # Write a row for just the column labels
        writer.writerow(["SKU", "Item Name", "Date", "QTY Sold", "Price"])
        # Sort the writing of rows by vendors
        for id, vendor in cosigners.items():
            for key, value in saleItems.items():
                if(value.cosigner == vendor):
                    writer.writerow([value.SKU, value.product, value.date, value.QTY, value.price, value.cosigner])