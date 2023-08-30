#!/usr/bin/python3
"""Singly linked list impelementation."""


class Node:
    """A node data structure."""

    def __init__(self, data, next_node=None):
        """Initialize a node.

        Args:
            data (int): data to store.
            next_node (Node): pointer to next node.
        """
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data
        if type(next_node) is not Node:
            if next_node is not None:
                raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node:
            if value is not None:
                raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list data structure."""

    def __init__(self):
        """Initialize a singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """insert a new node in sorted order."""
        new_node = Node(value)
        p = self.__head

        if self.__head is None:
            self.__head = new_node
        while p:
            if p.data > value:
                new_node.next_node = p.next_node
                p.next_node = new_node
                new_node.data = p.data
                p.data = value
                break
            elif p.next_node is None:
                p.next_node = new_node
                break
            p = p.next_node

    def __str__(self):
        p = self.__head
        res = []

        while p:
            res.append(str(p.data))
            p = p.next_node
        return "\n".join(res)
