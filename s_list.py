from typing import Union, Optional
class SList:
    """
    A class that implements a sorted list ADT capable of storing and performing operations
    on a list of integers in ascending order.

    Attributes:
        _head (SListNode): The head node of the list.
        _size (int): The number of elements in the list.
    """
    class SListNode:
        """
        An inner class representing a node in the SList.

        Attributes:
            data: The value stored in the node.
            next (SListNode): The next node in the list.
        """
        def __init__ (self, data = None):
            """
            Initializes a new instance of the SListNode class.

            Parameters:
                data: The value to store in the node.
            """
            self.data = value
            self.next = None

    def __init__ (self):
        """
        Initializes a new instance of the SList class.
        """
        self._head = None
        self._size = 0

    # Insert a new value in the list. Maintain nondecreasing ordering of elements
    def insert(self, data: int):
        """
        Inserts an item into the sorted list while maintaining ascending order.

        Parameters:
            data (int): The data to be inserted.
        """

        new = SListNode(data)

        if self.head == None:
            new.next = self.head
            self.head = new
            return
        
        curr = self.head

        # if there is a next node, check to see if its value is less than new_node.data
        while curr.next != None:
            if curr.next.data <= new.data:
                curr = curr.next
            else:
                break

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
        pass

    # Remove the first occurance of value.
    def remove(self, value):
        """
        Removes the first occurrence of the specified value from the list.

        Parameters:
            value (int): The value to remove from the list.

        Returns:
            bool: True if the value was found and removed; False otherwise.
        """
        pass

    # Remove all instances of value
    def remove_all(self, value):
        """
        Removes all instances of the specified value from the list.

        Parameters:
            value (int): The value to remove from the list.
        """
        pass


    # Convert the list to a string and return it
    def __str__(self) -> str:
        """
        Returns a string representation of the list.

        Returns:
            str: The string representation of the list, with values separated by commas.
        """
        pass

    # Return an iterator for the list
    def __iter__(self) -> 'Iterator[SListNode]':
        """
        Returns an iterator for the list. Recall from the class what could be returned from this method.

        Returns:
            Iterator[SListNode]: An iterator that allows traversal of the list.
        """
        pass

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
        pass

    def __len__(self) -> int:
        """
        Returns the number of items in the list.

        Returns:
            int: The number of items in the list.
        """
        pass
