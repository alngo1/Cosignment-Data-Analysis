import cleanData
import pandas as pd

# Define simple categorization rules based on keywords
def categorize_item(name: str) -> str:
    name = name.lower()
    if any(word in name for word in ["tee", "t-shirt", "shirt", "top"]):
        return "Tees/Tops"
    elif any(word in name for word in ["hoodie", "sweatshirt", "pullover"]):
        return "Hoodies/Sweatshirts"
    elif any(word in name for word in ["jacket", "coat", "parka", "windbreaker"]):
        return "Jackets/Outerwear"
    elif any(word in name for word in ["jeans", "denim"]):
        return "Jeans"
    elif any(word in name for word in ["pants", "trousers", "slacks"]):
        return "Pants"
    elif "shorts" in name:
        return "Shorts"
    elif any(word in name for word in ["skirt", "dress"]):
        return "Skirts/Dresses"
    elif any(word in name for word in ["hat", "cap", "beanie"]):
        return "Hats/Accessories"
    elif any(word in name for word in ["bag", "backpack", "tote"]):
        return "Bags"
    elif any(word in name for word in ["shoes", "sneakers", "boots", "sandals"]):
        return "Footwear"
    else:
        return "Other"

if __name__ == "__main__":
    cleanData.createCleanedCSV()

    df = pd.read_csv("cleaned.csv")
    # Apply categorization
    df["Category"] = df["Item Name"].apply(categorize_item)
    
    df.to_csv("categorized.csv", index=False)