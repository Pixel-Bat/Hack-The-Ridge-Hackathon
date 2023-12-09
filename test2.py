import folium as folium
from streamlit_folium import st_folium
import streamlit as st
from geopy.geocoders import Nominatim



st.set_page_config(layout="wide")

def get_pos(lat, lng):
    return lat, lng


m = folium.Map()

m.add_child(folium.LatLngPopup())


map = st_folium(m, height=1000, width=3000)

data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])

    geolocator = Nominatim(user_agent="geo_info")
    location = geolocator.reverse((data[0], data[1]), language='en')

    # Extract the country from the location details
    
    country = location.raw.get('address', {}).get('country', 'Country not found')
    f = open("country.txt", "w")
    f.write(str(country))
    f.close()




if data is not None:
    st.write(data) # Writes to the app
    print(data) # Writes to terminal
    print(country)