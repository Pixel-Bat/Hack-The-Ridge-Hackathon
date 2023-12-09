import wbdata
import datetime

def get_country_gdp_history(country_code, indicator="NY.GDP.MKTP.CD", start_date="1960", end_date="2020"):
    data_date = (datetime.datetime(int(start_date), 1, 1), datetime.datetime(int(end_date), 1, 1))
    data = wbdata.get_dataframe(indicators={indicator: "GDP (current US$)"}, country=country_code, data_date=data_date)
    return data

# Example: Fetching GDP history for the United States
country_code_usa = "USA"
gdp_data_usa = get_country_gdp_history(country_code_usa)

print(f"GDP History for {country_code_usa}:\n")
print(gdp_data_usa.head())
