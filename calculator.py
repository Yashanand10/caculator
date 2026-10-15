numb=int(input("enter the 1st number "))
numb2=int(input("enter the 2nd number"))
operator=input("enter the operation to be perform")
if operator=="+":
   print(numb+numb2)
elif operator=="-":
    print(numb-numb2)
elif operator=="*":
    print(numb*numb2)
elif operator=="/":
    print(numb//numb2)
else:
    print ("right operator")

