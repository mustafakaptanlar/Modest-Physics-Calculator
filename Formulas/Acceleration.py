print("Accelaration Formula")
print("a = (v-u) / t")
initial_velocity = float(input("Initial velocity : "))
final_velocity = float(input("Final velocity : "))
time = float(input("Time taken: "))
velocity_difference = final_velocity - initial_velocity
accelaration = velocity_difference / time
print("Accelaration : ",accelaration)
