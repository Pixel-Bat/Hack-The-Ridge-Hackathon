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
        Print30Lines()

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