import subprocess #import library

choice = input("What you want to calculate : ").casefold() #user choices which calculation he/she wants to do.


if choice == "average speed":
    subprocess.call(["python", "Formulas/Average Speed.py"]) #Calls Average Speed Formula
if choice == "acceleration":
    subprocess.call(["python", "Formulas/Acceleration.py"]) #Calls Acceleration Formula
 if choice == "density":
    subprocess.call(["python", "Formulas/Density.py"]) #Calls Density Formula
if choice == "force":
    subprocess.call(["python", "Formulas/Newton's Second Law.py"]) #Calls Weight Formula
if choice == "power":
    subprocess.call(["python", "Formulas/Power.py"]) #Calls Power Formula
if choice == "weight":
    subprocess.call(["python", "Formulas/Weight.py"]) #Calls Weight Formula
if choice == "pressure":
    subprocess.call(["python", "Formulas/Pressure.py"]) #Calls Pressure Formula
if choice == "kinetic energy":
    subprocess.call(["python", "Formulas/Kinetic Energy.py"]) #Calls Kinetic Energy Formula
if choice == "ohm's law":
    subprocess.call(["python", "Formulas/Ohm's Law.py"]) #Calls Ohm's Law Formula
if choice == "frequency":
    subprocess.call(["python", "Formulas/Frequency.py"]) #Calls Frequency Formula
