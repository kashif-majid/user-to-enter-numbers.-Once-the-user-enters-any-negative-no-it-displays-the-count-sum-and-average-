i=1
count=0
sum=0
while i==1:
    a = int(input("ENTER NUMBERS: "))
    if a>0:
        if a%2!=0:
            count+=1
            sum+=a
    else:
        print("COUNT OF ODD NUMBERS IS: {}".format(count))
        print("SUM OF ODD NUMBERS IS: {}".format(sum))
        print("AVERAGE OF ODD NUMBERS IS: ", sum/count)
        i = int(input("\nIF U WANT TO CONTINUE PRESS 1 ELSE PRESS ANY KEY: "))

