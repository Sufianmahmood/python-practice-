temperature = int(input("Temperature: "))
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's nom day")
else : 
    print("It's a cold day")

age = int(input("Age: "))
message = "eligible" if age >= 18 else "not eligible"
print(message)
