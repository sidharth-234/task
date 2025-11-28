def minion_game(string):
    vowels = "AEIOU"
    s = string.upper()          
    length = len(s)

    kevin_score = 0
    stuart_score = 0

    for i in range(length):
        if s[i] in vowels:
          
            kevin_score += length - i
        else:
        
            stuart_score += length - i


    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

word = input("Enter a word: ")
minion_game(word)
