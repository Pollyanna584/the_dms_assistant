## Install Pandas ('pip install pandas')

## Libraries
import pandas as pd
import random as rd

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

## Item Randomizer
def rollItems(item_count, shop_count, row):
    global shop_inventory
    shop_array=range(0,item_count)
    shop_inventory=rd.sample(shop_array,shop_count)
    
## Combat Items
m_combat_count = len(m_combat)
m_combat_shop_count = round(m_combat_count*.2)
newrow=0
rollItems(m_combat_count, m_combat_shop_count, newrow)
m_combat_inventory = shop_inventory
m_combat_shop = m_combat.loc[[m_combat_inventory], ["Name", "Price"]]
print(m_combat_shop)

##tests
# m_combat_shop = m_combat.loc[[list(m_combat_inventory)], ["Name", "Price"]]
# print(m_combat_shop)

# m_combat_list=list(m_combat_inventory)
# m_combat_shop = m_combat.loc[[m_combat_list], ["Name", "Price"]]
# print(m_combat_shop)

print(m_combat_inventory)