from linked_list import LinkedList
from unittest import TestCase, main


class TestLinkedList(TestCase):
    def setUp(self) -> None:
        print("SetUp")
        self.ll = LinkedList([5, 6, 2, 4, 8, 1, 9])

    def tearDown(self) -> None:
        print("tearDown")
        del self.ll

    # @unittest.skip("Just for Now!")
    def test_pop(self):
        print("test_pop")
        self.assertTrue(self.ll.pop() == 9)
        self.assertTrue(self.ll.tail.data == 1)
        print(self.ll)

    def test_insert(self):
        print("test_insert")
        self.ll.insert(99, 0)
        self.assertTrue(self.ll.head.data == 99)
        self.ll.insert(99, self.ll.count + 10)
        self.assertTrue(self.ll.tail.data == 99)
        print(self.ll)



if __name__ == '__main__':
    main()
