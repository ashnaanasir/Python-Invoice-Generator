"""CSC111 Winter 2021 Final Project: UK VAT Invoice Generation

Instructions
===============================

This Python module contains the vendor class used in this program.

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
