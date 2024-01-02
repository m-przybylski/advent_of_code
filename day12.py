import json

input = "day12"

content = open(input).read()
content = json.loads(content)


def sumAllNumbers(obj):
    if isinstance(obj, int):
       return obj
    
    
    if isinstance(obj, dict):
        count = 0
        keys = dict.keys(obj)
        for key in keys:
            if isinstance(obj[key], int):
                count += obj[key]

            if isinstance(obj[key], list):
                for x in obj[key]:
                    count += sumAllNumbers(x)

            if isinstance(obj[key], dict):
                count += sumAllNumbers(obj[key])

        return count

    if isinstance(obj, list):
        count = 0
        for element in obj:
            if isinstance(element, int):
                count += element

            if isinstance(element, list):
                for x in element:
                    count += sumAllNumbers(x)

            if isinstance(element, dict):
                count += sumAllNumbers(element)

        return count
    
    return 0

def sumAllNonRedNumbers(obj):
    if isinstance(obj, int):
       return obj
    
    
    if isinstance(obj, dict):
        count = 0
        for value in dict.values(obj):
            if value == 'red':
                return 0
        for key in dict.keys(obj):
            if isinstance(obj[key], int):
                count += obj[key]

            if isinstance(obj[key], list):
                for x in obj[key]:
                    count += sumAllNonRedNumbers(x)

            if isinstance(obj[key], dict):
                count += sumAllNonRedNumbers(obj[key])

        return count

    if isinstance(obj, list):
        count = 0
        for element in obj:
            if isinstance(element, int):
                count += element

            if isinstance(element, list):
                for x in element:
                    count += sumAllNonRedNumbers(x)

            if isinstance(element, dict):
                count += sumAllNonRedNumbers(element)

        return count
    
    return 0

print(sumAllNumbers(content))
print(sumAllNonRedNumbers(content))
