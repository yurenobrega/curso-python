students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))

age = lambda ages:ages[2]
# students.sort(key=age)
sorted_students = sorted(students, key=age)

for i in sorted_students:
    print(i)