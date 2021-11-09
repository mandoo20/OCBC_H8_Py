#py 026_h8ocbc_converter.py for run this apps!

def c_to_k_vice_versa(numberS, toS):
    '''
    Celcius to Kelvin vice versa
    '''
    if toS.upper() == "K":
            value = float(numberS + 273.15)
            return str(round(value,2))
    else:
        value = float(numberS - 273.15)
        return str(round(value,2))

def f_to_k_vice_versa(numberS, toS):
    '''
    Fahrenheit to Kelvin vice versa
    '''
    if toS.upper() == "K":
            value = float((numberS - 32) * 5/9 + 273.15)
            return str(round(value,2))
    else:
        value = float((numberS - 273.15) * 9/5 + 32)
        return str(round(value,2))

def f_to_c_vice_versa(numberS, toS):
    '''
    Fahrenheit to Celsius vice versa
    '''
    if toS.upper() == "C":
            value = float((numberS - 32) * 5/9)
            return str(round(value,2))
    else:
        value = float((numberS * 9/5) + 32)
        return str(round(value,2))



def temperatureConverter(fromI, to):
    '''
    This function is used to convert temperature.
    :param fromI: Input initial Temperature | string
    :param to: Input target convert(C || K || F) | string
  
    :return: print value: convert Temperature | print string
    '''
    try:
        number = int(fromI[:-1])
        tempKey = fromI[-1]
    except ValueError:
        errMess()

    else:
        if tempKey.upper() == "C":
            if to.upper() == "K":
                print("Celsius to Kelvin: "+ c_to_k_vice_versa(number,to) + " K")
            elif to.upper() == "F":
                print("Celsius to Fahrenheit: "+ f_to_c_vice_versa(number,to) + " °F")
            else:
                errMess()

        elif tempKey.upper() == "K":
            if to.upper() == "C":
                value = float(number - 273.15)
                print("Kelvin to Celsius: "+ c_to_k_vice_versa(number,to) + " °C")
            elif to.upper() == "F":
                print("Kelvin to Fahrenheit: " + f_to_k_vice_versa(number,to) + " °F")
            else:
                errMess()
        elif tempKey.upper() == "F":
            if to.upper() == "C":
                print("Fahrenheit to Celsius: "+ f_to_c_vice_versa(number,to) + " °C")
            elif to.upper() == "K":
                print("Fahrenheit to Kelvin: "+ f_to_k_vice_versa(number,to) + " K")
            else:
                errMess()
        else:
            errMess()



def printSpace():
    '''
    for print space while looping menu converter
    '''
    for lop in range(2):
        print("")

def errMess():
    '''
    for print repeatitive error message on temperatureConverter function
    '''
    print("Wrong Input Value! Please Try again [ex value: 30c || 20F || 5K]")
    print("(not case sensitive!! AND Cannot convert to same temperature[ex: 30c to c])")

flag = 0
while flag == 0:
    printSpace()
    inputStr = input("\nTemperature[ex: 30c,55F,26k or x(for exit)]: ")
    if inputStr != "x":
        toStr = input("\nConvert To[C || k || F]: ")
        temperatureConverter(inputStr, toStr)
    else:
        flag = 1
printSpace()
print("Thankyou!")
