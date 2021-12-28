import random 

again=True

while again:
    print("Your answer issss: ")
    print(random.choice(['code','study']))
    anotherroll=input("Wanna go again? ")
    if anotherroll.lower()=='yes'or anotherroll.lower()=='y':
        continue
    elif anotherroll.lower() != "y" or anotherroll.lower()!="yes":
        break 
     #the lines above can be replaced with   
    # elif anotherroll.lower() == "n" or anotherroll.lower()=="no":
      # break 
#goodbye world :)
