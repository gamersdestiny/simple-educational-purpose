contacts = {}
Exit = False
name = ''
num = 0
def Addcontact():
    name = input('enter the name ')
    number = int(input('enter the number '))
    contacts[name] = number

def Deletecontact():
    dele = input('enter the name of the contact to be deleted\n ')
    contacts.pop(dele)

def Showcontacts():
    for Name,Number in contacts.items():
        print(Name, Number)

while Exit == False:
    print()
    choice = input('1.Add contact \n2.Delete contact \n3.Show all contact \n0.Exit\n').lower()
    if '1' in choice:
        Addcontact()
    elif '2' in choice:
        Deletecontact()
    elif '3' in choice:
        Showcontacts()
    elif '0' in choice:
        Exit = True