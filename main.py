from linked_list import LinkedList

if __name__ == '__main__':
    ll = LinkedList([5, 6, 2, 4,  8, 1, 9])
    # ll.insert(66, 3)
    print(ll.pop(6))
    print(ll.tail.data)
    print(ll)