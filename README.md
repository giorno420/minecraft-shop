# Flask-Minecraft Server shop
[![Discord](https://img.shields.io/discord/794061682279317554)](https://discord.giornosmp.com)
![PyPI - License](https://img.shields.io/pypi/l/mi)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/0-percent-optimized.svg)](https://forthebadge.com)

A web server for a simple Minecraft server shop!

You need <a href="https://www.spigotmc.org/resources/authmereloaded.6269">AuthMe Reloaded</a> to use password verification.
This project uses:
 - SFTP to get the passwords database
 - A custom plugin for running commands
 - Python, Java and JavaScript :D

## Setting up
This requires you to have basic knowledge of Python, the command line and Java. If stuff breaks, it is NOT my problem

### Prerequisites
Setting this up will need the following stuff downloaded. Also note that this can only be ran in a UNIX based system. Windows will break it.
 - <a href="https://python.org/downloads">Python 3</a>
 - <a href="https://java.com/en/download/">Java 11</a>
 - <a href="https://git-scm.com">Git</a>

### Getting the source
Clone this repository

```sh
git clone https://github.com/giorno420/minecraft-shop.git
```

### Config
I'm using a `settings.json` file for configuration, and a `settings.json.example` file which shows how your config file should look like. Delete the `settings.json.example` file in the production environment. All the information and details are in the example file.

### Requirements
This project uses modules (duh). Installing them all is fairly easy. Open this project's directory, and run: 
```sh
pip3 install -r requirements.txt
```

### Adding the plugin
Download the plugin and follow the detailed instructions <a href="https://github.com/giorno420/minecraft-shop-plugin">here</a>

### Starting the web server
Run the `main.py` file, and congratulations! You successfully set everything up

## Security issues
For security issues, refrain from creating a regular pull request/issue. Instead, send me an <a href="mailto:giornogiovannabusiness@gmail.com">email</a> instead. Its safer that way. 

## License
This project is licensed under the MIT License
