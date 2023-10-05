import random as r
flag=1
print("WELCOME TO THE GAME")
print("\nPRESS 1 TO PLAY")
print("PRESS 2 TO EXIT\n=>",end="")
flag=int(input())
def game(l):
    b=r.randint(0,4)
    x=l[b]
    count=5
    a=[]
    s=[]
    for i in x:
        if i not in a:
            a.append(i)
    while(count>0 and sorted(a)!=sorted(s)):
        for i in range (len(x)):
            if x[i] in s:
                print(x[i],end=" ")
            else:
                print("_",end=" ")
        print("\n")
        print("GUESSES LEFT",count)
        z=input("guess the letter:")
        print("\n**********************************\n")
        if z in a:
            if z in s:
                print("YOU HAVE ALREADY GUESSED THIS WORD \n")
            else:
                s.append(z)
        else:
            count-=1
    else:
        if(count==0):
            print("\n***SORRY BUT YOU LOST***")
            print("\nTHE WORD WAS:-\n")
            for i in range (len(x)):
                print(x[i],end=" ")
        else:
            for i in range (len(x)):
                print(x[i],end=" ")
            print("\n\n!!!HURRRAY YOU WON!!!")
            print("\n******************\n")
    print("PRESS 1 TO PLAY AGAIN")
    print("PRESS 2 TO EXIT\n=>",end="")
    return int(input())



while(flag==1):
        print("SELECT THE CATEGORY YOU WANT TO GUESS\n\n***********************************************\n")
        print("1.PRESS 1 TO GUESS MOVIES")
        print("2.PRESS 2 TO GUESS VEGETABLES")
        print("3.PRESS 3 TO GUESS FRUITS")
        print("4.PRESS 4 TO GUESS MUSICAL INSTRUMENTS\n=>",end="")
        g=int(input())
        if g==1:
            l=["bahubali","oppenheimer","jawan","pushpa","avengers"]
            flag=game(l)
        elif g==2:
            l=["broccoli","pumpkin","reddish","cabbage","bittergaurd"]
            flag=game(l)
        elif g==3:
            l=["orange","apple","banana","watermelon","muskmelon"]
            flag=game(l)
        elif g==4:
            l=["harmonica","voilin","piano","trumpet","flute"]
            flag=game(l)
else:
    print("*************************")
    print("\nTHANKS FOR PLAYING")
        
        
    
    
    

        
        
        
    
    
