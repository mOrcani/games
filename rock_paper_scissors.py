import random
#=============================================================================================================
def randomgame():           


    rock="""
    _______
---'     ___)   
        (____)
        (_____)
        (____)
---'____(___)
        
    """
    paper="""
    _______
---'    ______)   
        _______)
        ________)
        _______)
---'__________)
        
    """

    scissors="""
    _______
---'     ___)____   
            ______)
         ___________)
        (____)
---'____(___)
        
    """
    
    print("""
        Welcome ya bro to my game <3 
        Do u want to know the rules? (yes or no)
        """)


    respond=input("").lower()
    if respond=="no":
        print("""
            ****** The Rules Of The Game ******
            0)u will choose and computer will choose 
            1)there is 3 only possibles u choose (rock,paper,scissors) 
            2)rock damage the scissors ==>rock will win
            3)scissors cut the paper   ==>scissors will win
            4)paper covers the rock    ==>paper will win
        
            """) 
    
        urchoice=input("now choose one of [rock,paper,scissors]").lower()

    else:
        urchoice=input("alright it's time to choose one of [rock,paper,scissors]").lower()

# if there is errors and the user did not follow the instuctions 

    if urchoice not in ["rock","paper","scissors"]:
        print("""Error ...ur choice should be one of [rock,paper,scissors]
                Now u have 2 only tries to choice right 
              """)
        # time to try
        i=2
        while i>0:
            urchoice=input("pls choose one of [rock,paper,scissors]").lower()
            if urchoice not in ["rock","paper","scissors"]:
                print(f"""Error ...ur choice should be one of [rock,paper,scissors]
                 Now u have {i-1} only tries to choice right 
              """)
                if i-1==0:
                    break
                
            else:
                if urchoice=="paper":
                    print(f"u choosed the [paper] \n{paper}")
                    break
                elif urchoice=="rock":
                    print(f"u choosed the [rock] \n{rock}")
                    break
                else: 
                    print(f"u choosed the [scissors] \n{scissors}")
                    break
    else:
        if urchoice=="paper":                
            print(f"u choosed the [paper] \n{paper}")
        elif urchoice=="rock":
            print(f"u choosed the [rock] \n{rock}")
        else: 
            print(f"u choosed the [scissors] \n{scissors}")
                        
    def possiblities():
#=============================================================================================================
# -----the computer choice-----
        
        computerchoice=random.choice(["rock","paper","scissors"])  
        if computerchoice=="paper":
            print(f"computer choosed the [paper] \n{paper}")
        elif computerchoice=="rock":
            print(f"computer choosed the [rock] \n{rock}")
        else: 
            print(f"computer choosed the [scissors] \n{scissors}")
            
#=============================================================================================================
#-----comparison-----            
#=============================================================================================================            
# -----if computer choosed paper-----
        if computerchoice=="paper" and urchoice=="rock":
            print("-----=computer won=-----")
        elif computerchoice=="paper" and urchoice=="scissors" :
            print("-----=you won=-----")
        elif computerchoice=="paper" and urchoice=="paper" :
            print("-----=draw=-----")  

#=============================================================================================================             
# -----if computer choosed rock-----
        elif computerchoice=="rock" and urchoice=="paper":
            print("-----=you won=-----")    
        elif computerchoice=="rock" and urchoice=="rock":
            print("-----=draw=-----")  
        elif computerchoice=="rock" and urchoice=="scissors":
            print("-----=computer won=-----")
            
#=============================================================================================================
# -----if computer choosed scissors-----
        elif computerchoice=="scissors" and urchoice=="paper":
            print("-----=computer won=-----")
        elif computerchoice=="scissors" and urchoice=="scissors":
            print("-----=draw=-----")
        elif computerchoice=="scissors" and urchoice=="rock":
            print("-----=you won=-----")     
    possiblities()
#=============================================================================================================
randomgame()            
           