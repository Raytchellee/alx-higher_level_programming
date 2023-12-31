#!/usr/bin/python3
"""Documentation for python class"""


class Node:
    """A class example for square"""

    def __init__(self, data, next_node=None):
        """initializes data and next_node as private"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        elif type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """returns data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets size of self to value"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """returns next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets next_node of self to value"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A single linked list class"""
    def __init__(self):
        ''' sets private head'''
        self.__head = None

    def sorted_insert(self, value):
        ''' inserts node to sorted list'''
        if self.__head is None:
            self.__head = Node(value)
        elif value <= self.__head.data:
            new_node = Node(value, self.__head)
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                   current.next_node.data <= value):
                current = current.next_node

            temp = current.next_node
            current.next_node = Node(value, temp)

    def __str__(self):
        ''' prints all linked list values'''
        current = self.__head
        values = []
        while current is not None:
            values.append(str(current.data))
            values.append("\n")
            current = current.next_node
        return ''.join(values[:-1])
