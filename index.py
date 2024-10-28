
def calculate_wind_chill(temperature, wind_speed):
    if temperature < 50:
        wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed**0.16 + 0.4275 * temperature * wind_speed
        return round(wind_chill, 2)
    else:
        return temperature
    
def convert_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def main():
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or celsius (F/C)? ")

    if unit.upper() == "C":
        temperature = convert_to_fahrenheit(temperature)

    print("Wind Chill Values:")
    print("------------------")
    for wind_speed in range(5, 65, 5):
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At temperature {temperature}F and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}")

if __name__ == '__main__':
    main() 