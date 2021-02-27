def indiatous():
    return float(amount * 0.0137130)
def ustoindia():
    return float(amount * 72.9330)

a = input("Enter a from country:")
b = input("Enter a to country:")
amount = float(input("Enter the amount:"))

if a == 'India' and b == 'Usa':
    new = indiatous()
    print("The amount in usd is " + str(new))

elif a == 'Usa' and b == 'India':
    new = ustoindia()
    print("The amount in rupees is " + str(new))
