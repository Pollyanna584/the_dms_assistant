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

def generate_general_store(df_summons_pets, df_magical, df_consumables, pet_percentage_range, magic_percent_range, consumable_percentage_range, price_adjustment_range, num_items_in_shop_low_percent, num_items_in_shop_high_percent):
    total_items = len(df_summons_pets) + len(df_magical) + len(df_consumables)

    # Calculate the number of items for each category based on percentage ranges
    pet_percent = random.randint(*pet_percentage_range)
    magic_percent = random.randint(*magic_item_percentage_range)
    consumable_percent = random.randint(*consumable_percentage_range)

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
    all_items = pd.concat([df_pet_consumables, df_magical]).dropna(subset=['Name'])

    # Generate the store inventory with random price adjustments
    num_items_in_shop = round(random.uniform(num_items_in_shop_low_percent, num_items_in_shop_high_percent) / 100 * total_items)
    store_inventory = random.sample(list(all_items[['Name', 'Adjusted Price']].itertuples(index=False, name=None)), num_items_in_shop)

    for idx, item in enumerate(store_inventory, 1):
        name, price = item
        formatted_price = format_price(price)
        store_inventory[idx - 1] = (name, formatted_price)

    return store_inventory

#### Name Generator functions

def choose_adj():
    all_adj = [item for sublist in adjectives for item in sublist]
    adj = random.choice(all_adj)
    return adj

def needs_plural(adj):
    return adj in adjectives[-1]

def pluralize(noun):
    irr_sg = ["Ox", "Mouse", "Goose", "Man", "Child", "Foot", "Tooth" ]
    irr_pl = ["Oxen", "Mice", "Geese", "Men", "Children", "Feet", "Teeth"]
    same_pl =["Deer", "Elk", "Moose", "Sheep", "Fish"]

    if noun in same_pl:
        return noun
    elif noun in irr_sg:
        return irr_pl[irr_sg.index(noun)]
    else:
        return noun + "s"

def generate_random_name():
    adj = choose_adj()
    all_nouns = [item for sublist in nouns for item in sublist]
    noun = random.choice(all_nouns)

    if needs_plural(adj):
        noun = pluralize(noun)

    return adj + " " + noun

####### get the names:
adjectives = [
	["Laughing", "Leering", "Sneering", "Smiling"], 
	["Frowning", "Glaring", "Crying", "Happy", "Frightened", "Running"], 
	["Prancing", "Dancing", "Leaping", "Wandering", "Barking", "Drunken"], 
	["Slaughtered", "Roaring", "Howling", "Rearing", "Sleeping", "Hanging"], 
	["Flying", "Galloping", "Hunted", "Drowned", "Fighting", "Swollen"], 
	["Racing", "Limping", "Growling", "Yowling", "Prowling", "Horned"], 
	["Fanged", "Silent", "Blinded", "Naked", "Fettered"], 
	# 1 racist colors
	["Red", "Yellow", "White", "Black", "Brown", "Pale", "Dark"],
	# 2 neutral descriptors
	["Orange", "Green", "Blue", "Purple", "Pink", "Golden", "Silver"], 
	["Striped", "Spotted", "Ashen", "Grey", "Dirty", "Tarnished", "Rusty", "Russet"], 
	["Gilded", "Iron", "Tin", "Bronze", "Platinum", "Ochre", "Violet"], 
	["Gray", "Crimson", "Indigo", "Rosy", "Umber", "Brass", "Copper"], 
	["Lavender", "Stone", "Oaken", "Leaden", "Steel", "Saffron"], 
	["Verdant", "Bronzed", "Electrum", "Cerulean", "Maroon", "Glass"], 
	["Glazed", "Brazen", "Sanguine", "New", "Old", "Broken", "Great"], 
	["High", "Upset", "Overturned", "Rotten", "Burned", "Enchanted"], 
	["Shady", "Forsaken", "Ruined", "Near", "Far", "Hidden", "Sunlit"], 
	["Single", "Lone", "Lonely", "Double", "Triple", "Rising", "Fallen"], 
	["Crowned", "Royal", "Lucky", "Unlucky", "Cursed", "Blessed"], 
	["Battered", "Smooth", "Bald", "Icy"], 
	# 3 needs plural
	["Two", "Twin", "Three", "Four"]
]

