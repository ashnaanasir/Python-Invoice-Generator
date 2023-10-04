"""CSC111 Winter 2021 Final Project: UK VAT Invoice Generation

Instructions
===============================

This Python module runs the program and builds the tkinter gui.

Copyright Information
===============================

This file is Copyright (c) 2021 Ayesha Nasir.
"""
import webbrowser
from tkinter import *
from classes.invoice import Invoice
from render_data import autocomplete_tree_payer, autocomplete_tree_vendor
from pdf_invoice_generator import create_invoice

fields_invoice = ('Services', 'Quantity', 'Amount', 'Due Date')
vendor = None
payer = None
invoice = None

root = Tk()
root.title('Invoice Generator')
prg_title = Label(root, text='Please input the following information to generate the Invoice.',
                  font=('Helvetica', 14), fg='black')
prg_title.grid(row=0, column=0, pady=10, padx=5, columnspan=5)


###########################################
# Payer
###########################################
# update payer suggestion box
def update_payer(data) -> None:
    """
    updating the list of suggestions
    """
    payer_suggestion.delete(0, END)

    # add payer suggestions
    for item in data:
        payer_suggestion.insert(END, item.name)


# selecting the Payer:
def selectsuggestion_p(e) -> None:
    """
    adds the selected item into the
    """
    # empty the entry box and add the name to it
    payer_name.delete(0, END)
    name = payer_suggestion.get(ACTIVE)
    payer_name.insert(0, name)

    global payer  # declaring payer as a global value so i can update it inside the function
    option = autocomplete_tree_payer.get_suggestions(list(name.lower()))
    payer = option[0]


def autocomplete_suggestions_p(e) -> None:
    """
    Updating the listbox with autocomplete
    """
    # get the typed characters in payer_name entrybox
    typed = list(payer_name.get())
    update_payer(autocomplete_tree_payer.get_suggestions(typed))


# creating the payer autocomplete entry box:
payer_label = Label(root, text="Enter or Select the company's name:")
payer_label.grid(row=1, column=0, sticky=W, padx=5)
payer_name = Entry(root, font=('Helvetica', 20))
payer_name.grid(row=2, column=0, pady=20, sticky=W, padx=10, columnspan=2)

# creating a payer listbox with automatic suggestions
payer_suggestion = Listbox(root, width=50)
payer_suggestion.grid(row=3, column=0, sticky=W, padx=10, columnspan=2)

update_payer(autocomplete_tree_payer.get_suggestions([]))

# bind on clicking the listbox
payer_suggestion.bind("<<ListboxSelect>>", selectsuggestion_p)

# bind on the payer_name entrybox
payer_name.bind("<KeyRelease>", autocomplete_suggestions_p)


###########################################
# Vendor
###########################################
# update vendor suggestion box
def update_vendor(data) -> None:
    """
    updating the list of suggestions
    """
    vendor_suggestion.delete(0, END)

    # add vendor suggestions
    for item in data:
        vendor_suggestion.insert(END, item.name)


# selecting the Payer:
def selectsuggestion_v(e) -> None:
    """
    adds the selected item into the
    """
    # empty the entry box and add the name to it
    vendor_name.delete(0, END)
    name = vendor_suggestion.get(ACTIVE)
    vendor_name.insert(0, name)

    global vendor  # declaring payer as a global value so i can update it inside the function
    option = autocomplete_tree_vendor.get_suggestions(list(name.lower()))
    vendor = option[0]


def autocomplete_suggestions_v(e) -> None:
    """
    Updating the listbox with autocomplete
    """
    # get the typed characters in vendor_name entrybox
    typed = list(vendor_name.get())
    update_vendor(autocomplete_tree_vendor.get_suggestions(typed))


# creating the payer autocomplete entry box:
vendor_label = Label(root, text="Enter or Select the vendor's name:")
vendor_label.grid(row=1, column=2, sticky="w", padx=5)
vendor_name = Entry(root, font=('Helvetica', 20))
vendor_name.grid(row=2, column=2, pady=20, sticky="e", padx=10, columnspan=2)

# creating a vendor listbox with automatic suggestions
vendor_suggestion = Listbox(root, width=50)
vendor_suggestion.grid(row=3, column=2, sticky="e", padx=10, pady=10, columnspan=2)

update_vendor(autocomplete_tree_vendor.get_suggestions([]))

# bind on clicking the listbox
vendor_suggestion.bind("<<ListboxSelect>>", selectsuggestion_v)

# bind on the vendor_name entrybox
vendor_name.bind("<KeyRelease>", autocomplete_suggestions_v)


###########################################
# Invoice Information
###########################################
invoice_info = {}

invoice_label = Label(root, text="Please enter information about the services:")
invoice_label.grid(row=5, column=0, sticky="W", padx=5)

# service name
service_label = Label(root, text="Services Rendered:")
service_label.grid(row=6, column=0, sticky="w", padx=5)
service_name = Entry(root, font=('Helvetica', 20))
service_name.grid(row=7, column=0, sticky=E, padx=10, pady=5, columnspan=2)


# service quantity
quantity_label = Label(root, text="Quantity:")
quantity_label.grid(row=6, column=2, sticky="w", padx=5)
quantity_name = Entry(root, font=('Helvetica', 20))
quantity_name.grid(row=7, column=2, sticky="e", padx=10, pady=5, columnspan=2)


# Amount name
amount_label = Label(root, text="Amount:")
amount_label.grid(row=8, column=0, sticky="w", padx=5)
amount_name = Entry(root, font=('Helvetica', 20))
amount_name.grid(row=9, column=0, sticky=E, padx=10, pady=5, columnspan=2)


# service quantity
due_label = Label(root, text="Due:")
due_label.grid(row=8, column=2, sticky="w", padx=5)
due_name = Entry(root, font=('Helvetica', 20))
due_name.grid(row=9, column=2, sticky="e", padx=10, pady=5, columnspan=2)


###########################################
# Invoice generation
###########################################
# function that handles the button click:
def generate_invoice(e) -> None:
    """
    Calls the relevant function to generate the required pdf
    """
    global invoice_info
    global vendor
    global payer
    global invoice
    services = (e[0], e[1], e[2])
    invoice_info = {
        'due': e[3]
    }
    invoice = Invoice(
        vendor, payer, services, invoice_info
    )

    create_invoice(invoice)

    webbrowser.open_new('/Invoices/invoice.pdf')
    print('Invoice should automatically open in a chrome window, if it doesn\'t, please navigate '
          'to the invoice folder.')

    root.destroy()


# generate invoice button
btn = Button(root, text="Generate Invoice", bg='white', command=lambda: generate_invoice(e=[
    service_name.get(), quantity_name.get(), amount_name.get(), due_name.get()
]))
btn.grid(pady=10, row=10, column=0)


root.mainloop()
