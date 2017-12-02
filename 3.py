def print_timesTable() :
     for i in range(2,10):
         print("===",i,"===")
         for j in range(1,10):
             print(i,"x",j,"=",i*j)
print_timesTable()

#https://wikidocs.net/24

num = [1,2,3,4]
num.append(5)
print(num)

num.insert(0,0)
print(num)
num.extend([6,7])

print(num)

color = ['red','blue','yello','red']
print(color.index('red'))
print(color.index('red',1))
print(color.count('red'))
print(color.pop())
color.sort()
print(color)

color.remove('blue')
print(color)