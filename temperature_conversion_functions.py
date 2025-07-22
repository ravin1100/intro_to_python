
def celsius_to_farenheit(cel_temp):
    print(f"{cel_temp}°C = {cel_temp * (9 / 5) + 32}°F")

def fahrenheit_to_kelvin(fah_temp):
    print(f"{fah_temp}°F = {((fah_temp - 32) * 5 / 9) + 273.15}°K")

def kelvin_to_celsius(kel_temp):
    print(f"{kel_temp}°K = {kel_temp - 273.15}°C")


celsius_to_farenheit(0)
fahrenheit_to_kelvin(32)
kelvin_to_celsius(300)