nouns = [
	["Rose", "Daisy", "Lily", "Violet", "Carnation", "Bluebell"], 
	["Blossom", "Crocus", "Snowdrop", "Primrose", "Jonquil", "Honeysuckle"], 
	["Poppy", "Pansy", "Ambrosia", "Nightshade", "Camellia", "Jasmine"], 
	["Cereus", "Dahlia", "Geranium", "Gillyflower", "Hemlock", "Hibiscus"], 
	["Hyacinth", "Iris", "Lavender", "Lilac", "Lotus", "Mandrake"], 
	["Marigold", "Saffron", "Pennyroyal", "Peony", "Pimpernel", "Clover"], 
	["Thistle", "Tulip", "Oleander", "Orchid", "Cherry", "Apple"], 
	["Plum", "Pear", "Peach", "Fig", "Chestnut", "Almond", "Olive"], 
	["Filbert", "Lemon", "Lime", "Mulberry", "Persimmon", "Quince"], 
	["Walnut", "Pomegranate", "Coconut", "Oak", "Elm", "Maple", "Pine", "Fir"], 
	["Rowan", "Beech", "Cedar", "Willow", "Holly", "Laurel", "Linden"], 
	["Aspen", "Birch", "Ebony", "Hazel", "Larch", "Cypress", "Magnolia"], 
	["Palm", "Sycamore", "Yew", "Alder", "Juniper", "Aubergine", "Grape"], 
	["Gooseberry", "Mushroom", "Pineapple", "Truffle", "Strawberry"], 
	["Acorn", "Wheat", "Rye", "Potato", "Barley", "Corn", "Wormwood"], 
	["Parsley", "Leaf", "Ivy", "Bush", "Log", "Branch", "Hedge", "Tree"], 
	["Thorn", "Fern", "Vine", "Bud"], 
	# 1 inanimates
	["Barrel", "Hammer", "Stein", "Tankard", "Ball", "Chain", "Lamp"], 
	["Shoe", "Egg", "Nut", "Goblet", "Stool", "Chair", "Table", "Bridle"], 
	["Saddle", "Spindle", "Sword", "Spear", "Shield", "Bolt", "Nest"], 
	["Dam", "Wall", "Gate", "Door", "Jack", "Spade", "Anchor", "Sun"], 
	["Moon", "Star", "Coin", "Cup", "Rod", "Fork", "Spoon", "Knife"], 
	["Heart", "Sheaf", "Cross", "Crescent", "Spur", "Cloud", "Globe"], 
	["Crown", "Helm", "Hat", "Harp", "Pipe", "Drum", "Bugle", "Flute"], 
	["Clarion", "Trumpet", "Axe", "Lance", "Banner", "Sickle", "Key"], 
	["Anvil", "Nail", "Wheel", "Well", "Drop", "River", "Pearl", "Bucket"], 
	["Plough", "Carbuncle", "Lock", "Arrow", "Bow", "Staff", "Wand"], 
	["Orb", "Whip", "Pot", "Cane", "Collar", "Knot", "Mug", "Lantern"], 
	["Cart", "Yoke", "Tub", "Tun", "Block", "Tackle", "Bone", "Comb"], 
	["Rock", "Scale", "Pin", "Lute", "Fiddle", "Distaff", "Tap"], 
	["Cork", "Cap", "Fetter", "Gallows", "Post", "Stirrup", "Ring"],
	# 2 animal parts
	["Tooth", "Skull", "Tail", "Claw", "Horn", "Hoof", "Wing", "Feather"], 
	["Antler", "Tusk", "Beak", "Fang", "Sting", "Beard"], 
	# 3 animals
	["Bull", "Pony", "Stag", "Hart", "Deer", "Hind", "Wolf", "Lamb"], 
	["Goat", "Dog", "Hound", "Hare", "Coney", "Rabbit", "Hog", "Pig"], 
	["Sow", "Cow", "Steer", "Fox", "Cat", "Lion", "Tiger", "Bear"], 
	["Rat", "Giraffe", "Hippo", "Antelope", "Rhino", "Hyena", "Jackal"], 
	["Camel", "Mule", "Horse", "Donkey", "Steed", "Badger"], 
	["Hedgehog", "Weasel", "Mink", "Beaver", "Cub", "Boar", "Bat"], 
	["Panther", "Elk", "Moose", "Leopard", "Pard", "Elephant", "Vixen"],
	["Cougar", "Puma", "Pup", "Mastiff", "Calf", "Colt", "Foal", "Filly"], 
	["Ox", "Yak", "Buck", "Doe", "Fawn", "Roe", "Kit", "Stallion", "Mare"], 
	["Stoat", "Greyhound", "Ibex", "Ram", "Sheep", "Wombat", "Possum"], 
	["Raccoon", "Porcupine", "Squirrel", "Mole", "Capybara", "Camelopard"], 
	["Mouse", "Otter", "Eel", "Dolphin", "Fish", "Shark", "Crab"], 
	["Octopus", "Seahorse", "Whale", "Perch", "Trout", "Mackerel"], 
	["Herring", "Seal", "Walrus", "Carp", "Turtle", "Toad", "Frog"], 
	["Salamander", "Tortoise", "Lizard", "Snake", "Serpent", "Crocodile"], 
	["Alligator", "Viper", "Adder", "Eagle", "Cock", "Hen", "Owl", "Swallow"],
	["Hawk", "Tern", "Gull", "Albatross", "Songbird", "Goose", "Swan"], 
	["Vulture", "Raven", "Crow", "Jay", "Cockerel", "Rooster", "Gander"], 
	["Duck", "Duckling", "Dove", "Robin", "Bluebird", "Finch", "Sparrow"], 
	["Bird", "Stork", "Crane", "Heron", "Loon", "Buzzard", "Turkey"], 
	["Lark", "Pheasant", "Martlet", "Emu", "Magpie", "Osprey", "Ostrich"], 
	["Parrot", "Pelican", "Quail", "Spider", "Bee", "Wasp", "Locust"], 
	["Grasshopper", "Ant", "Scorpion", "Beetle", "Flea", "Dragonfly"], 
	["Butterfly", "Pegasus", "Dragon", "Roc", "Griffin", "Manticore"], 
	["Yeti", "Gorgon", "Owlbear", "Hippogriff", "Chimera", "Ettin"], 
	["Flumph", "Gargoyle", "Basilisk", "Unicorn", "Drider", "Wyvern"], 
	["Hippocampus", "Phoenix"], 
	# 4 humanoids 
	["Dwarf", "Elf", "Orc", "Demon", "Devil", "Banshee", "Fairy", "Monkey"], 
	["Mermaid", "Giant", "Kobold", "Ogre", "Troll", "Harpy", "Cyclops"], 
	["Gnoll", "Hobgoblin", "Dryad", "Undine", "Nymph", "Centaur", "Hag"], 
	["Imp", "Drow", "Goblin", "Pixie", "Bugbear", "Minotaur", "Angel"], 
	["Ape", "Baboon","Satyr", "Sphinx", "Knight", "Jester", "Man"], 
	["Bandit", "Gladiator", "Maid", "Maiden", "Sailor", "Soldier"], 
	["Rider", "Child", "Queen", "King", "Thief", "Smith", "Priest"], 
	["Wizard", "Witch", "Mage", "Sage", "Scholar", "Knave", "Seamstress"], 
	["Laundress"],
	# 5 people parts
	["Arm", "Leg", "Head", "Hand", "Foot", "Tongue", "Mouth", "Thumb", "Toe"]
]

# Load the CSV data into DataFrames (replace filenames accordingly)
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

# Generate and print the store inventory
store_inventory = generate_general_store(df_summons_pets, df_magical, df_consumables, pet_percentage_range, magic_item_percentage_range, consumable_percentage_range, price_adjustment_range, num_items_in_shop_low_percent, num_items_in_shop_high_percent)

print(generate_random_name()+" Inventory:")
for idx, item in enumerate(store_inventory, 1):
    name, price = item
    print(f"{idx}. {name} - Price: {price}")