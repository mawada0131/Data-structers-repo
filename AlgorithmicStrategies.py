
def count_vowels(str):
    vowels = set('a','i','u','e','o')
    countVowels = 0 
    for char in str:
        if char in vowels:
            countVowels +=1
    countConsonants = len(str) - countVowels
    return countVowels , countConsonants


def Median_char(str):
    sortedStr = sorted(str)
    if len(str)%2 ==0:
        return sortedStr[(len(str)//2)-1]
    return sortedStr[len(str)//2]

def Word_Score(str):
    max_score = 0
    best_word = ''
    words_list = str.split()
    for word in words_list:
        score = 0
        for char in word:
            score += ord(char)-ord('a')+1
        if score > max_score:
            max_score = score
            best_word = word
    return best_word

def Largest_of_3(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > a:
        if b > c:
            return b
        else:
            return c
    else:
        return a

    
print(Largest_of_3(3,3,3))