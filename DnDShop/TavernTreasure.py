import pandas as pd
import random
import os

####### Adjust these variables for testing and customization
pet_percentage_range = (1, 5)
magic_item_percentage_range = (10, 20)
consumable_percentage_range = (40, 50)
price_adjustment_range = (-10, -5)  # Price adjustment in percentage
num_items_in_shop_low_percent = 3  # Lowest percentage for number of random items in the shop
num_items_in_shop_high_percent = 3  # Highest percentage for number of random items in the shop

####### Item Generator functions

def format_price(price):
    if pd.notna(price):
        price_in_copper = price
        if price_in_copper is not None:
            platinum = int(price_in_copper // 1000)
            gold = int((price_in_copper % 1000) // 100)
            silver = int((price_in_copper % 100) // 10)
            copper = int(round(price_in_copper % 10))  # Round to nearest digit before converting to integer

            # Add non-zero currency amounts to the list
            price_list = []
            if platinum != 0:
                price_list.append(f"{platinum} platinum")
            if gold != 0:
                price_list.append(f"{gold} gold")
            if silver != 0:
                price_list.append(f"{silver} silver")
            if copper != 0:
                price_list.append(f"{copper} copper")

            # Join the list elements with commas
            formatted_price = ', '.join(price_list)

            return formatted_price

    return "Price not available"

def adjust_prices(df_items, price_adjustment_range):
    df_items['Adjusted Price'] = df_items.loc[df_items['Price'].notna(), 'Price'].apply(lambda price: apply_adjustment(price, price_adjustment_range))
    return df_items

def apply_adjustment(price, price_adjustment_range):
    if price is None:
        return None
    price_adjustment = random.uniform(*price_adjustment_range)
    adjusted_price = price * (1 + price_adjustment / 100)
    return adjusted_price

def generate_general_store(df_magical, df_consumables, magic_item_percentage_range, consumable_percentage_range, price_adjustment_range, num_items_in_shop_low_percent, num_items_in_shop_high_percent):
    total_items = len(df_magical) + len(df_consumables)

    # Calculate the number of items for each category based on percentage ranges
    magic_percent = random.randint(*magic_item_percentage_range)
    consumable_percent = random.randint(*consumable_percentage_range)

    if magic_percent == 0:
        num_magic_items = 0
    else:
        num_magic_items = round((magic_percent / 100) * total_items)

    if consumable_percent == 0:
        num_consumables = 0
    else:
        num_consumables = round((consumable_percent / 100) * total_items)

    # Check if there are any consumable items to add
    all_items = df_consumables if num_consumables > 0 else pd.DataFrame()
    if magic_percent > 0:  # Only include magical items if magic_percent > 0
        all_items = pd.concat([all_items, df_magical]).dropna(subset=['Name'])

    # Generate the store inventory with random price adjustments
    num_items_in_shop = round(random.uniform(num_items_in_shop_low_percent, num_items_in_shop_high_percent) / 100 * total_items)
    store_inventory = random.sample(list(all_items[['Name', 'Adjusted Price']].itertuples(index=False, name=None)), min(len(all_items), num_items_in_shop))

    for idx, item in enumerate(store_inventory, 1):
        name, price = item
        formatted_price = format_price(price)
        store_inventory[idx - 1] = (name, formatted_price)

    return store_inventory

def generate_creature_stables(df_summons_pets, price_adjustment_range, num_items_in_stables):
    df_summons_pets = adjust_prices(df_summons_pets, price_adjustment_range)

    stable_inventory = random.sample(list(df_summons_pets[['Name', 'Adjusted Price']].itertuples(index=False, name=None)), min(len(df_summons_pets), num_items_in_stables))

    for idx, item in enumerate(stable_inventory, 1):
        name, price = item
        formatted_price = format_price(price)
        stable_inventory[idx - 1] = (name, formatted_price)

    return stable_inventory

data_dir = os.path.dirname(os.path.realpath(__file__))
df_magical = pd.read_csv(f'{data_dir}/Items/magic_items.csv').dropna(subset=['Name'])
df_summons_pets = pd.read_csv(f'{data_dir}/Items/summons_pets.csv').dropna(subset=['Name'])
df_consumables = pd.read_csv(f'{data_dir}/Items/consumable_items.csv').dropna(subset=['Name'])

# Convert 'Price' column to numeric, coerce errors to convert non-numeric values to NaN
df_magical['Price'] = pd.to_numeric(df_magical['Price'], errors='coerce')
df_summons_pets['Price'] = pd.to_numeric(df_summons_pets['Price'], errors='coerce')
df_consumables['Price'] = pd.to_numeric(df_consumables['Price'], errors='coerce')

# Adjust the prices of each DataFrame
df_magical = adjust_prices(df_magical, price_adjustment_range)
df_summons_pets = adjust_prices(df_summons_pets, price_adjustment_range)
df_consumables = adjust_prices(df_consumables, price_adjustment_range)