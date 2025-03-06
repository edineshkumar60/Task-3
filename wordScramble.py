import random
#Task 3
#2.Word Scramble --->
words = ["python", "javascript", "java", "automation", "pytest", "guvi", "selenium"]

selectrandomword = random.choice(words)

wordtostring = list(selectrandomword)
#the word selected will be shared as single string or char
random.shuffle(wordtostring)
#the word is jumbled
stringtoword = "".join(wordtostring)  #again the jumbled single string is made to
print("Play Scramble,Unscramble game & The word is - "+stringtoword )

while True :

    guessword = input("Enter your Guess : ")
    if (guessword.lower() != selectrandomword.lower()) :
        print("Try again until you guess")
    else :
        print("Congrats, You found the word")
        break

