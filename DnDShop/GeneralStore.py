## Install Pandas ('pip install pandas')

## Libraries
import pandas as pd

## Pandas options
pd.options.display.max_rows = 9999 #Max rows shown

## Import CSVs
m_combat = pd.read_csv(r'/Users/pmonk/GitHub/PersonalRepo/Python/DnDShop/Items/MagicItems/combatitems.csv')
m_noncombat = pd.read_csv(r'/Users/pmonk/GitHub/PersonalRepo/Python/DnDShop/Items/MagicItems/noncombatitems.csv')
m_consume = pd.read_csv(r'/Users/pmonk/GitHub/PersonalRepo/Python/DnDShop/Items/MagicItems/consumables.csv')
n_gear = pd.read_csv(r'/Users/pmonk/GitHub/PersonalRepo/Python/DnDShop/Items/NormalItems/adventuregear.csv')
n_armor = pd.read_csv(r'/Users/pmonk/GitHub/PersonalRepo/Python/DnDShop/Items/NormalItems/armor.csv')
n_weapon = pd.read_csv(r'/Users/pmonk/GitHub/PersonalRepo/Python/DnDShop/Items/NormalItems/weapons.csv')
n_tools = pd.read_csv(r'/Users/pmonk/GitHub/PersonalRepo/Python/DnDShop/Items/NormalItems/tools.csv')

volume_choice = input("Choose an option:\n1 - lots of items\n2 - normal amount\n3 - few items\n")

global item_volume
if volume_choice=="1":
    print(m_combat.sample(frac=.06))
elif volume_choice=="2":
    print(m_combat.sample(frac=.03))
elif volume_choice=="3":
    print(m_combat.sample(frac=.015))
else:
    print("nope")
    exit