import folium
import os, sys, subprocess
from pathlib import Path
import platform
from countryinfo import CountryInfo
import wikipediaapi as wiki
import pygame

#colours
background_colour = (234, 212, 252)
white = (0, 0, 0)

#wikipedia stuff
Country = 'forks'
wiki_wiki = wiki.Wikipedia('MyProjectName', 'en')
page_py = wiki_wiki.page(Country)

#pygame stuff
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('A Brief Overview')
Icon = pygame.image.load('globe.png')
my_font = pygame.font.SysFont('arial', 24)
pygame.display.set_icon(Icon)
screen.fill(background_colour)
font = pygame.sysfont.SysFont('arial', 24)
MAX_WIDTH_YOU_WOULD_LIKE = 500
limit_pixel_width = max(MAX_WIDTH_YOU_WOULD_LIKE, 24 * 5)
text_surface = my_font.render(page_py.summary[0:1000], True, white)
screen.blit(text_surface, (0,0))
pygame.display.flip()

running = True

#folium stuff
filelocation = "interactive_map.html"

whatOS = platform.system()

#check if os is mac
if whatOS == "Darwin":

    print("OS is Mac")

    #print summary of location
    print("Title: %s" % page_py.title)
    print("Summary: %s" % page_py.summary[0:1000])

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
        popup="San Francisco<br>ugly",
        icon=folium.Icon(color="blue"),
    ).add_to(m)

        # Save the map as an HTML file
    m.save(filelocation)

    command = (f"open -a 'Google Chrome' {filelocation}")
    subprocess.Popen(command, shell=True)

    while running:
        for event in pygame.event.get(): 
      
        # Check for QUIT event       
            if event.type == pygame.QUIT: 
                running = False
        page_py = wiki_wiki.page(Country)

#check if os is windows
if whatOS == "Windows":

    print("OS is Windows")

    #print summary of location
    print("Title: %s" % page_py.title)
    print("Summary: %s" % page_py.summary[0:1000])

    my_file = Path(filelocation)
    if my_file.is_file():
        fileExist = 1
    else:
        fileExist = 0

    if fileExist == 1:
        os.remove(".\interactive_map.html")

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

    os.system(".\interactive_map.html")

    while running:
        for event in pygame.event.get(): 
      
        # Check for QUIT event       
            if event.type == pygame.QUIT: 
                running = False
        page_py = wiki_wiki.page(Country)