FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#the funcions
def convert_to_celsius(fahrenheit):
    temperature_celsius = (temperature_farenheit - 32)* FAHRENHEIT_TO_CELSIUS_FACTOR
    print(str(temperature_farenheit)+"°F is "+str(temperature_celsius)+"°C")

def convert_to_fahrenheit(celsius):
    temperature_farenheit = (temperature_celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(str(temperature_celsius)+"°C is "+str(temperature_farenheit)+"°F")

#Enter data
temperature=float(input("Enter the temperature to convert: "))

#validating user inputs
if type(temperature) == float:
    units=input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip()
    if units == "f":
        temperature_farenheit=temperature
        convert_to_celsius(temperature_farenheit)
    elif units == "c":
        temperature_celsius = temperature
        convert_to_fahrenheit(temperature_celsius)
    else:
        print ("Invalid temperature. Please enter a C/F.")
else:
    print("Invalid temperature. Please enter a numeric value.")


    

