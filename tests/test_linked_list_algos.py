from linked_list import LinkedList
from unittest import TestCase, main
from linked_list_algos import nth_element_from_end

class TestLinkedList(TestCase):
    def setUp(self) -> None:
        print("SetUp")
        self.ll = LinkedList([5, 6, 2, 4, 8, 1, 9])

    def tearDown(self) -> None:
        print("tearDown")
        del self.ll

    def test_nth_element_from_end(self):
        self.assertTrue(nth_element_from_end(self.ll, 3) == 8)
        self.assertTrue(nth_element_from_end(self.ll, 7) == 4)
        self.assertFalse(nth_element_from_end(self.ll, -2))