## Install Pandas ('pip install pandas')

## Libraries
import pandas as pd
import random as rd
import os

## Pandas options
pd.options.display.max_rows = 9999 #Max rows shown
dir = os.path.dirname(os.path.abspath(__file__))

## Import CSVs
m_combat = pd.read_csv(f'{dir}/Items/MagicItems/combatitems.csv')
m_noncombat = pd.read_csv(f'{dir}/Items/MagicItems/noncombatitems.csv')
m_consume = pd.read_csv(f'{dir}/Items/MagicItems/consumables.csv')
n_gear = pd.read_csv(f'{dir}/Items/NormalItems/adventuregear.csv') 
n_armor = pd.read_csv(f'{dir}/Items/NormalItems/armor.csv')
n_weapon = pd.read_csv(f'{dir}/Items/NormalItems/weapons.csv')
n_tools = pd.read_csv(f'{dir}/Items/NormalItems/tools.csv')

## Item Randomizer
def rollItems(item_count, shop_count, row):
    global shop_inventory
    shop_array=range(0,item_count)
    shop_inventory=rd.sample(shop_array,shop_count)

magic_choice = input("Choose an option:\n1 - lots of items\n2 - normal amount\n3 - few items\n") 

## Combat Items
m_combat_count = len(m_combat)
m_combat_shop_count = round(m_combat_count*combat_percent)
newrow=0
rollItems(m_combat_count, m_combat_shop_count, newrow)
m_combat_inventory = shop_inventory
m_combat_shop = m_combat.loc[m_combat_inventory, ["Name", "Price"]]
print(m_combat_shop)