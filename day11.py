input = "hepxcrrq"

alphabet = "abcdefghijklmnopqrstuvwxyz"

min_index = 0
max_index = len(alphabet) - 1

def get_next_password(old_password: str) -> str:
    index_to_increment = len(old_password) - 1
    new_password = list(old_password)
    while True:
        letter_to_change = new_password[index_to_increment]
        new_index = alphabet.index(letter_to_change) + 1
        if (new_index > max_index):
            new_password[index_to_increment] = "a"
            index_to_increment -= 1
            if index_to_increment < 0:
                break
            continue
        else:
            new_password[index_to_increment] = alphabet[new_index]
            break

    return "".join(new_password)

def has_straight(password) -> bool:
    count = 0
    sequence = []
    for ch in password:
        index = alphabet.index(ch)
        if len(sequence) == 0:
            sequence.append(index)
            count += 1
        elif sequence[-1] == index - 1:
            sequence.append(index)
            count += 1
        else:
            sequence = [index]
            count = 1

        if count == 3:
            return True
        
    return False

def has_invalid_characters(password: str) -> bool:
    for ch in password:
        if ch == "i" or ch == "o" or ch == "l":
            return True
    
    return False

def has_pairs(password: str) -> bool:
    count = 0
    sequence = []
    for ch in password:
        index = alphabet.index(ch)
        if len(sequence) == 0:
            sequence.append(index)
        elif sequence[-1] == index:
            sequence = []
            count += 1
        else:
            sequence = [index]

        if count == 2:
            return True
        
    return False


def is_password_valid(password):
    return has_straight(password) and not has_invalid_characters(password) and has_pairs(password)

password = get_next_password("hepxcrrq")
while (not is_password_valid(password)):
    password = get_next_password(password)

print(password)

password = get_next_password(password)
while (not is_password_valid(password)):
    password = get_next_password(password)

print(password)