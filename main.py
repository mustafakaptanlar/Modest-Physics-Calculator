formulas = {
    'average speed': 'Average Speed.py',
    'acceleration': 'Acceleration.py',
    'density': 'Density.py',
    'force': "Newton's Second Law.py",
    'power': 'Power.py',
    'weight': 'Weight.py',
    'pressure': 'Pressure.py',
    'kinetic energy': 'Kinetic Energy.py',
    "ohm's law": "Ohm's Law.py",
    'frequency': 'Frequency.py'
}

while True:
    choice = input("What you want to calculate, or enter 'exit' to quit: ").casefold()
    if choice == 'exit':
        break
    try:
        exec(open(f"Formulas/{formulas[choice]}").read())
    except KeyError:
        print("Invalid choice. Please select a valid formula.")
