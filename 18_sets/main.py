utensils = {"fork", "spoon", "knife", "knife", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

for x in dinner_table:
    print(x)
    
