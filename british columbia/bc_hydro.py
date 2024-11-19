import requests
import json

# Define the URL for the outages data
url = "https://www.bchydro.com/power-outages/app/outages-map-data.json"

# Define headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://www.bchydro.com",
    "Referer": "https://www.bchydro.com/power-outages/app/outage-map.html"
}

# Make the GET request to fetch the outage data
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON data
    outages = []
    
    for outage in data:
        # Include polygon data in each outage entry
        outages.append({
            "id": outage['id'],
            "municipality": outage.get('municipality', 'N/A'),
            "area": outage.get('area', 'N/A'),
            "cause": outage.get('cause', 'Unknown'),
            "numCustomersOut": outage.get('numCustomersOut', 'N/A'),
            "crewStatusDescription": outage.get('crewStatusDescription', 'N/A'),
            "latitude": outage['latitude'],
            "longitude": outage['longitude'],
            "dateOff": outage.get('dateOff', 'Unknown'),
            "crewEta": outage.get('crewEta', 'Unknown'),
            "polygon": outage.get('polygon', [])  # Add polygon data here
        })
    
    # Print the final JSON output
    print(json.dumps(outages))
else:
    print(json.dumps({"error": f"Failed to fetch data, status code {response.status_code}"}))
