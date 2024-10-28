def calculate_wind_chill(temp_f, wind_speed_mph):
    wind_chill = 35.74 + 0.6215 * temp_f - 35.75 * (wind_speed_mph ** 0.16) + 0.4275 * temp_f * (wind_speed_mph ** 0.16)
    return wind_chill

def convert_celsius(celcius):
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit

temperature = float(input('What is the temperature? '))
user_value = input('Fahrenheit or Celsius (F/C)? ').strip().upper()

if user_value == 'C':
    fahrenheit = convert_celsius(temperature)
else:
    fahrenheit = temperature

for wind_speed in  range(5, 61, 5):
    wind_clill = calculate_wind_chill(temp_f=fahrenheit, wind_speed_mph=wind_speed)
    print(f'At temperature {fahrenheit}F, and wind speed {wind_speed} mph, the windchill is: {wind_clill:.2f}F')
