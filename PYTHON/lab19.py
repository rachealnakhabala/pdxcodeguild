q = int(input("How many cards do you have? : "))
# user_cards = user_cards

for i in range(q):
    if i < q: #i < q:
        # q = int(input("How many cards do you have : "))
        user_cards = input("What card do you have? : ")
        i += 1
        continue
    else: 
        print("Please try again")


c2 = 2
c3 = 3
c4 = 4
c5 = 5
c6 = 6
c7 = 7
c8 = 8
c9 = 9
c10 = 10
J = 10
Q = 10
K = 10
A = 1


user_cards = 0
total = 0
# final = total
max_total = 21

if user_cards == "J":
    total += 10
elif user_cards == "Q":
    total += 10
elif user_cards == "K":
    total += 10
elif user_cards == "A" and total > 10:
    total += 1
elif user_cards ==  "A" and total < 10:
    total += 11
elif user_cards == c2:
    total += c2
elif user_cards == c3:
    total += c3
elif user_cards == c4:
    total += c4
elif user_cards == c5:
    total += c5
elif user_cards == c6:
    total += c6
elif user_cards == c7:
    total += c7
elif user_cards == c8:
    total += c8
elif user_cards == c9:
    total += c9
elif user_cards == c10:
    total += c10

# c2 = 2
# c3 = 3
# c4 = 4
# c5 = 5
# c6 = 6
# c7 = 7
# c8 =8
# c9 = 9
# c10 = 10
# J = 10
# Q = 10
# K = 10
# A = 1

# for i in range(q):
#     if i < q: #i < q:
#         total = input("What card do you have? : ")
#         i += 1
#         continue
#     else: 
#         print("Please try again")
# q2 = input("What's your second card do you have? : ")
# q3 = input("What's your third card do you have? : ")
# print(sum(total))
# def A_value():
#     if final <= 10:
#         A = 1
#     else: 
#         A = 10
# A_value()

def myfunction():
    if total < 17:
        print("HIT")
    elif total >= 17 and total < max_total:
        print("Stay")
    elif total == max_total:
        print("BLACKJACK!!!!!!!!")
    elif total > max_total:
        print("Already bussssssteddd")
myfunction()
