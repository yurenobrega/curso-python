student = ("Yure", 22, "male")

print(student.count("Yure"))
print(student.index("male"))

for x in student:
    print(x)
    
if "Yure" in student:
    print("Yure is here!")