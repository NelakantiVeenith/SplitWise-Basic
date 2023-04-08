import groups

print("Hi Veenith")

i = 0

while i == 0:
    a = 'r'
    decision = 'r'
    while decision == a:
        p = open('group_num', 'a')
        p.close()
        p = open('group_num', 'r')
        o = p.readline()
        try:
            decision = int(input("Would you like to create a New Group?\n Select the options\n1.Yes\n2.No\n"))

        except:
            print("\nWe only accept integer value")
            break

        if decision == 1:

            p = open('group_num', 'w')
            p.write("1")
            p.close()

            groups.newgroup()
        elif decision == 2 and o == '1':
            groups.group()
        else:
            print("\nInvaild or there are no groups created yet\n")
            break
