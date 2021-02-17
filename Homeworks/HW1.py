import random
prime=[]
for number in range(2,100):
    bolen = 0
    for i in range(2,number):
        if(number%i==0):
            bolen+=1
    if(bolen==0):
        prime.append(number)
#print(prime)
x=random.sample(prime,9)
#print(x)
row1=(x[0:3])
row2=(x[3:6])
row3=(x[6:9])
matrix=[]
matrix.append(row1)  
matrix.append(row2) 
matrix.append(row3)
print(matrix)
