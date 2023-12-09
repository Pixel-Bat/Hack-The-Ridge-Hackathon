from countryinfo import CountryInfo

def gatherinfo(country):
    name=country

    returnlist = []

    country = CountryInfo(name)

    returnlist.append(country.capital())

    returnlist.append(country.currencies())

    returnlist.append(country. languages())

    returnlist.append(country.borders())

    returnlist.append(country.provinces())

    returnlist.append(country.area())

    returnlist.append(country.calling_codes())

    returnlist.append(country.capital_latlng())

    returnlist.append(country.timezones())

    returnlist.append(country.population())

    returnlist.append(country.alt_spellings())
    return returnlist