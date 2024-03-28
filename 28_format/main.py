animal = "cow"
item = "moon"

print("The {1} jumped over the {0}".format(animal, item))

print(f"The {animal} jumped over the {item}")

print("The {animal} jumped over the {item}".format(animal="sheep", item="fence"))
 
text = "The {} jumped over the {}"

print(text.format(animal, item))