# Python Invoice Generator.

This repository contains the final project for CS111 Course at University of Toronto. Instead of opting to work with other teammates, I ended up building this project myself as I was stuck in a very different timezone than the rest of my classmates. This project was inspired by my hopes of automating some part of my dad's job, which involves creating bank reconciliations and invoices for businesses in UK. This project was a first attempt and a generic version. 

### How to run this:

run  pip install -r requirements.txt and pip install tk

(OPTIONAL) Open the file main.py and navigate to line 206 and copy paste the absolute path to Invoices/invoice.pdf. This ensures that once a invoice is generated, it automatically opens in your browser.

Run the main.py file with Python
A GUI screen will open up. use the scroll functionality or search function to chose vendor and payer, and add random amounts/date.
Click on generate Invoice and the generated pdf should open up in the browser if you have followed the optional step above. If not, then you can navigate to the Invoices folder and open the Invoice.pdf to view the invoice generated using your selections.


To see the autocomplete tree structure for specific vendors and payers, use the print function in the console for the display method of the two autocomplete trees, (autocomplete_tree_payer.display() , autocomplete_tree_vendor.display()).

The data folder contains the csv files for the sample list of Vendors and Payers

The CSC111 folder contains the project report in a PDF format detailing the process of creation of the code.
