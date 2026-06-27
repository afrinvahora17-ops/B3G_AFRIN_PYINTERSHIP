e={"Riya":5000,"Afrin":6000,"John":7000,"vahora":8000}
sorted_e=sorted(e.items(),key=lambda X:X[1],reverse=True)
for name,salary in sorted_e[:3]:
    print(name,salary)