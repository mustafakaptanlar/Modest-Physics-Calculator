import subprocess #import library

choice = input("What you want to calculate : ") #user choices which calculation he/she wants to do.

if choice == "acceleration":
    subprocess.call(["python", "Formulas/Acceleration.py"]) #Calls Acceleration Formula
if choice == "density":
    subprocess.call(["python", "Formulas/Density.py"]) #Calls Density Formula
if choice == "average speed":
    subprocess.call(["python", "Formulas/Average Speed.py"]) #Calls Average Speed Formula
if choice == "force":
    subprocess.call(["python", "Formulas/Newton's Second Law.py"]) #Calls Newton's Second Law Formula
if choice == "power":
    subprocess.call(["python", "Formulas/Power.py"]) #Calls Power Formula
if choice == "weight":
    subprocess.call(["python", "Formulas/Weight.py"]) #Calls Weight Formula
