# Write your code below this line 👇
def prime_checker(number):
    many = 0
    for check in range(1,number):
        checking = number % check
        if checking == 0:
            many += 1
    if many >= 2:
        print(f"{number} it's not a prime number")
    else:
        print(f"{number} it's a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)