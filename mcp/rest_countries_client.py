#!/usr/bin/env python3
"""
Real MCP Client - REST Countries API
Demonstrates client-server communication with a real REST API
"""

import requests
import json
from typing import List, Dict, Optional


class RESTCountriesClient:
    """
    A real MCP client that connects to the REST Countries API
    REST Countries is a free public API with no authentication needed
    API Documentation: https://restcountries.com
    """
    
    def __init__(self, base_url="https://restcountries.com/v3.1"):
        """
        Initialize the REST Countries client
        
        Args:
            base_url: The base URL for the REST Countries API
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "RESTCountriesClient/1.0"
        })
    
    def create_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Create a request structure (similar to JSON-RPC pattern)
        
        Args:
            endpoint: API endpoint (e.g., "/all", "/name/canada")
            params: Query parameters
            
        Returns:
            Dictionary representing the request
        """
        request = {
            "method": "GET",
            "url": f"{self.base_url}{endpoint}",
            "params": params or {},
            "headers": dict(self.session.headers)
        }
        return request
    
    def send_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Send a request to REST Countries API
        
        Args:
            endpoint: API endpoint
            params: Query parameters
            
        Returns:
            Response data from the API
        """
        request = self.create_request(endpoint, params)
        
        print(f"\n📤 Sending request to REST Countries API:")
        print(f"   URL: {request['url']}")
        if request['params']:
            print(f"   Params: {request['params']}")
        
        try:
            response = self.session.get(
                request['url'],
                params=request['params'],
                timeout=10
            )
            response.raise_for_status()  # Raise error for bad status codes
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Error: {e}")
            return None # type: ignore
    
    def receive_response(self, response_data, title: str = "Response"):
        """
        Display and parse the API response
        
        Args:
            response_data: Data from the API
            title: Title for the response section
        """
        if response_data is None:
            print(f"\n❌ No response data")
            return
        
        print(f"\n📥 {title}:")
        print(json.dumps(response_data, indent=2, default=str))
    
    def get_all_countries(self) -> Optional[List[Dict]]:
        """
        Fetch all countries
        
        Returns:
            List of all countries with their data
        """
        print("\n" + "="*70)
        print("Fetching ALL countries from REST Countries API")
        print("="*70)
        
        response = self.send_request("/all")
        
        if response:
            print(f"\n✅ Successfully retrieved {len(response)} countries")
            return response # type: ignore
        else:
            print(f"\n⚠️  Note: The /all endpoint is not available (API limitation)")
            print(f"   You can fetch countries by specific code or name instead")
        return None
    
    def get_country_by_name(self, country_name: str) -> Optional[List[Dict]]:
        """
        Fetch country by name
        
        Args:
            country_name: Name of the country to search
            
        Returns:
            List of matching countries
        """
        print("\n" + "="*70)
        print(f"Searching for country: {country_name}")
        print("="*70)
        
        response = self.send_request(f"/name/{country_name}")
        
        if response:
            print(f"\n✅ Found {len(response)} match(es)")
            return response # type: ignore
        return None
    
    def get_country_by_code(self, country_code: str) -> Optional[Dict]:
        """
        Fetch country by ISO 3166-1 alpha-3 code
        
        Args:
            country_code: 3-letter country code (e.g., 'USA', 'CAN', 'AUS')
            
        Returns:
            Country data
        """
        print("\n" + "="*70)
        print(f"Searching for country code: {country_code}")
        print("="*70)
        
        response = self.send_request(f"/alpha/{country_code.upper()}")
        
        if response:
            # API returns a list, get the first item
            country = response[0] if isinstance(response, list) else response
            print(f"\n✅ Found country: {country.get('name', {}).get('common', 'Unknown')}")
            return country
        return None
    
    def display_country_summary(self, country: Dict):
        """
        Display a summary of country data
        
        Args:
            country: Country dictionary from API
        """
        if not country:
            return
        
        name = country.get('name', {})
        print("\n" + "-"*70)
        print(f"Country: {name.get('common', 'Unknown')}")
        print(f"Official: {name.get('official', 'N/A')}")
        print(f"Capital: {country.get('capital', ['N/A'])[0]}")
        print(f"Region: {country.get('region', 'N/A')}")
        print(f"Subregion: {country.get('subregion', 'N/A')}")
        print(f"Population: {country.get('population', 'N/A'):,}")
        print(f"Area: {country.get('area', 'N/A')} km²")
        print(f"Timezones: {', '.join(country.get('timezones', ['N/A']))}")
        print(f"Languages: {country.get('languages', {})}")
        print(f"Currencies: {country.get('currencies', {})}")
        print("-"*70)


def main():
    """Main demonstration of REST Countries API client"""
    
    print("="*70)
    print("🌍 Real MCP Client - REST Countries API")
    print("="*70)
    
    # Create a client
    client = RESTCountriesClient()
    
    # Example 1: Get a specific country by code
    print("\n\n" + "#"*70)
    print("# Example 1: Get country by ISO code")
    print("#"*70)
    
    country_data = client.get_country_by_code("USA")
    if country_data:
        client.receive_response(country_data, "Country Data (USA)")
        client.display_country_summary(country_data)
    
    # Example 2: Search by country name
    print("\n\n" + "#"*70)
    print("# Example 2: Search by country name")
    print("#"*70)
    
    countries = client.get_country_by_name("Canada")
    if countries:
        client.receive_response(countries, "Search Results (Canada)")
        if countries:
            client.display_country_summary(countries[0])
    
    # Example 3: Search another country
    print("\n\n" + "#"*70)
    print("# Example 3: Another country search")
    print("#"*70)
    
    countries = client.get_country_by_name("Japan")
    if countries:
        client.receive_response(countries, "Search Results (Japan)")
        if countries:
            client.display_country_summary(countries[0])
    
    # Example 4: Get all countries (just the count)
    print("\n\n" + "#"*70)
    print("# Example 4: Get count of all countries")
    print("#"*70)
    
    all_countries = client.get_all_countries()
    if all_countries:
        print(f"\n📊 Total countries in database: {len(all_countries)}")
        print("\nFirst 3 countries:")
        for i, country in enumerate(all_countries[:3], 1):
            name = country.get('name', {}).get('common', 'Unknown')
            region = country.get('region', 'N/A')
            print(f"   {i}. {name} ({region})")
    
    print("\n\n" + "="*70)
    print("✅ REST Countries Client Examples Complete!")
    print("="*70)
    
    print("\n📚 Key Learning Points:")
    print("  1. CLIENT: This Python script (makes requests)")
    print("  2. SERVER: REST Countries API (responds to requests)")
    print("  3. PROTOCOL: HTTP/REST (standard web protocol)")
    print("  4. REQUEST: GET /name/Canada (what we ask for)")
    print("  5. RESPONSE: JSON with country data (what we get)")
    print("  6. This is real client-server communication!")


if __name__ == "__main__":
    main()
