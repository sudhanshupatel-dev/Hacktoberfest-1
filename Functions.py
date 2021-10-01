details={}

def studentinfo(details):
    n=int(input("Enter no of keys and values pair: "))
    for i in range(n):
        k=input("Enter key: ")
        print("1. If value is int")
        print("2. If value is string")
        ch=int(input("Enter your choice: "))
        if ch==1:
            v=int(input("Enter value: "))
        else:
            v=input("Enter value")
        details[k]=v
    print(details)


def display(details):
    for i in details:
        print(i, ": ",details[i])

def menu():
    print("1. Student Profile Creation")
    print("2. Display Details")

    ch=int(input("Enter your choice: "))
    if ch==1:
        studentinfo(details)
    elif ch==2:
        display(details)
    else:
        exit()
while True:
    menu()

