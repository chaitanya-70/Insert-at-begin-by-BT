#Insert at begin DLL using backtraverse


class Node:
    def __init__(s,data):
        s.data=data
        s.prev=None
        s.next=None
class DLL:
    
    def __init__(s):
        s.head=None
    def iab(s,data):
        newnode=Node(data)
        newnode.next=s.head
        if s.head:
            s.head.prev=newnode
        s.head=newnode 
    def backtraverse(s):
        print("values for traversing backward....")
        temp=s.head
        if not temp:
            print("Empty list")
            return
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end='<-->')
            temp = temp.prev
        print("None")
    
    def display(s):
        temp=s.head
        print("Double Linked List:")
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
dll=DLL()
n=int(input("enter the no of elements to insert at begin:"))
for i in range(n):
    val=int(input(f"enter element {i+1}:"))
    dll.iab(val)
dll.display()
dll.backtraverse()






