import hashlib

input = "yzbqklnj"
# input = "abcdef"

count = 0
while True:
    test = input + str(count)
    if hashlib.md5(test.encode()).hexdigest().startswith("00000"):
        break;
    count +=1

print(count)


count = 0
while True:
    test = input + str(count)
    if hashlib.md5(test.encode()).hexdigest().startswith("000000"):
        break;
    count +=1

print(count)
