#BMI calculator

#Gather information about the client
def gather_info():
    height = float(input("Please enter your height(in m): "))
    weight = float(input("Please enter your weight(in kg): "))
    units = input("Are your measurements in imperial or metric units? ").lower().strip()
    return (height,weight,units)

def calculate_BMI(height,weight,units='metric'):
    """
    We will return BMI figures by calculating below
    """
    if units == 'metric':
        bmi = (weight / (height ** 2)) 
        return round(bmi)
    else:
        bmi = 703 * (weight / (height ** 2))
        return round(bmi)

while True:
    height,weight, units = gather_info()
    if units.startswith("i"):
        bmi = calculate_BMI(height=height, weight=weight, units='imperial')
        print (f"Your BMI is {bmi} ")
        break
    if units.startswith("m"):
        bmi = calculate_BMI(height=height, weight=weight, units='metric')
        print (f"Your BMI is {bmi} ")
        break
    else:
        print("Error: Unknown measurement system. Please use imperial or metric.")



