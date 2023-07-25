import pandas as pd
import random
import re
import os

# Adjust these variables for testing and customization
pet_percentage = 5
magic_item_percentage = 20
consumable_percentage = 40
price_adjustment_percent = -10  # Change this percentage to adjust the prices of all items
num_items_in_shop_low_percent = 5  # Lowest percentage for number of random items in the shop
num_items_in_shop_high_percent = 15  # Highest percentage for number of random items in the shop

def extract_numeric_price(price):
    # Convert to string and remove non-numeric characters from the price string
    price_str = str(price)
    numeric_price = re.sub(r'[^\d.]', '', price_str)
    try:
        return float(numeric_price)
    except ValueError:
        return 0

def adjust_prices(df_items, percent):
    df_items['Price'] = df_items['Price'].apply(extract_numeric_price)
    df_items['Price'] = df_items['Price'] * (1 + percent / 100)
    return df_items

def generate_general_store(df_summons_pets, df_magical, df_consumables, pet_percent, magic_percent, consumable_percent, price_percent, num_items_in_shop_low_percent, num_items_in_shop_high_percent):
    total_items = len(df_summons_pets) + len(df_magical) + len(df_consumables)

    # Calculate the number of items for each category based on percentages
    num_pet_items = round((pet_percent / 100) * total_items)
    num_magic_items = round((magic_percent / 100) * total_items)
    num_consumables = round((consumable_percent / 100) * total_items)

    # Filter pets by rarity and calculated percentage
    rarity_distribution = [num_pet_items // 5] * 5
    remainder = num_pet_items % 5
    for i in range(remainder):
        rarity_distribution[i] += 1

    pet_items = []
    for rarity, count in zip(['Common', 'Uncommon', 'Rare', 'Very Rare', 'Legendary'], rarity_distribution):
        items_of_rarity = df_summons_pets[df_summons_pets['Rarity'] == rarity]
        if not items_of_rarity.empty:
            sampled_items = items_of_rarity.sample(count, replace=True)
            pet_items.extend(sampled_items)

    # Concatenate pets and consumable items into one DataFrame
    df_pet_consumables = pd.concat([pd.DataFrame(pet_items), df_consumables])

    # Combine pets, magical, and consumable items into one DataFrame
    all_items = pd.concat([df_pet_consumables, df_magical])

    # Adjust prices based on the provided percentage
    all_items = adjust_prices(all_items, price_percent)

    # Calculate the number of items in the shop within the specified range
    num_items_in_shop = round(random.uniform(num_items_in_shop_low_percent, num_items_in_shop_high_percent) / 100 * total_items)

    store_inventory = random.sample(list(all_items[['Name', 'Price']].itertuples(index=False, name=None)), num_items_in_shop)

    return store_inventory

# Load the CSV data into DataFrames (replace filenames accordingly)
dir = os.path.dirname(os.path.abspath(__file__))
df_magical = pd.read_csv(f'{dir}/Items/magic_items.csv')
df_summons_pets = pd.read_csv(f'{dir}/Items/summons_pets.csv') 
df_consumables = pd.read_csv(f'{dir}/Items/consumable_items.csv')  # Assuming you have a CSV for consumable items

# Generate and print the store inventory
store_inventory = generate_general_store(df_summons_pets, df_magical, df_consumables, pet_percentage, magic_item_percentage, consumable_percentage, price_adjustment_percent, num_items_in_shop_low_percent, num_items_in_shop_high_percent)

print("Generated Store Inventory:")
for idx, item in enumerate(store_inventory, 1):
    name, price = item
    print(f"{idx}. {name} - Price: {price:.2f} gold")
