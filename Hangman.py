import random as r
l=["bahubali","oppenheimer","jawan","pushpa","avengers"]
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
        print("\nTHE CORRECT WORD WAS:-\n")
        for i in range (len(x)):
            print(x[i],end=" ")
    else:
        for i in range (len(x)):
            print(x[i],end=" ")
        print("\n\n!!!HURRRAY YOU WON!!!")
        
        
    
    
