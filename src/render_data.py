"""CSC111 Winter 2021 Final Project: UK VAT Invoice Generation

Instructions
===============================

This Python module creates the autocomplete tree structure for payer and vendor data.

Copyright Information
===============================

This file is Copyright (c) 2021 Ayesha Nasir.
"""
from src.classes.vendor import Vendor
from src.classes.autocomplete_tree import AutocompleteTree
from src.classes.payer import Payer
from csv import reader


list_vendors = []  # creating a list of vendors for creation of the autocomplete tree.

with open('../data/vendor_data.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    next(csv_reader)  # to skip the header file.
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        unique_id, name, phone, email, website = row[0:5]  # personal info
        street_num, street_name, city, state, country, postal = row[5:11]  # address
        service_type, vat_rate = row[11:13]  # invoicing information
        vendor = Vendor(unique_id, name, {
            'phone': phone,
            'email': email,
            'website': website,
            'street_num': street_num,
            'street_name': street_name,
            'city': city,
            'state': state,
            'country': country,
            'postal': postal,
            'service_type': service_type,
            'vat_rate': vat_rate
        })
        list_vendors.append(vendor)


list_payers = []  # creating a list of possible payers for creation of autocomplete tree.

with open('../data/payer_data2.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    next(csv_reader)  # to skip the header file.
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        name = row[0]
        street_num, street_name, city, state, country, postal = row[1:7]
        email, phone = row[7:9]
        payer = Payer(name, {
            'street_num': street_num,
            'street_name': street_name,
            'city': city,
            'state': state,
            'country': country,
            'postal': postal,
            'email': email,
            'phone': phone
        })

        list_payers.append(payer)


# Creating autocomplete tree for the payer

autocomplete_tree_payer = AutocompleteTree()

for p in list_payers:
    autocomplete_tree_payer.add_subtree({
        'list': p.get_name(),
        'item': p
    })


# creating autocomplete tree for the Vendor


autocomplete_tree_vendor = AutocompleteTree()

for p in list_vendors:
    autocomplete_tree_vendor.add_subtree({
        'list': p.get_name(),
        'item': p
    })
