import pandas as pd




def cal(amt,a):
    am=amt/a
    return am



def prebill(name):
    g=open(name,'r')



    return float(g.readline())






def bill(name,total):
    inputt=prebill(name)
    f=open(name,'w')
    a=inputt+total
    f.write(str(a))
    f.close()

def substract(name,amt):
    inputt=prebill(name)
    f=open(name,'w')
    a=inputt-amt
    f.write(str(a))

def addition(name,amt):
    inputt=prebill(name)
    f=open(name,'w')
    a=inputt+amt
    f.write(str(a))
















def calculation(group_name):
    names=[]
    with open(group_name,'r') as f:
        for line in f:
            names.append(line.rstrip("\n"))
    print("People in "+group_name+" are")
    index=[]
    values=[]
    column=['Names']
    for idx,val in enumerate(names):
        index.append(idx+1)
        values.append(val)
    print(pd.DataFrame(values,index,column))
    num=int(input("Would you like to add expenses or settle the expenses?\n1.Add Expenses\n2.Settle Expenses\n"))
    if num==1:

        decide=int(input("1.To split equally \n2.To add individually\n"))
        if decide==1:
            amt=float(input("Hey howmuch did you pay?\n"))
            print(pd.DataFrame(values,index,column))
            index=[]
            select2=[]
            print("Select the people from the list\n and enter 0 after your done selecting from the list\n")
            for i in range(0,100):
                select=int(input())
                if select==0:
                    break
                index.append(select-1)
            total=cal(amt,len(index))
            print(total)

            for i in range(0,len(index)):
                bill(names[index[i]],total)
            data_store=[]
            for i in names:
                f=open(i,'r')
                a=float(f.readline())
                data_store.append('%.2f'%a)

            column=['Amount']
            print("The amount to be paid by your mates\n")
            print(pd.DataFrame(data_store,names,column))


        elif decide==2:
            print(pd.DataFrame(values,index,column))
            print("Select the people from the list\n and enter 0 after your done selecting from the list\n")
            index=[]
            for i in range(0,100):
                select=int(input())
                if select==0:
                    break
                index.append(select-1)
            for i in range(0,len(index)):
                print("How much did you pay for "+names[index[i]])
                amt=float(input())
                addition(names[index[i]],amt)
            data_store=[]
            for i in names:
                f=open(i,'r')
                a=float(f.readline())
                data_store.append('%.2f'%a)
            column=['Amount']
            print("The amount to be paid by your mates\n")
            print(pd.DataFrame(data_store,names,))

    elif num == 2:
        print(pd.DataFrame(values,index,column))
        print("Select the people from the list\n and enter 0 after your done selecting from the list\n")
        index=[]
        for i in range(0,100):
            select=int(input())
            if select==0:
                break
            index.append(select-1)
        for i in range(0,len(index)):
            print("How much did "+names[index[i]]+" pay?\n")
            amt=float(input())
            substract(names[index[i]],amt)
        data_store=[]
        for i in names:
            f=open(i,'r')
            a=float(f.readline())
            data_store.append('%.2f'%a)
        column=['Amount']
        print("The amount to be paid by your mates\n")
        print(pd.DataFrame(data_store,names,column))








