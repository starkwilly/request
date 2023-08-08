import xml.etree.ElementTree as ET

# Assuming you already have the 'response_xml' from the previous example also living in this repository

# Parse the XML response
root = ET.fromstring(response_xml)

# Extract information from the parsed XML
vehicle_type = root.find(".//Type").text
vehicle_make = root.find(".//Make").text
max_passengers = root.find(".//MaxPassengers").text
num_doors = root.find(".//NumDoors").text
vehicle_photo_url = root.find(".//PhotoURL").text

# Print the extracted information
print("Vehicle Type:", vehicle_type)
print("Vehicle Make:", vehicle_make)
print("Max Passengers:", max_passengers)
print("Number of Doors:", num_doors)
print("Vehicle Photo URL:", vehicle_photo_url)
