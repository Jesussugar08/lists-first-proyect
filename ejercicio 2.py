List_fruits = ['mango', 'apple', 'pineapple', 'carrot', 'kiwi']
print('=================================================================')
print('1.MANGO 2.Apple 3.Pineapple 4.Carrot 5.kiwi:')
print('type "salir" to exit the program :')
print('=================================================================')

# here we are going to start the bucle
while True:
    fruit = input('Select a number of the prefered fuit :')

    if fruit.lower() == "salir":
        break

    if fruit == "1":
        print(F"YOU WILL HAVE  {List_fruits[0]}")

    elif fruit == "2":
        print(f"YOU WILL  HAVE {List_fruits[1]}")

    elif fruit == "3":
        print(f"YOU WILL  HAVE {List_fruits[2]}")

    elif fruit == "4":
        print(f"YOU WILL  HAVE {List_fruits[3]}")

    elif fruit == "5":
        print(f"YOU WILL  HAVE {List_fruits[4]}")

    else:
        print('That option is not available')
