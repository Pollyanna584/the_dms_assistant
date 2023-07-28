import pandas as pd
import random

class ShopkeeperGenerator:

    def __init__(self):
        self.data_dir = './Shopkeeper'
        self.names = pd.read_csv(f'{self.data_dir}/shopkeeper_names.csv')
        self.races = pd.read_csv(f'{self.data_dir}/races.csv')
        self.voices = pd.read_csv(f'{self.data_dir}/voices.csv')

    def generate_name(self):
        # Choose 2 or 3 names, with a 5% chance of choosing 3 names
        name_count = 3 if random.random() < 0.05 else 2
        chosen_names = random.choices(self.names.values.flatten(), k=name_count)
        return ' '.join(chosen_names)

    def generate_race(self):
        return random.choice(self.races.values.flatten())

    def generate_voice(self):
        return random.choice(self.voices.values.flatten())

    def generate_shopkeeper(self):
        name = self.generate_name()
        race = self.generate_race()
        voice = self.generate_voice()
        return {
            "Name": name,
            "Race": race,
            "Voice": voice
        }

# Test the ShopkeeperGenerator class
# generator = ShopkeeperGenerator()
# print(generator.generate_shopkeeper())
