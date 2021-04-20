"""CSC111 Winter 2021 Final Project: UK VAT Invoice Generation

Instructions
===============================

This Python module contains the dataclasses used in this program.

Copyright Information
===============================

This file is Copyright (c) 2021 Ayesha Nasir.
"""
from __future__ import annotations
from typing import Dict, Any, Optional, Tuple, List


# A class that represents a vendor.
class Vendor:
    """
    A vendor class for the python program. A vendor class would more generally represent the freelance
    worker/contractor that would be sending the invoice.

    Instance Attributes:
        - unique_id: an int that uniquely identifies the vendor
        - name: a str representing the name of the vendor/contractor
        - info: dict containing the remaining information about the vendor.

    Representation Invariants:
        - len(str(unique_id)) == 10
        - name != '' and info != {}
    """
    unique_id: int
    name: str
    info: Dict[Any]
    address: Optional[str]

    #  initializes a new vendor.
    def __init__(self, unique_id: int, name: str, info: Dict[Any]) -> None:
        """
        initializes a new vendor.
        """
        self.unique_id = unique_id
        self.name = name
        self.info = info
        self.address = f'{self.info["street_num"]} {self.info["street_name"]} \n ' \
                       f'{self.info["city"]}, {self.info["state"]} \n ' \
                       f'{self.info["country"]}. {self.info["postal"]}'

    def get_name(self) -> List[any]:
        """
        returns the name in lowercase characters
        """
        return [char.lower() for char in self.name]


# Class that represents a payer or company which receives the invoice.
class Payer:
    """
    A payer class for the python program. A vendor would be a company or person who the bill is sent
    to be paid.

    Instance Attributes:
        - name: a str representing the name of the payer/company.
        - info: dict containing rest of the information about the payer.

    Representation Invariants:
        - name != '' and info != {}
    """
    name: str
    info: Dict[Any]
    address: Optional[str]

    #  initializes a new payer
    def __init__(self, name: str, info: Dict[Any]) -> None:
        """
        initializes a new vendor.
        """
        self.name = name
        self.info = info
        self.address = f'{self.info["street_num"]} {self.info["street_name"]} \n' \
                       f'{self.info["city"]}, {self.info["state"]} \n' \
                       f'{self.info["country"]}. {self.info["postal"]}'

    def get_name(self) -> List[any]:
        """
        returns the name in lowercase characters
        """
        return [char.lower() for char in self.name]


# Class representing an invoice object
class Invoice:
    """
    A class that represents an invoice between a set of payer and vendor for a specific amount and
    services rendered.

    Instance Attributes:
        - vendor: Vendor that is sending the invoice.
        - payer: Payer, reciever of the invoice.
        - services: list of tuples containing the services/product, price and quantity.
        - info: a dict containing rest of the information
    """
    vendor: Vendor
    payer: Payer
    services: List[Tuple]
    info: Dict[Any]

    def __init__(self, vendor: Vendor, payer: Payer, services: List[Tuple],
                 info: Dict[Any]) -> None:
        """
        initializes a list object.
        """
        self.vendor = vendor
        self.payer = payer
        self.services = services
        self.info = info
        # total = 0
        # for service in services:
        #     total += int(service[1]) * int(service[2])
        # self.info['total'] = total


# Tree structure class for autocomplete tree
class AutocompleteTree:
    """
    The tree structure that separates different payer and vendor names
    alphabetically for autocomplete functionality in the program.

    """
    root: Optional[Any]
    subtrees: List[Any]
    item: Optional[Any]

    def __init__(self, root='', subtrees=None) -> None:
        """
        Initializes a new autocomplete tree.
        subtrees can only be a list of one item
        """
        if root != '' and subtrees == []:
            self.root = root
            self.subtrees = subtrees
            self.item = None
        elif root != '' and subtrees != []:
            self.root = root
            self.subtrees = []
            tree = AutocompleteTree(subtrees[0], [])
            self.subtrees.append(tree)
        else:
            self.root = ''
            subtrees = []
            for ltr in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
                tree = AutocompleteTree(ltr, [])
                subtrees.append(tree)
            self.subtrees = subtrees  # initialize with a subtree of lists of alphabet.
            self.item = None

    def get_subtree(self, ltr: str) -> Any:
        """
        returns the subtree corresponding to the given alphabet, else returns an empty str
        """
        for subtree in self.subtrees:
            if subtree.root == ltr:
                return subtree

    def display(self, depth=0) -> str:
        """
        displays the current tree.
        """
        s = '  ' * depth + self.root + ' \n'
        if self.subtrees == []:
            if self.item is not None:
                s += ' ' * (depth + 1) + self.item.name + ' \n'
                return s
            else:
                return s
        else:
            for subtree in self.subtrees:
                s += subtree.display(depth + 1)
            return s

    def subtree_finder(self, lst: List) -> Any:
        """
        finds the subtree.
        """
        tree = self
        index = 0
        for chr in lst:
            if tree.get_subtree(chr) is not None:
                tree = tree.get_subtree(chr)
                index += 1
            else:
                return [tree, index]

        return [tree, index]

    def add_subtree(self, tree_item: Dict[Any]) -> None:
        """
        add a item in the tree. tree_item is a dict with tree_item["list"] = a list of alphabets in
        the item name broken down into a list and tree_item["item"] = an object to be added.
        """
        lst = tree_item['list']
        item = tree_item['item']

        recursing_subtree, index = self.subtree_finder(lst)
        lst = lst[index:]
        while lst != []:
            first_letter = lst.pop(0)  # removes the first alphabet again
            current_tree = AutocompleteTree(first_letter, [])  # creates a tree object
            recursing_subtree.subtrees.append(current_tree)  # adds it as a subtree
            recursing_subtree = current_tree  # changes this to the tree
        recursing_subtree.item = item

    def get_suggestions(self, lst_chr: List) -> List[Any]:
        """
        Returns the auto-complete suggestions for vendors/payers in the form of a list.
        input is a list of characters from the input string in lowercase.

        """
        right_subtree = self.subtree_finder(lst_chr)[0]
        lst_leafs = []
        right_subtree.find_leafs(lst_leafs)
        return lst_leafs

    def find_leafs(self, lst_leafs) -> Any:
        """
        find all leaf nodes in itself.
        """
        if self.item is not None:
            lst_leafs.append(self.item)

        for subtree in self.subtrees:
            subtree.find_leafs(lst_leafs)
