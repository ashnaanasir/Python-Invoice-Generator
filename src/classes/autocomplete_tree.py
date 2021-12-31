"""CSC111 Winter 2021 Final Project: UK VAT Invoice Generation

Instructions
===============================

This Python module contains the payer class used in this program.

Copyright Information
===============================

This file is Copyright (c) 2021 Ayesha Nasir.
"""
from __future__ import annotations
from typing import Dict, Any, Optional, Tuple, List


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
        if not self.subtrees:
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
        for char in lst:
            if tree.get_subtree(char) is not None:
                tree = tree.get_subtree(char)
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
        while lst:
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
