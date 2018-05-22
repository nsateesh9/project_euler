
ip = int(input("Enter the number:"))
sumof3 = 0
sumof5 = 0
if ip<=0 :
    print("Enter a positive integer")
else:
    ip = ip-1
# while ip!=0:
    for i in range (0,ip):
        if ip%3 == 0:
            sumof3 += ip
            ip -= 1
        elif ip%5 == 0:
            sumof5 += ip
            ip -= 1
        else:
            ip -= 1
    print ("sum of multiples of 3 or 5 :" , sumof3+sumof5)



