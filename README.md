# The DM's Assistant:
### A 5e DungeonMaster tool I am developing for myself
  
![GitHub Repo stars](https://img.shields.io/github/stars/Pollyanna584/DnD?style=social)
[![Docker Pulls](https://img.shields.io/docker/pulls/pollyanna584/the_dms_assistant.svg)](https://hub.docker.com/r/pollyanna584/the_dms_assistant)
[![Docker Version](https://img.shields.io/docker/v/pollyanna584/the_dms_assistant?sort=semver)](https://hub.docker.com/r/pollyanna584/the_dms_assistant))

# About :
- The DM's Assitant is a tool to assist Dungeon Masters playing Dungeons and Dragons 5e
- The magic items in the shop can be found in the [DnDShop/Items](https://github.com/Pollyanna584/DnD/tree/main/DnDShop/Items) folder.  It is a list of magic items from the 5e source books but can be edited to be used for any TTRPG
- Requirements can be found in [requirements.txt](https://github.com/Pollyanna584/DnD/blob/main/requirements.txt)
- This can be pulled an ran locally at localhost:1738
- You can also pull the docker image at [pollyanna584/the_dms_assistant:latest](https://hub.docker.com/r/pollyanna584/the_dms_assistant)


## Features
- Will generate a random shop name with a random amount of items based on the parameters given on the first page
- You can export this as a CSV which is required if you would like to save the shop.  Shops will not be saved after you leave the page unless you download the csv

## Bugs
- If you change the values where the high is a lower number than the low the page will break and you'll have to reload
- If any of the 3 values (Pets, Magic Items, and Consumables) do not return an item then nothing will display