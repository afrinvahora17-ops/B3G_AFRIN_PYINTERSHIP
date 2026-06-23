student = [("Riya", 88), ("Aman", 95), ("Sara", 72)]

sorted_students = sorted(student, key=lambda X: X[1], reverse=True)

print(sorted_students)