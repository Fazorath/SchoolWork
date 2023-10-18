def makecar(manufacturer,modelname,**information):
    information["Manufacturer"] = manufacturer
    information["Mode"] = modelname
    return information


camaro = makecar("Chevy","Camaro",Color='White',Displacement="2.0lt Turbo", Seating=2, TopSpeed=160) 
print(camaro)
