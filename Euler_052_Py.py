#Ariel Tynan
#Euler Problem 052, Permuted Multiples, Solved in Python
#Started and solved 5 March 2022

#x is number of interest, m is multiplier
def num_Remove(x,m): #Removes valid integers from tempArr 0-9
    tempArr = [0,1,2,3,4,5,6,7,8,9]
    xtemp = [int(a) for a in str(m*x)]
    for j in xtemp:
        tempArr[j] = 0
    return tempArr

for i in range(100000,1000000,1):
    if num_Remove(i,2) == num_Remove(i,3) == num_Remove(i,4) == num_Remove(i,5) == num_Remove(i,6):
        print(i)


