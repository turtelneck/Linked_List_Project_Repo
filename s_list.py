from typing import Union, Optional
class SList:
    """
    A class that implements a sorted list ADT capable of storing and performing operations
    on a list of integers in ascending order.

    Attributes:
        _head (SListNode): The _head node of the list.
        _size (int): The number of elements in the list.
    """
    class SListNode:
        """
        An inner class representing a node in the SList.

        Attributes:
            value: The value stored in the node.
            next (SListNode): The next node in the list.
        """
        def __init__ (self, value = None):
            """
            Initializes a new instance of the SListNode class.

            Parameters:
                value: The value to store in the node.
            """
            self.value = value
            self.next = None


    def __init__ (self):
        """
        Initializes a new instance of the SList class.
        """
        self._head = None
        self.size = 0


    # Insert a new value in the list. Maintain nondecreasing ordering of elements
    def insert(self, value: int):
        """
        Inserts an item into the sorted list while maintaining ascending order.

        Parameters:
            value (int): The value to be inserted.
        """
        new = self.SListNode(value)

        if self._head is None:
            new.next = self._head
            self._head = new
            return

        curr = self._head

        while curr.next and curr.next.value <= new.value:
            curr = curr.next

        new.next = curr.next
        curr.next = new

    
    # Search for a value in the list, return it if found, None otherwise
    def find(self, value: int) -> Union['SListNode', None]:#'SListNode' | None:
        """
        Searches for the first node containing the specified value.

        Parameters:
            value (int): The value to search for in the list.

        Returns:
            SListNode | None: The node containing the value if found; None otherwise.
        """
        curr = self._head
        while curr:
            if curr.value == value:
                return curr
            curr = curr.next
        return None


    # Remove the first occurance of value.
    def remove(self, value):
        """
        Removes the first occurrence of the specified value from the list.

        Parameters:
            value (int): The value to remove from the list.

        Returns:
            bool: True if the value was found and removed; False otherwise.
        """
        if self._head and self._head.value == value:
            self._head = self._head.next
            return True

        curr = self._head

        while curr and curr.next and curr.next.value != value:
            curr = curr.next

        if curr and curr.next:
            curr.next = curr.next.next
            return True

        return False


    # Remove all instances of value
    def remove_all(self, value):
        """
        Removes all instances of the specified value from the list.

        Parameters:
            value (int): The value to remove from the list.
        """
        prev = None
        curr = self._head

        while curr:
            if curr.value == value:
                if prev:
                    prev.next = curr.next
                else:
                    self._head = curr.next
            else:
                prev = curr
            curr = curr.next


    # Convert the list to a string and return it
    def __str__(self) -> str:
        """
        Returns a string representation of the list.

        Returns:
            str: The string representation of the list, with values separated by commas.
        """
        list_str = "["
        curr = self._head
        while curr:
            list_str += f'{curr.value}, '
            curr = curr.next
        return list_str[:-2] + "]"

    # Return an iterator for the list
    def __iter__(self) -> 'Iterator[SListNode]':
        """
        Returns an iterator for the list. Recall from the class what could be returned from this method.

        Returns:
            Iterator[SListNode]: An iterator that allows traversal of the list.
        """
        curr = self._head
        while curr:
            yield curr
            curr = curr.next

    # Return the item at the given index, or throw an exception if invalid index
    def __getitem__(self, index: int) -> int:
        """
        Returns the item at the specified index.

        Parameters:
            index (int): The index of the item to retrieve.

        Raises:
            IndexError: If the index is out of bounds.

        Returns:
            int: The value of the node at the specified index.
        """
        if index < 0 or index >= len(self):
            raise IndexError("Index out of bounds")

        curr = self._head
        for _ in range(index):
            curr = curr.next

        return curr.value

    def __len__(self) -> int:
        """
        Returns the number of items in the list.

        Returns:
            int: The number of items in the list.
        """
        count = 0
        curr = self._head
        while curr:
            count += 1
            curr = curr.next
        return count
