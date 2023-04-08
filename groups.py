import calc
class members:
    def __init__(self,names,amount):
        self.names=names
        self.amount=amount
        g=open(names,'w')
        g.write(str(amount))









def newgroup():

    group_name=input("Enter the name of the group\n")
    f=open(group_name,'w')
    f.close()
    num='r'
    num2='r'
    while num==num2:
        try:
            num=int(input("Enter howmany members in a group"))
        except:
            print("Enter integer values")
            break
        print("Enter their names")
        names=[]
        f=open(group_name,'a')
        for i in range(0,num):
            a=input(i+1)
            f.write(a+"\n")
            names.append(a)
            names[i]=members(names[i],0.00)
        f.close()


def group():

    a=2
    while a==2:
        group_name=input("What is your group name?\n")
        try:
            f=open(group_name,'r')
        except:
            print("The group does not exist")
            continue
        try:
            decision=int(input("Would you like to add a new member?\n Select the options\n1.Yes\n2.No\n"))
        except:
            print("Enter only the integer value")
            break
        if decision==1:
            num=int(input("Enter the number of members you would like to add in the group\n"))

            print("Enter their names")
            names=[]
            f=open(group_name,'a')
            for i in range(0,num):
                a=input(i+1)
                f.write(a+"\n")
                names.append(a)
                names[i]=members(names[i],0.00)
            f.close()
            calc.calculation(group_name)
            break
        elif decision==2:
            calc.calculation(group_name)
            break
        else:
            print("Invalid option choosen\n")
            break



