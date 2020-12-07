f= open("test.txt","w+")
print("want to change delay\n1-->Yes 2-->No")
change=int(input())
if(change==1):
    print("wiredelay")
    wiredelay=input()
    print("Gatedelay")
    gatedelay=input()
else:
    wiredelay = "1"
    gatedelay = "1"
while(1):
    print("1-->inpt 2-->from 3-->gate 4-->exit")
    choice=int(input())
    if (choice==1):
        print("input adress")
        inpad1=input()
        inpad=inpad1.split(" ")
        for i in range(len(inpad)):
            a = (inpad[i], " ", inpad[i], "gat inpt 1 0 ", wiredelay,"\n")
            f.writelines(a)
    if(choice==2):
        print("from address")
        frad=input()
        frsp=frad.split(" ")
        print("enter input address")
        iad=input()
        for i in range(len(frsp)):
            if (frad == " "):
                continue
            a = (frsp[i], " ", frsp[i], "fan from ",iad,"gat ", wiredelay,"\n")
            f.writelines(a)
    if(choice==3):
        print("number of gate")
        nuga=int(input())
        for i in range(nuga):
            print("gate address")
            gaad=input()
            print("gate")
            ga=input()
            a = (gaad, " ", gaad, "gat ", ga, " 1 2 ", gatedelay," ", wiredelay, "\n")
            f.writelines(a)
            print("input address")
            gainad=input()
            b=(gainad,"\n")
            f.writelines(b)
    if(choice==4):
        break


f.close()
f= open("final.txt","r")
a=f.read()
print(a)