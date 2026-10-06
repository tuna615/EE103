x = float(input("What x to find the square root of? "))
guess = float(input("What guess to start with? "))

# Türevi f'(g) = 2*g olduğundan Newton formülü: nextguess = guess - (guess**2 - x) / (2 * guess)
nextguess = guess - ((guess ** 2) - x) / (2 * guess)

print("Current estimate square:", guess ** 2)
print("Next guess:", nextguess)