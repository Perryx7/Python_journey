#list of users
users = ['Dave', 'Eve', 'Frank']

data = ['dia' , 25, 3.6, True]

emptylist = []

#check if a  value exist in a list
print('dia' in users)

#accessing a value in a list with a positing index
print(users[0])
print(users[-1])#last item in a list

#knmow a position of an existing value in a list

print(users.index('Eve'))

print(len(users))#know the length of a lists

#return the first value up to the position 1
print(users[0:2])

#add a value to alist
users.append('Grace')
print(users)
users.insert(0, 'Heidi')#add a value at a specific position
print(users)
users.extend(data)#add multiple values to a list
print(users)
users.remove('Frank')#remove a value from a list
print(users)
users.pop()#remove the last value in a list
print(users)
users.clear()#remove all values in a list
print(users)
#combine two list
users += ['jason' ,'kate']
print(users)
#sort a list in ascending order
users.sort()
print(users)
#sort a list in descending order
users.sort(reverse=True)
print(users)
#reverse the order of a list
users.reverse()
print(users)
#copy a list
newlist = users.copy()
print(newlist)
print(" ")

del users[0]#delete a value at a specific position
print(users)

# data.claer()#clear all values in a list

users[2:2] = ['leo', 'mike']#add multiple values at a specific position
print(users)

users[1:3] = ['nancy']#replace multiple values with a single value
print(users)

nums = [5, 3, 8, 6, 7, 2, 4, 1]

numscpy = nums.copy()#copy a list
numpdesc = nums.sort(reverse = True)
# mynums = list(nums)#another way to copy a list
# mycopy = nums[:]#another way to copy a list

#tuples 

mytuple = ('dia', 25, 3.6, True)

anothertuple = tuple(('eve', 30, 4.0, False))



