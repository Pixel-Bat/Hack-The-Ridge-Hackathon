from countryinfo import CountryInfo


# Input the Name of the Country
name=input("Enter your country: ")

# Passing the country name to the in-built function of the module
country = CountryInfo(name)

# Printing all the details using the Pre-defined Functions

# 1) Printing the Capital of the Country
print("Capital is: ",country.capital())

# 2) Printing the Currency used in the Country
print("Currencies is: ",country.currencies())

# 3) Printing the Languages spoken in the Country
print("Language is: ",country. languages())

# 4) Printing the Borders of the Country and Function
# returns bordering countries (ISO3) for a specified country
print("Borders are: ",country.borders())

# 5) Printing the Provinces of the Country
print("Provinces are: ", country.provinces())

# 8) Printing the Latitudes and Longitudes of the Country
print("Capital Latitudes and Longitudes are: ", 
						country.capital_latlng())

# 9) Printing the TimeZone in the Country
print("TimeZone: ", country.timezones())

# 10) Printing the Current Population in the Country
print("Population: ", country.population())

# 11) Printing the Other Names of the Country
print("Others names: ",country.alt_spellings())