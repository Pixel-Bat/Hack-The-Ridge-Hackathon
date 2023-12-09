import folium
import os, sys, subprocess
from pathlib import Path
import platform

filelocation = "interactive_map.html"

whatOS = platform.system()

if whatOS == "Darwin":

    print("OS is Mac")

    if os.getuid() == 0:
        print("Root access Granted")

    else:
        print("Root required in order to load map")
        subprocess.call(['sudo', 'python3', *sys.argv])
        sys.exit()

    my_file = Path(filelocation)
    if my_file.is_file():
        fileExist = 1
    else:
        fileExist = 0

    if fileExist == 1:
        command = (f"rm {filelocation}")
        subprocess.Popen(command, shell=True)

    # Create a base map centered at a specific location
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=12)

    # Add a marker to the map
    folium.Marker(
        location=[37.7749, -122.4194],
        popup="San Francisco",
        icon=folium.Icon(color="blue"),
    ).add_to(m)

        # Save the map as an HTML file
    m.save(filelocation)

    command = (f"open -a 'Google Chrome' {filelocation}")
    subprocess.Popen(command, shell=True)

if whatOS == "Windows":
    print("OS is windows")
    exit()