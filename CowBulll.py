import random
def sec_list():
    l=[0,1,2,3,4,5,6,7,8,9]
    list=random.sample(l,k=5)
    print(list)
    return list 
def check_guess():
    bull=[]
    cow=[]
    num=sec_list()
    i=0
    while i<=10:
        number=int(input("enter your number :   "))
        position=int(input("enter the position of your number :   "))

        if  number in num:
            index = num.index(number)
            if index== position: 
                if number not in bull:
                    bull.insert(index,number)
                    print("***bull*** the number and position both are right..great ""\n",bull) 
                else:
                    print("You Already Used This digit Try  any Different digit")
            else:
                cow.append(number)
                print("Cow, This number is in list but position is erong s please try again ...""\n",cow)
        elif  number not in num:
            print("You Guess is wrong")
        if bull==num:
            print("Congractulation you win the game ")
            break 
        i+=1
        print(i,"Turns are left")
    else:
        print("You used all chances ")   
    return bull 
def play_again():
    while True:
        again=int(input("If you Want to play again press yes1 no2 :   ") )
        if again==1:
            check_guess()
        else:
            print("thank you for enter in game ..have a nice day")
            break
play_again()


            



