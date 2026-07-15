fruite = {"apple", "banana", "cherry", "papaya", "mango"}
fruite.add("orange")
fruite.add("kiwi")
fruite.add("grapes")
fruite.remove("apple")
fruite.discard("banana")
print("Total number of elements in fruite set is:",len(fruite))
print("checking whether the fruite set mango is exists or not:", "mango" in fruite)
city1 = {"delhi", "mumbai", "kolkata", "chennai", "bangalore"}
city2 = {"nanded", "pune", "nagpur", "mumbai", "kolkata"}
print("Union of city1 and city2 is:", city1.union(city2))
print("Intersection of city1 and city2 is:", city1.intersection(city2))
print("Difference of city1 and city2 is:", city1.difference(city2))
print("Symmetric difference of city1 and city2 is:", city1.symmetric_difference(city2))
print("checking whether city1 is subset of city2 or not:", city1.issubset(city2))
print("checking whether city1 is superset of city2 or not:", city1.issuperset(city2))
for i in city1:
    print(i)
for i in city2:
    print(i)
city1.duplicate = city1.copy()
print("Duplicate of city1 is:", city1.duplicate)