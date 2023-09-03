print("Welcome to Deutsch Pizza")
S = 15
M = 20
L = 25
pepperoni_small_pizza = 2
pepperoni_medium_or_large_pizza = 3
pizza = str(input("Please choose pizza size: "))
pepperoni = str(input("Do you want add pepperoni Y/n: "))
if pepperoni == "Y" and pizza == "S":
    print(f"The bill is: ${pepperoni_small_pizza + S}")
elif pepperoni == "Y" and pizza == "M":
    print(f"The bill is: ${M + pepperoni_medium_or_large_pizza}")
elif pepperoni == "Y" and pizza == "L":
    print(f"The bill is: ${M + pepperoni_medium_or_large_pizza}")
if pizza == "S" and pepperoni == "n":
    print("The bill is: $", S)
elif pizza == "M" and pepperoni == "n":
    print("The bill is: $", M)
elif pizza == "L" and pepperoni == "n":
    print("The bill is: $", L)



