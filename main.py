# We need an interactive map to show areas affected by the flood in Valencia
# We will use the folium library to create the map
# We will use the pandas library to read the data from a csv file
# We will use the geopy library to get the coordinates of Valencia
# We will use the geopy library to get the coordinates of the affected areas
# We will use the geopy library to calculate the distance between Valencia and the affected areas



import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy import distance

# Read the data from the csv file
df = pd.read_csv('flood.csv')

# Get the coordinates of Valencia
geolocator = Nominatim(user_agent="flood_map")

location = geolocator.geocode("Valencia, Spain")
valencia_lat = location.latitude
valencia_lon = location.longitude

# Create the map
m = folium.Map(location=[valencia_lat, valencia_lon], zoom_start=10)

# Add a marker for Valencia
folium.Marker([valencia_lat, valencia_lon], popup='Valencia').add_to(m)

# Add a marker for each affected area
for index, row in df.iterrows():
    location = geolocator.geocode(row['Area'])
    area_lat = location.latitude
    area_lon = location.longitude
    folium.Marker([area_lat, area_lon], popup=row['Area']).add_to(m)
    distance = geodesic((valencia_lat, valencia_lon), (area_lat, area_lon)).km
    print(f"The distance between Valencia and {row['Area']} is {distance:.2f} km")

# Save the map to an html file
m.save('flood_map.html')
