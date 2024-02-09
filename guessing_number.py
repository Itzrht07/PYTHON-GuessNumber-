import random
n=40 #final value

to_be_guessed= int(n*random.random()) #it always give random ressults

guess=1 #initia value

while guess!= to_be_guessed: #agr to be guessed or guess equal nhe hue to loop start hoga
    guess=int(input("new number="))
    if guess>0: #0 se bada hoga hamesha
        if guess>to_be_guessed:
            print("bada hai bhadwe") 
        elif guess<to_be_guessed:
            print("tere jitna chota hai")
    else:
        print("bhakk choomu") #0  se chota hua toh
        break
else:
    print("me jeet gya")