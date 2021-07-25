veg={"tomato","potato","carot","carot","apple"}
frits={"apple","mango","banana"}
# print(veg & frits)
# veg.add("brinjal")
# veg.remove("potato")  #we can use discard or remove fnction
# print(veg)
print(veg.intersection(frits))
print(veg.union(frits))
print(veg.issubset(frits))
print(veg.difference(frits))