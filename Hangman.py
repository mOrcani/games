
import random

computer_choice = random.choice(["dog", "cat", "love", "messi", "phone", "margotrobbie","scarlett","cristiano","snopdog","serry","nsoohy"])

def guess():
    sec_word = ["-" for _ in computer_choice]
    hearts = 6  # Number of chances
    guessed_letters = []  # my true guessed letters
    
    print(f"Now the word is: {''.join(sec_word)}")
    print("So let's play (: ! ... Guess a letter from a-z:")
    
    while hearts > 0:
        guessing = input("Enter a letter: ").lower()
        
        if len(guessing) != 1 or not guessing.isalpha():
            print("Please enter a single letter (a-z)!")
            continue
        
        if guessing in guessed_letters:
            print(f"You already guessed '{guessing}'! Try another letter.")
            continue
        
        guessed_letters.append(guessing)
        
        if guessing in computer_choice:
            for i in range(len(computer_choice)):
                if computer_choice[i] == guessing:
                    sec_word[i] = guessing
            print(f"Good guess! The word is now: {''.join(sec_word)}")
        else:
            hearts -= 1
            print(f"Sorry, '{guessing}' is not in the word. You have {hearts} hearts left.")
        
        if ''.join(sec_word) == computer_choice:
            print("You Won !!")
            break
    
    if hearts == 0:
        print(f"Sorry, you lost! The word was: {computer_choice}")

guess()       
           
        
        
                
            
            
        
        
        
    














































