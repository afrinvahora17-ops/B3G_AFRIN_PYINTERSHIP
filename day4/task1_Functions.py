def bulid_invoice(cust_name,*args,**kwargs):
    total=sum(args)

    print("Customer Name:",cust_name)
    print("price:",total)

    print("Extra details:")
    for key, value in kwargs.items():
        print(key,":",value)

bulid_invoice("Afrin Vahora",10000,20000,40000,discount=20,tax=10)