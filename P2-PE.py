i1 = 1
i2 = 1
i = 0
sum = 0
while i < 4000000:
    if (i % 2) == 0:
        sum = sum + i
    i = i1 + i2
    i2 = i1
    i1 = i
    
print(sum)