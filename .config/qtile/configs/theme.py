from os import path
import toml
from getpass import getuser


# Get the path of the current Qtile config file
config_dir = "/home/" + getuser() + "/.config/qtile"

# Construct the path to the JSON file within the folder
json_file_path = path.join(config_dir, "themes", "nord.toml")

with open(json_file_path, "r") as file:
    colors = toml.load(file)
