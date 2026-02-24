# TOML Files Overview

## What is TOML?

**TOML** (Tom's Obvious, Minimal Language) is a configuration file format that's designed to be easy to read and write. 
It's commonly used for:
- Application configuration files
- Python package management (pyproject.toml)
- Build system configurations
- Settings and preferences

TOML maps to hash tables/dictionaries and uses a simple key-value syntax with support for nested structures.

---

## Files in this Directory

### Python Scripts

#### 1. `my_tomlib.py`
- **Purpose**: Demonstrates reading TOML files using Python's built-in `tomllib` module
- **Library**: `tomllib` (Python 3.11+ standard library)
- **Reads**: `eg.toml`
- **Operation**: Parses and prints the entire TOML structure
- **Use case**: Modern, no-dependency TOML reading

#### 2. `my_toml.py`
- **Purpose**: Demonstrates reading TOML files using the third-party `toml` package
- **Library**: `toml` (requires `pip install toml`)
- **Reads**: `config.toml`
- **Operation**: Parses TOML and prints specific fields (title, owner info)
- **Use case**: Compatible with older Python versions (< 3.11)

#### 3. `programatic-toml.py`
- **Purpose**: Demonstrates creating/writing TOML files programmatically
- **Library**: `toml` (requires `pip install toml`)
- **Writes**: `programatic-config.toml`
- **Operation**: Converts Python dictionary to TOML format and saves to file
- **Use case**: Generating configuration files from code

---

### TOML Data Files

#### 1. `eg.toml`
- **Type**: Poetry package configuration example
- **Used by**: `my_tomlib.py`
- **Content**: Sample Python package metadata with dependencies
- **Structure**:
  - Project metadata (name, version)
  - Dependencies with version constraints
  - Build system configuration

#### 2. `config.toml`
- **Type**: Simple configuration file
- **Used by**: `my_toml.py`
- **Content**: Basic title and owner information
- **Structure**:
  - Title section with name
  - Owner section with name and date of birth

#### 3. `programatic-config.toml`
- **Type**: Generated configuration file
- **Created by**: `programatic-toml.py`
- **Content**: Title and owner data (similar to config.toml)
- **Purpose**: Output from programmatic TOML generation

#### 4. `programatic-config01.toml`
- **Type**: Duplicate/backup file
- **Status**: Appears to be unused or a test output
- **Content**: Identical to `programatic-config.toml`

---

## Quick Reference

### Reading TOML (Modern Python 3.11+)
```python
import tomllib
with open("file.toml", "rb") as f:
    data = tomllib.load(f)
```

### Reading TOML (Python < 3.11)
```python
import toml
with open("file.toml", "r") as f:
    data = toml.load(f)
```

### Writing TOML
```python
import toml
data = {'key': 'value'}
with open("file.toml", "w") as f:
    toml.dump(data, f)
```

---

## File Relationships

```
my_tomlib.py ────reads───→ eg.toml
my_toml.py ──────reads───→ config.toml
programatic-toml.py ──creates──→ programatic-config.toml
```

---

## Learning Path

1. **Start with**: `my_toml.py` + `config.toml` - Basic TOML reading
2. **Then try**: `programatic-toml.py` - Creating TOML files
3. **Finally**: `my_tomlib.py` + `eg.toml` - Using modern built-in library
