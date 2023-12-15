input = "day2"

presents = open(input, "r").read().splitlines()

count = 0
for present in presents:
    w,l,h = list(map(int, present.split("x")))
    side1 = l * w 
    side2 = w * h 
    side3 = h * l
    superMin = min(side1, side2, side3)
    count += 2 * side1 + 2 * side2 + 2 * side3 + superMin

print(count)    

count = 0

for present in presents:
    dims = list(map(int, present.split("x")))
    maxDim = max(*dims)
    dims.remove(maxDim)
    wrap = 2 * dims[0] + 2 * dims[1]
    bow = maxDim*dims[0]*dims[1]
    
    count += wrap + bow

print(count)    
