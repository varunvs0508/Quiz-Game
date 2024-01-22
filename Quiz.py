print("Welcome to python quiz game")
score=0
print("Who taught Arjuna the 'Brahmastra'?")
print("1. Sri Krishna\n2. Dronacharya\n3. Mahadev\n4. Sage vyasyaa")
ans=int(input("Your choice-enter option number : "))
if(ans==2):
    print("Correct")
    score+=1
else:
    print("Wrong")
print("Volcanic eruption do not occur in the ")
print("1. Baltic Sea\n2. Black Sea\n3. Carribean Sea\n4. Caspian Sea")
ans=int(input("Your choice-enter option number : "))
if(ans==1):
    print("Correct")
    score+=1
else:
    print("Wrong")
print("D.D.T. was invented by")
print("1. Mosley\n2. Rudolf\n3. Karl Benz\n4. Daltona")
ans=int(input("Your choice-enter option number : "))
if(ans==1):
    print("Correct")
    score+=1
else:
    print("Wrong")
print("Your score is : ",score," out of 3")