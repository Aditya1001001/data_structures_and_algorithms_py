import random

"""
A linked list is a linear collection of data elements,
whose order is not given by their physical placement in memory.
Instead, each element points to the next. It is a data structure
consisting of a collection of nodes that together represent a sequence.

An classic linked list in python my implementation:

List is:
  Head->|Node|->|Node|->|Node|->None



SOME IMPROVEMENTS:
  [ ] - We can change the method get to __getitem__ if you want,
         because is more pythonic
  [ ] - We can create __delitem__ to use like this : del singly_linked_list[1]

"""


class Node:
    def __init__(self, value, node=None):
        self.__value = value
        self.__next = node

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node

    def __str__(self):
        return f"Node: {self.value}"


class SinglyLinkedList:
    def __init__(self, head=None):
        self._head = head
        self.__len = 0

    def __iter__(self):
        """
          Best:
            Time Complexity O(1)

          Worst:
            Time Complexity O(N)
        """
        current_node = self._head
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def __len__(self):
        """
          Time Complexity O(1)
        """
        return self.__len

    def get(self, index):
        """
          Best Case:
            Time Complexity O(N)

          Worst Case:
            Time Complexity O(N^2)
        """
        current_index = 0
        current_node = self._head
        while current_node:
            if current_index == index:
                return current_node.value
            current_index += 1
            current_node = current_node.next

        raise IndexError("Index out off range")

    def remove(self, index=None):
        """
          Time Complexity O(n)
        """
        if self._head is None:
            return

        if index and index > self.__len:
            raise IndexError("List indext out of range")

        if index == self.__len - 1:
            self._head = self._head.next
            return

        raise NotImplementedError()

    def pop(self, index=None):
        """
          Time Complexity O(1)
        """

        if index and index > self.__len:
            raise IndexError("List indext out of range")

        popped_node = self._head
        self._head = self._head.next
        popped_node.next = None
        self.__len -= 1
        return popped_node.value

    def append(self, value, first=True, tail=False):
        if value is None:
            return None
        if first and not tail:
            self._append_first(value)
        if tail:
            self._append_tail(value)

    def _append_first(self, value):
        """
          Time Complexity O(1)
        """

        tmp = Node(value)
        tmp.next = self._head
        self._head = tmp
        self.__len += 1

    def _append_tail(self, value):
        """
          In the best case this code has the time complexity O(1)
          In the worst case the time complexity O(N)

          Before:
            N1->N2->N3->N4->None

          After:
            N1->N2->N3->N4->Node(value)->None
        """

        if self.__len == 0:
            self._append_first(value)

        else:
            node = Node(value)
            current_head_node = self._head

            while current_head_node.next is not None:
                current_head_node = current_head_node.next

            node.next = current_head_node.next
            current_head_node.next = node
            self.__len += 1

    def __setitem__(self, index, new_value):
        """
          Time Complexity O(N)

        """

        current_node = self._head
        if current_node is None:
            raise IndexError("The linked list is empty")
        for node_number in range(index):
            if current_node.next is None:
                raise IndexError("Index out of range")
            current_node = current_node.next
        current_node.value = new_value

    def get_node(self, index = -1):
        """
        Returns the node at the specified index of the SinglyLinkedList it's
        called on, returns the last node by default.
        """
        if index == -1:
            curr_node = self._head
            if curr_node is None or curr_node.next is None:
                return curr_node
            while curr_node.next != None:
                curr_node = curr_node.next
            return curr_node
        else:
            curr_index = 0
            curr_node = self._head
            while curr_node:
                if curr_index == index:
                    return curr_node
                curr_index += 1
                curr_node = curr_node.next

            raise IndexError("Index out off range")

    def sort(self, reverse=False, key="merge"):
        """
        Sorts the SinglyLinkedList object it's called on.

        Args:
            reverse: Flag to reverse the sorting order, is set to false by
            default.
            key: parameter for choosing the sorting algorithm.

        Returns:
            Sorted SinglyLinkedList object.
        """

        if self._head is None:
            raise IndexError("The linked list is empty")
        if self._head.next is None:
            return self
        if key == "merge":
            return self.merge_sort(reverse)
        elif key == "quick":
            return self.quick_sort(reverse)
        elif key == "heap":
            pass
        else:
            raise ValueError("Unknown sorting method specified")

    def merge_sort(self, reverse=False):
        """
        Sorts the SinglyLinkedList object using merge sort algorithm.

        Args:
            reverse: Flag to reverse the sorting order, is set to false by
            default.

        Returns:
            Sorted SinglyLinkedList object.

        Time Complexity: O(NlogN)
        """
        if self._head is None or self._head.next is None:
            return self

        leftHalf, rightHalf = self._split_list()

        leftHalf = leftHalf.merge_sort(reverse)
        rightHalf = rightHalf.merge_sort(reverse)

        return leftHalf._merge_lists(rightHalf, reverse)

    def _split_list(self):
        """
        Splits the SinglyLinkedList object into two halves.

        Returns:
            Tuple of two SinglyLinkedList objects that contain two
            halves of the original SinglyLinkedList object.
        """

        rightHalf = SinglyLinkedList()
        leftHalf = SinglyLinkedList()
        midPointer = self._head
        frontRunner = midPointer.next

        while frontRunner is not None:
            frontRunner = frontRunner.next

            if frontRunner is not None:
                frontRunner = frontRunner.next
                midPointer = midPointer.next

        rightHalf._head = midPointer.next
        midPointer.next = None
        leftHalf._head = self._head
        return leftHalf, rightHalf

    def _merge_lists(self, rightHalf, reverse=False):
        """
        Merges the nodes of two SinglyLinkedList objects in an
        ascending/descending order.

        Args:
            rightHalf: Second SinglyLinkedList object to be merged with the
            one function is called on.
            reverse: Flag to reverse the sorting order, is set to false by
            default.

        Returns:
            A merged sorted SinglyLinkedList object.
        """

        leftHalf = self._head
        merged_list = SinglyLinkedList()
        fake_head = Node(None)
        curr = fake_head
        rightHalf = rightHalf._head

        if reverse:
            while leftHalf and rightHalf:
                if leftHalf.value > rightHalf.value:
                    curr.next = leftHalf
                    leftHalf = leftHalf.next

                else:
                    curr.next = rightHalf
                    rightHalf = rightHalf.next

                curr = curr.next
        else:
            while leftHalf and rightHalf:
                if leftHalf.value < rightHalf.value:
                    curr.next = leftHalf
                    leftHalf = leftHalf.next

                else:
                    curr.next = rightHalf
                    rightHalf = rightHalf.next

                curr = curr.next

        if leftHalf is None:
            curr.next = rightHalf

        elif rightHalf is None:
            curr.next = leftHalf
        merged_list._head = fake_head.next

        return merged_list
    
    def quick_sort(self, reverse = False):
        if(self._head is None or self._head.next is None):               # if single node return
            return self

        pivot_index = random.randint(0, self.__len - 1)
        pivot = self.get_node(pivot_index)                                        
        leftHalf = SinglyLinkedList()
        rightHalf = SinglyLinkedList()

        curr = self._head
        ptr_left = leftHalf._head
        ptr_right = rightHalf._head

        while curr.next is not None:
            if curr.value < pivot.value:
                if ptr_left is None:
                    ptr_left = Node(curr.value)
                else:
                    ptr_left.next = Node(curr.value)
                    ptr_left = ptr_left.next
            elif  curr.value > pivot.value:
                if ptr_right is None:
                    ptr_right = Node(curr.value)
                else:
                    ptr_right.next = Node(curr.value)
                    ptr_right = ptr_right.next
            curr = curr.next
        
        ptr_left.next = None
        ptr_right.next = None
        sort_left = leftHalf.quick_sort(reverse)
        sort_right = rightHalf.quick_sort(reverse)

        if sort_left._head is not None:
            pivot.next = sort_right._head
            left_tail = sort_left.get_node()
            print(sort_left._head, left_tail)
            left_tail.next = pivot
            return sort_left
        else:
            pivot.next = sort_right._head
            sort_right._head = pivot
            return sort_right


__all__ = ["SinglyLinkedList"]