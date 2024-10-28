def calculate_wind_chill(temperature, wind_speed):
    # you do not need to check if tempereature less than 50
    # you forget to power last value to 0.16
        wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed**0.16 + 0.4275 * temperature * wind_speed**0.16
        return wind_chill
    
def convert_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def main():
    temperature = float(input("What is the temperature? "))
    unit = input("Fahrenheit or celsius (F/C)? ")

    if unit.upper() == "C":
        temperature = convert_to_fahrenheit(temperature)

    print("Wind Chill Values:")
    print("------------------")
    # you need to write range(5, 61, 5) than (5, 65, 5) because you only need the wind speed up to 60 mph and you need to write 61 because it counts up to 61,
    # so the last number written will be 60.
    for wind_speed in range(5, 61, 5):
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At temperature {temperature}F and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}")

if __name__ == '__main__':
    main()       