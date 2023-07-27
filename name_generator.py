import random

#### Name Generator functions

class NameGenerator:
	def __init__(self):
		self.adjectives = [
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

		self.nouns = [
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

	def choose_adj(self):
		all_adj = [item for sublist in self.adjectives for item in sublist]
		adj = random.choice(all_adj)
		return adj

	def needs_plural(self, adj):
		return adj in self.adjectives[-1]
	
	def pluralize(self, noun):
		irr_sg = ["Ox", "Mouse", "Goose", "Man", "Child", "Foot", "Tooth" ]
		irr_pl = ["Oxen", "Mice", "Geese", "Men", "Children", "Feet", "Teeth"]
		same_pl =["Deer", "Elk", "Moose", "Sheep", "Fish"]

		if noun in same_pl:
			return noun
		elif noun in irr_sg:
			return irr_pl[irr_sg.index(noun)]
		else:
			return noun + "s"

	def generate_random_name(self):
		adj = self.choose_adj()
		all_nouns = [item for sublist in self.nouns for item in sublist]
		noun = random.choice(all_nouns)
		if self.needs_plural(adj):
			noun = self.pluralize(noun)
		return adj + " " + noun

# Create an instance
name_gen = NameGenerator()

# Call methods
chosen_adj = name_gen.choose_adj()
needs_plural = name_gen.needs_plural(chosen_adj)

generator = NameGenerator()
print(generator.generate_random_name())