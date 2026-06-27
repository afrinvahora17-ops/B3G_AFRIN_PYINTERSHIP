student = [("riya",88),("aman",95),("sara" ,72)]

sorted_student = sorted(student, key=lambda x:x[1], reverse=True)

print(sorted_student)