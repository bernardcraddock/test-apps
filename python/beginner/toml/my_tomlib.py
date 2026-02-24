import tomllib
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
toml_file = script_dir / "eg.toml"

with open(toml_file, "rb") as f:
    data = tomllib.load(f)

print(data)
