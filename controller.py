from c_ncie_data_service_api import c_ncie_data_service_api

api_result = c_ncie_data_service_api('daily-summaries', 'TMIN,TMAX,TOBS,DAPR,MDPR,PRCP,SNOW,SNWD,AWND,ACMH,ACSH,PSUN', 'USW00012921', '2021-01-01', '2021-11-05', '90,-180,-90,180', 'json')
print(api_result.get_data())
api_result.write_data_file('weather_data_san_antonio.json')

# National Data Buoy Center: https://www.ndbc.noaa.gov/ (Examples: AUCE, WHRI2)
# Rochester International Airport: USW00014925; Chicago O'Hare International Airport: USW00094846; San Jose International Airport: USW00023293
