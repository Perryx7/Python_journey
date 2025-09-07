#Dictionnaries
band = {
  "vocals" : "plant",
  "giutar" : "page"
 }


band2 = dict(vocals = "plant", guitar = "page")

#acces itemps

print(band["vocals"])# output = plant
print(band.get("guitar"))#output  = page

#list al keys
print(band.keys())

#list all values
print(band.values())

#verify a key exist
print ("guitar" in band)
print ("triangle" in band)

#change values
band["vocals"] = ["coverdale"]
band["drums"] = "bonhman"

#add a new key value
band.update({"bass" : "jpj"})

print(band)

#remove items
print(band.pop('bass'))
print(band.popitem()) #return a tuple
print(band)


#delete a values
band["drums"] = "bonham"
del band["drums"]
print(band)


band2.clear()
print(band2)

del band2


#copy dictionaries

# band2 =  band #create a reference

band2 = band.copy()
band2["drums"] = "dave"
print("goog copy")
print(band)
print(band2)

#with  the constructor function
band3 = dict(band)
print("good copy")
print(band3)

#nested dicTionnaries 

member1  = {
    "name" : "plant",
    "instrument" : "vocals" 

}


member2  = {
    "name" : "page",
    "instrument" : "guitar" 

}


group  = {
    "member1" : member1,
    "member2" : member2 

}

print(group)
print(group["member1"]["name"])

#sets

#create a set

nums = {1,2,3,4}

nums2 = set((1,2,3,4))
#add a mew element to a list

nums.add(8)
print(nums)

#merge two sets to create a new set

one = [123]
two = [567]

mynewset = one.union(two)
print(mynewset)

