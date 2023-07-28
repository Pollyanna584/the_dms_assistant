# The DM's Assistant:
### A 5e DungeonMaster tool I am developing for myself
#
### https://dmassist.monkcloud.win/
#

![GitHub Repo stars](https://img.shields.io/github/stars/Pollyanna584/DnD?style=social)
[![Docker Pulls](https://img.shields.io/docker/pulls/pollyanna584/the_dms_assistant.svg)](https://hub.docker.com/r/pollyanna584/the_dms_assistant)
[![Docker Version](https://img.shields.io/docker/v/pollyanna584/the_dms_assistant?sort=semver)](https://hub.docker.com/r/pollyanna584/the_dms_assistant)

# About :
- The DM's Assitant is a tool to assist Dungeon Masters playing Dungeons and Dragons 5e
- As of now, the only feature in production is a randomized shop generator

## Getting The DM's Assistant

The DM's Assistant is a relatively small Docker container (122 MB compressed). Pull the latest release from the index, and make sure I didn't forget to update the version number here by checking the version badge above:

    $ docker pull pollyanna584/the_dms_assistant:v1.0.2

## Using The DM's Assistant

The simplest way to use The DM's Assistant is to run the docker container:

    $ docker run --name the_dms_assitant -d -p 1738:1738 pollyanna584/the_dms_assistant:v1.0.2

The DM's Assitant will be available at [http://localhost:1738/](http://localhost:1738/). You can change `-p 1738:1738` to any port. For example, if you want to view The DM's Assistant over port 8371 then you would do `-p 8371:1738`.

## Connecting with Docker compose

    version: "3.9"
    services:
      the_dms_assistant:
        container_name: the_dms_assistant
        image: pollyanna584/the_dms_assistant:v1.0.2
        restart: unless-stopped
        ports:
          - 1738:1738

# D&D Shop Creator!
## About:
- The magic items in the shop can be found in the [DnDShop/Items](https://github.com/Pollyanna584/DnD/tree/main/DnDShop/Items) folder.  It is a list of magic items from the 5e source books but can be edited to be used for any TTRPG
- If you'd like to run it locally, the Python version in the docker container is 3.9 because of numpy issues but I wrote it on 3.10.6 and it works fine when not compiling it to a docker container. 
- Other requirements can be found in [requirements.txt](https://github.com/Pollyanna584/DnD/blob/main/requirements.txt)
- Running it locally will allow you to change the CSV files for other TTRPGs
- If ran locally, you can access it at [localhost:1738](localhost:1738)
- Code found here can include other features and bug fixes that haven't been uploaded to docker yet

## Features:
- Will generate a random shop name with a random amount of items based on the parameters given on the first page
- Will also generate a random name, 
- You can export this as a CSV which is required if you would like to save the shop.  Shops will not be saved after you leave the page unless you download the csv

## Bugs:
- If you change the values where the high is a lower number than the low the page will break and you'll have to reload
- If any of the 3 values (Pets, Magic Items, and Consumables) do not return an item then nothing will display

## Credits:
- Shout out to [honeybeehailey](https://www.twitch.tv/honeybeehailey) for the shopkeeper idea!
- Shout out to [r/D100](https://www.reddit.com/r/d100/) and [u/rusty8684](https://www.reddit.com/user/rusty8684) for the voice prompts!

## Looking For:
- Fantasy names that can be used as either last names or first names.  Mine are all human for now
- Ideas for new features