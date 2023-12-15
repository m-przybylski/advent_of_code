input = "day5"

def hasDoubleLetter(word: str) -> bool:
    for idx, ch in enumerate(word):
        if idx == 0:
            continue
        if word[idx - 1] == word[idx]:
            return True
        
    return False

def hasThreeVowels(word: str) -> bool:
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for ch in word:
        if ch in vowels:
            count += 1
            if count == 3:
                return True
        
    return False

def hasProhibitedString(word: str) -> bool:
    prohibitedStrings = ['ab', 'cd', 'pq', 'xy']
    for prohibitedString in prohibitedStrings:
        if prohibitedString in word:
            return True

    return False
    

def hasPairs(word: str) -> bool:
    for i in range(len(word) - 1):
        two = word[i:i+2]
        left = word[:i]
        right = word[i+2:]
        if two in left or two in right:
            return True

    return False


def hasRepeatWithSpace(word: str) -> bool:
    for i in range(1, len(word) - 1):
        left = word[i - 1]
        right = word[i + 1]
        if left == right:
            return True

    return False

def partOne():
    count = 0
    words = open(input, "r").read().splitlines()
    for word in words:
        if hasDoubleLetter(word) and hasThreeVowels(word) and not hasProhibitedString(word):
            count += 1

    print(count)


def partTwo():
    count = 0
    words = open(input, "r").read().splitlines()
    for word in words:
        if hasPairs(word) and hasRepeatWithSpace(word):
            count += 1

    print(count)


# 236
partOne()
# 51
partTwo()