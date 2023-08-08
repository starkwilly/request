import requests

# API endpoint URL
api_url = "https://api.amadeus.com/v1/cars/search"

# API credentials
client_id = "your_client_id"
client_secret = "your_client_secret"

# Construct the XML payload
xml_payload = """
<CarAvailability>
    <PickupLocation>Houston, Texas</PickupLocation>
    <DropOffLocation>Los Alamos, New Mexico</DropOffLocation>
    <PickupDateTime>2023-08-15T10:00:00</PickupDateTime>
    <DropOffDateTime>2023-08-20T14:00:00</DropOffDateTime>
</CarAvailability>
"""

# Set headers
headers = {
    "Content-Type": "application/xml",
    "Authorization": f"Bearer {access_token}"  # Include the access token if required
}

# Send the POST request
response = requests.post(api_url, data=xml_payload, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Parse the response content (XML)
    response_xml = response.content.decode("utf-8")
    print(response_xml)
else:
    print("Request failed with status code:", response.status_code)
    print(response.text)  # Print error details if available
