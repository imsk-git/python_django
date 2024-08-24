# for i in range(10):
#     print(i)


#WAP to find 20 to 50 odd and even number

for i in range(20,51):
    if i % 2 == 0:
        print(f"{i} is even number.")
    else:
        print(f"{i} is odd number.")



#WAP using while loop print 50 to 5

a = 50
while a>=5 and a<=50:
    print(a)
    a -= 1



#WAP is string or number










#WAP for break

for i in range(5000000000000000000000000000):
    if i == 60:
        break
    print(i) # this breaks after 59

#WAP for continue

for i in range(50):
    if i == 10:
        continue
    print(i) # this don't take 10


for i in range(20):
    if i % 2 != 0:
        print(i)
    else:
        pass