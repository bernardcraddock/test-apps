import toml
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
config_file = script_dir / "config.toml"

with open(config_file, "r") as f:
    data = toml.load(f)

print(data['title']['name'])
print(data['owner']['name'])
print(data['owner']['dob'])
print(data)
