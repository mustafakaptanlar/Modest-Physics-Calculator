import subprocess #import library

choice = input("What you want to calculate : ") #user choices which calculation he/she wants to do.

if choice == "acceleration":
    subprocess.call(["python", "Formulas/Acceleration.py"]) #Calls Acceleration Formula
if choice == "density":
    subprocess.call(["python", "Formulas/Density.py"]) #Calls Density Formula
if choice == "average speed":
    subprocess.call(["python", "Formulas/Average Speed.py"]) #Calls Average Speed Formula
