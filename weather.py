import geocoder

# Get city name from user
place = input("Enter City Name: ")

# Geocode the location
location = geocoder.osm(place)

# Check if location was found
if location.ok:
    # Get weather information from user
    weather = input("Enter Weather for the Day: ")

    # Print the geolocation details and weather information
    print("Geolocation Details:")
    print(location.json)
    print("Weather for the Day:", weather)
else:
    print("Location not found.")
