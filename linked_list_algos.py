from linked_list import LinkedList

sll = LinkedList([5, 6, 2, 4, 8, 1, 9])


def nth_element_from_end(ll, pos):
    if ll.count and 1 <= pos <= ll.count:

        p1 = sll.head
        p2 = sll.head

        i = 0
        while i < pos:
            p2 = p2.next
            i += 1

        while p2:
            p1 = p1.next
            p2 = p2.next.next

        print(f"{pos} element is {p1.data}")
        return p1.data
    else:
        print("Ivalid pos or No elements")

def find_mid(ll):
    p1 = sll.head
    p2 = sll.head

    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next

    print(f"Middle element is {p1.data}")


find_mid(sll)

def is_looped(ll):
    ...


def loop_start(ll):
    ...


def common_thread(ll):
    ...

