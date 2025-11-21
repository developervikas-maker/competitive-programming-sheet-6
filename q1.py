
T = int(input())  

for i in range(T):
    S = input() 
    vowels = 0
    consonants = 0

    for ch in S:
        if ch.isalpha():  
            if ch.lower() in 'aeiou':  
                vowels += 1
            else:
                consonants += 1

    print(vowels, consonants)
