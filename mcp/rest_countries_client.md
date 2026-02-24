# Real REST API Client - REST Countries Integration

## Overview

This is a **real, working API client** that connects to the **REST Countries API** to fetch live country data. Unlike the mock client, this makes actual HTTP requests and parses real JSON responses.

**What it teaches:**
- How to make real HTTP requests in Python
- Parsing JSON responses
- Error handling for API failures
- Building practical client applications

## What It Does

The script fetches detailed information about countries worldwide:

```
┌──────────────────────────────────────────┐
│   REST Countries API Client              │
│                                          │
│ 1. get_country_by_code("USA")           │
│ 2. get_country_by_name("Canada")        │
│ 3. get_all_countries() [handles errors] │
│                                          │
│    ↓ HTTP GET requests ↓                │
│                                          │
│ REST Countries API (restcountries.com)  │
│    ↓ Returns JSON ↓                     │
│                                          │
│ Parse & Display:                        │
│ - Population, Capital, Languages        │
│ - Currencies, Timezones, Borders        │
│ - Region, Area, Official Names          │
└──────────────────────────────────────────┘
```

## How to Install and Run

### Prerequisites
- Python 3.14.2
- Located in: `/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/mcp/`
- Shared virtual environment at: `../../../.venv/`

### Step 1: Activate Virtual Environment
```bash
cd /Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps
source .venv/bin/activate
```

### Step 2: Run the Script
```bash
cd mcp
python rest_countries_client.py
```

### Step 3: View Full Output (Optional)
If terminal output is truncated, redirect to file:
```bash
python rest_countries_client.py > rest_countries_client.txt
```

### Expected Output
```
======================================================================
🌍 Real MCP Client - REST Countries API
======================================================================

# Example 1: Get country by ISO code
======================================================================
Searching for country code: USA
======================================================================

📤 Sending request to REST Countries API:
   URL: https://restcountries.com/v3.1/alpha/USA

✅ Found country: United States

📥 Country Data (USA):
{
  "name": {...},
  "population": 338289857,
  "capital": ["Washington, D.C."],
  "region": "Americas",
  ...
}

----------------------------------------------------------------------
Country: United States
Official: United States of America
Capital: Washington, D.C.
Population: 338,289,857
...
```

## Technology & Libraries

| Library | Version | Purpose | Why Used |
|---------|---------|---------|----------|
| **requests** | 2.32.5 | HTTP client | Easy HTTP requests, handles errors gracefully |
| **json** | Built-in | Parse responses | Standard for API response formatting |
| **typing** | Built-in | Type hints | Improves code clarity and IDE support |

### Installation (Already Installed in `.venv`)
```bash
pip install requests
```

## Code Structure

```python
class RESTCountriesClient:
    ├── __init__()              # Initialize with base URL
    ├── create_request()        # Build request structure
    ├── send_request()          # Make actual HTTP call
    ├── receive_response()      # Parse JSON response
    ├── get_country_by_code()   # Fetch by ISO 3166-1 alpha-3 code
    ├── get_country_by_name()   # Search by country name
    ├── get_all_countries()     # Fetch all countries (handles 400 error)
    └── display_country_summary()# Format data for display

main():
    ├── Example 1: Get USA by code
    ├── Example 2: Search for Canada by name
    ├── Example 3: Search for Japan by name
    ├── Example 4: Get all countries (graceful error handling)
    └── Display learning outcomes
```

## API Endpoints Used

```
Base URL: https://restcountries.com/v3.1

/alpha/{code}       → Get by 3-letter code (e.g., USA, CAN, JPN)
/name/{name}        → Search by country name (e.g., Canada)
/all                → Get all countries (returns 400 - not supported)
```

## Data Returned

Each country response includes:
```json
{
  "name": {
    "common": "United States",
    "official": "United States of America"
  },
  "population": 338289857,
  "area": 9833520,
  "capital": ["Washington, D.C."],
  "region": "Americas",
  "subregion": "North America",
  "languages": {"eng": "English"},
  "currencies": {
    "USD": {"name": "United States dollar", "symbol": "$"}
  },
  "timezones": ["UTC-12:00", "UTC-11:00", ..., "UTC+12:00"],
  "borders": ["CAN", "MEX"],
  ... (50+ fields total)
}
```

## Key Features

✅ **Real HTTP Requests** - Makes actual API calls, not mocked
✅ **Error Handling** - Gracefully handles API failures (400 errors)
✅ **Type Hints** - Clear function signatures with Python typing
✅ **Formatted Output** - Pretty-prints country data
✅ **Session Management** - Reuses HTTP session for efficiency

## Error Handling

The script handles API errors gracefully:

```python
try:
    response = self.session.get(...)
    response.raise_for_status()  # Raise error for 4xx/5xx
    return response.json()
except requests.exceptions.RequestException as e:
    print(f"❌ Error: {e}")
    return None
```

**Special Case:** The `/all` endpoint returns a 400 error (API limitation). The script catches this and prints a helpful message instead of crashing.

## Learning Outcomes

After running this script, you'll understand:
- ✅ How to make HTTP requests with the `requests` library
- ✅ How to parse JSON responses from APIs
- ✅ How to handle API errors gracefully
- ✅ How to build real client applications
- ✅ The difference between mock and real clients

## Comparison: Mock vs Real Client

| Feature | Mock Client | Real Client |
|---------|------------|------------|
| Network calls | ❌ None (simulated) | ✅ Real HTTP requests |
| Data source | 📝 Hardcoded responses | 🌐 Live REST Countries API |
| Error handling | 📋 Simple format | 🛡️ Try/except blocks |
| Use case | 🎓 Learning protocols | 🚀 Production-ready |

## Common API Calls

```python
# Get a specific country
country = client.get_country_by_code("USA")
client.display_country_summary(country)

# Search by name
results = client.get_country_by_name("Canada")
if results:
    client.display_country_summary(results[0])

# Get all countries (will fail gracefully)
all_countries = client.get_all_countries()
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: requests` | Activate `.venv`: `source .venv/bin/activate` |
| No output displayed | Redirect to file: `python script.py > output.txt` |
| API timeout | Check internet connection, try again |
| 400 error on `/all` | This is expected - API doesn't support it |

## Next Steps

1. **Extend it** - Add filtering by region, population range, etc.
2. **Store results** - Save API responses to a database
3. **Build a CLI** - Add command-line arguments for queries
4. **Create a web UI** - Build a Flask/Django app using this client

## Files

- `rest_countries_client.py` - Main script (~8KB)
- `rest_countries_client.txt` - Sample output (if redirected)

## References

- **REST Countries API**: https://restcountries.com/
- **requests Library**: https://requests.readthedocs.io/
- **HTTP Status Codes**: https://httpwg.org/specs/rfc7231.html#status.codes

## Notes

- All data is fetched from a **public, free API** (no authentication needed)
- The script respects API rate limits (no excessive requests)
- Responses are **real, live data** - country info updates with API
