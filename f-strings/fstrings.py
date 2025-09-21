person = "dave"
coins = 3 

print("\n" +person + "has " +str(coins) + " coins left.")
massage ="\n%s has %s coins left." % (person, coins)

#format method
message ="\n{} has {} coins left." .format(person, coins)
#with the index method you can say which message is a priority
message ="\n{1} has {0} coins left." .format(coins, person) 



message ="\n{person} has {coins} coins left." .format(coins = coins, person = person) 

#with data structure

player = {
    "person" : "dia",
    "coins" : 3
}

message ="\n{person} has {coins} coins left." .format(**player) 

#with the letter f
message = f"\n{person} has {coins} left"

message = f"\n{person} has {2 * 5} left"
#you can add method with f strings 
message = f"\n{person.lower()} has {coins} left"


message = f"\n{player['person']} has {coins} left"

## you can pass formating options
num = 10
# .2f stand for 2 decimal places floating place of the number
print(f"\n2.25 times {num} is {2.25 * num:.2f}")
#you can use a loop
for num in range (1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}")
