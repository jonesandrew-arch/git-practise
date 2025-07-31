weight=float(input("Enter your weight: "))
pork=input("(L)bs or (K)g: ")
if pork=='L' or pork=='l':
    print(f'Weight in kilograms={weight* 0.45359237}')
elif pork=='K' or pork=='k':
    print(f'Weight in pounds: {weight// 0.45359237}')
else:
    print("enter the type of weight properly")