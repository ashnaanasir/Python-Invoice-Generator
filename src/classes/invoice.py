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
from .payer import Payer
from .vendor import Vendor


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
        # Following is commented because this program generates an invoice for only one service.
        # total = 0
        # for service in services:
        #     total += int(service[1]) * int(service[2])
        # self.info['total'] = total
