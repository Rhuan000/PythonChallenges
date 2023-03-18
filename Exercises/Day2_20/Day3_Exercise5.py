# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string = name1 + ' ' + name2
lower_string = combined_string.lower()
l = lower_string.count('l')
o = lower_string.count('o')
v = lower_string.count('v')
e = lower_string.count('e')
t = lower_string.count('t')
r = lower_string.count('r')
u = lower_string.count('u')
true = t + r + u + e
love = l + o + v + e
true_love = str(true) + str(love)
true_love = int(true_love)
if true_love <10 or true_love > 90:
    print(f'Your score is {true_love} you go together like coke and mentos.')
elif true_love >= 40 and true_love <=50:
    print(f'Your score is {true_love}, you are alright together.')
else:
    print(f'your score is {true_love}')