import folium as folium
from streamlit_folium import st_folium
import streamlit as st
from geopy.geocoders import Nominatim
from countryinfo import CountryInfo


st.set_page_config(layout="wide")

def get_pos(lat, lng):
    return lat, lng


m = folium.Map(location=[47.7749, 14.4194], zoom_start=3)







#m.add_child(folium.Popup("test"))


map = st_folium(m, height=1000, width=3000)

data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])

    geolocator = Nominatim(user_agent="geo_info")
    location = geolocator.reverse((data[0], data[1]), language='en')

    latf = open("lat.txt", "w")
    latf.write(str(data[0]))
    latf.close()

    lngf = open("lng.txt", "w")
    lngf.write(str(data[1]))
    lngf.close()

    # Extract the country from the location details
    
    country = location.raw.get('address', {}).get('country', 'Country not found')
    f = open("country.txt", "w")
    f.write(str(country))
    f.close()


def gatherinfo(country):
    name=country

    returnlist = []

    country = CountryInfo(name)

    returnlist.append(country.capital())

    returnlist.append(country.currencies())

    returnlist.append(country. languages())

    returnlist.append(country.borders())

    #returnlist.append(country.provinces())

    returnlist.append(country.area())

    #returnlist.append(country.calling_codes())

    #returnlist.append(country.capital_latlng())

    #returnlist.append(country.timezones())

    returnlist.append(country.population())

    #returnlist.append(country.alt_spellings())
    return returnlist



#folium.Marker(
#    location=[data[0], data[1]],
#    popup="test",
#    icon=folium.Icon(color="blue"),
#).add_to(m)


if data is not None:
    st.write(data) # Writes to the app
    #print(data) # Writes to terminal
    print(country)
    print(gatherinfo(country))