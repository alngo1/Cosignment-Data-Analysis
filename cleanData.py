import csv
import sortVendors

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
    
    def getQTY(self):
        return self.QTY
    
    def setDate(self, date):
        self.date = date

def createCleanedCSV():
    #create a dictionary to store SaleItem objects {productName: SaleItem}
    saleItems = {}
    #get the list of cosigner names
    cosigners = sortVendors.getCosignerNumbers()
    #read from csv file to add to dictionary
    with open("Sales Report 09_26_2025 (expanded).csv", 'r', newline='', errors="ignore") as csvfile:
        reader = csv.reader(csvfile)

        currentDate = ""
        #loop through each row in csv
        for row in reader:
            try:
                saleNumber = int(row[0])
            except:
                saleNumber = ""
                pass

            if(type(saleNumber) is int):
                currentDate = row[1]
            elif(type(row[0]) is str and len(row[0]) > 1 and row[0][0] == "'"):
                newItem = SaleItem(row[0][1:], row[1], float(row[2]), int(float(row[4])), cosigners[row[0][1:4]])
                if(row[1] in saleItems):
                    saleItems[row[1]].QTY += newItem.QTY
                else:
                    newItem.date = currentDate
                    saleItems[row[1]] = newItem
    

    #write saleItems to new csv file
    with open("cleaned.csv", "w", newline='') as csvfile:
        
        writer = csv.writer(csvfile)
        writer.writerow(["SKU", "Item Name", "Date", "QTY Sold", "Price"])
        for id, vendor in cosigners.items():
            for key, value in saleItems.items():
                if(value.cosigner == vendor):
                    writer.writerow([value.SKU, value.product, value.date, value.QTY, value.price, value.cosigner])