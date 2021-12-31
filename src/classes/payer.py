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
