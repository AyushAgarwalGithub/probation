import random as r
flag=1
print("WELCOME TO THE GAME")
print("\nPRESS 1 TO PLAY")
print("PRESS 2 TO EXIT\n=>",end="")
flag=int(input())
def game(l):
    b=r.randint(0,len(l)-1)
    x=l[b]
    count=5
    dis_words_in_list=[]
    guessed_words=[]
    for i in x:
        if i not in dis_words_in_list:
            dis_words_in_list.append(i)
    while(count>0 and sorted(dis_words_in_list)!=sorted(guessed_words)):
        for i in range (len(x)):
            if x[i] in guessed_words:
                print(x[i],end=" ")
            else:
                print("_",end=" ")
        print("\n")
        print("GUESSES LEFT",count)
        z=input("guess the letter:")
        print("\n**********************************\n")
        if z in dis_words_in_list:
            if z in guessed_words:
                print("YOU HAVE ALREADY GUESSED THIS WORD \n")
            else:
                guessed_words.append(z)
        else:
            count-=1
    else:
        if(count==0):
            print("\n***SORRY BUT YOU LOST***")
            print("\nTHE WORD WAS:-\n")
            for i in range (len(x)):
                print(x[i],end=" ")
            print("\n******************\n")
    
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
        
        
    
    
    

        
        
        
    
    
