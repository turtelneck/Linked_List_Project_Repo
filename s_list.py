from typing import Union, Optional
from course import Course

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
            data_obj: The data_obj stored in the node.
            next (SListNode): The next node in the list.
        """
        def __init__ (self, data_obj = None):
            """
            Initializes a new instance of the SListNode class.

            Parameters:
                data_obj: The data_obj to store in the node.
            """
            self.data_obj = data_obj
            self.next = None


    def __init__ (self):
        """
        Initializes a new instance of the SList class.
        """
        self._head = None
        self.size = 0


    # Insert a new data_obj in the list. Maintain nondecreasing ordering of elements
    def insert(self, data_obj):
        """
        Inserts an item into the sorted list while maintaining ascending order.

        Parameters:
            data_obj (int): The data_obj to be inserted.
        """
        new = self.SListNode(data_obj)

        if self._head is None:
            new.next = self._head
            self._head = new
            return

        curr = self._head

        while curr.next and curr.next.data_obj.number() <= new.data_obj.number():
            curr = curr.next

        new.next = curr.next
        curr.next = new

    
    # Search for a data_obj in the list, return it if found, None otherwise
    def find(self, num) -> Union['SListNode', None]:#'SListNode' | None:
        """
        Searches for the first node containing the specified data_obj.

        Parameters:
            data_obj (int): The data_obj to search for in the list.

        Returns:
            SListNode | None: The node containing the data_obj if found; None otherwise.
        """
        curr = self._head
        while curr:
            if curr.data_obj.number() == num:
                return curr.data_obj
            curr = curr.next
        return None


    # Remove the first occurance of data_obj.
    def remove(self, num):
        """
        Removes the first occurrence of the specified data_obj from the list.

        Parameters:
            num (int): The course number to remove from the list.

        Returns:
            bool: True if num was found and removed; False otherwise.
        """
        if self._head and self._head.data_obj.number() == num:
            self._head = self._head.next
            return True

        curr = self._head

        while curr and curr.next and curr.next.data_obj.number() != num:
            curr = curr.next

        if curr and curr.next:
            curr.next = curr.next.next
            return True

        return False


    # Remove all instances of data_obj
    def remove_all(self, num):
        """
        Removes all instances of the specified num from the list.

        Parameters:
            num (int): The num to remove from the list.
        """
        prev = None
        curr = self._head
        
        while curr:
            if curr.data_obj.number() == num:
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
            str: The string representation of the list, with data_objs separated by commas.
        """
        list_str = "["
        curr = self._head
        while curr:
            list_str += f'{curr.data_obj}, '
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
            int: The data_obj of the node at the specified index.
        """
        if index < 0 or index >= len(self):
            raise IndexError("Index out of bounds")

        curr = self._head
        for _ in range(index):
            curr = curr.next

        return curr.data_obj

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
