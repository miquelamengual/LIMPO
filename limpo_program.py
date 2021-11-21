import csv
from csv import reader
import pandas as pd
from csv import writer
from csv import DictWriter
from tabulate import tabulate
import random as rm

def login():
    col_list = ["Name", "Last_Name", "Username", "Email", "Telephone", "Password"]
    df = pd.read_csv("users.csv", usecols=col_list, index_col=False)
    exus = df["Username"]
    expass = df["Password"]
    us1 = input("Username: ")
    pas1 = input("Password: ")
    sa = 0
    for i in range(len(exus)):
        u = exus[i]
        u = str(u)
        if us1 == u:

            if pas1 == expass[i]:
                print("Successful login")
                sa = 1

    if sa != 1:
        print("\nSorry, the user or the password was incorrect")
        regis()


def regis():
    col_list = ["Name", "Last_Name", "Username", "Email", "Telephone", "Password"]
    df = pd.read_csv("users.csv", usecols=col_list, index_col=False)
    print("Let's get you started!\n")
    name = str(input("Name: "))
    last_name = str(input("Last Name: "))
    username = str(input("Username: "))
    email = str(input("Email: "))
    telephone = str(input("Telephone: "))
    password = str(input("Password: "))
    exus = df["Username"]
    valid_input = False
    while not valid_input:
        x = 0
        for i in range(len(exus)):
            r = exus[i]
            r = str(r)
            fin = len(exus)
            x += 1
            if username == r:
                print("\nSorry, that username is already taken.")
                print("Enter another user name.")
                username = str(input("Username: "))
                x = 0
        if x == fin:
            valid_input = True

    dic = {"name": name, "last_name": last_name, "username": username, "email": email, "Telephone": telephone, "password": password}

    # Pre-requisite - Import the DictWriter class from csv  module


    # The list of column names as mentioned in the CSV file
    headersCSV = ['name','last_name','username', 'email', 'Telephone', 'password']
    # The data assigned to the dictionary
    dict= {'name': str(name), 'last_name': last_name, 'username': username, 'email': email, 'Telephone': telephone, 'password': password}

    # Pre-requisite - The CSV file should be manually closed before running this code.

    # First, open the old CSV file in append mode, hence mentioned as 'a'
    # Then, for the CSV file, create a file object
    with open('users.csv', 'a', newline="") as f_object:
        # Pass the CSV  file object to the Dictwriter() function
        # Result - a DictWriter object
        dicwriter_object = DictWriter(f_object, fieldnames=headersCSV)
        # Pass the data in the dictionary as an argument into the writerow() function
        dicwriter_object.writerow(dict)
        # Close the file object
        f_object.close()

    print("\nAccount created successfully, now log in!\n")
    login()


def book_info():
    print("\nBooking Information")
    print("Please give us a greater insight of your desired cleaning space for us to asses you better\n")

    # Enter house details
    rooms = eval(input("Number of rooms: "))
    sqrdm = eval(input("\nSquared meters of the apartment: "))
    people = input("\nNumber of people living in the apartment: ")
    service = str(input("\nSelect the service you would like to book: \n1) Cleaning, \n2) Laundry, \n3) Cleaning and Laundry: \nEnter the number: "))
    material = input("\nDo you have the necessary material? (Yes / No): ")
    time = input("\nSelect the time (Morning, Noon, Night): ")

    # Store house details
    user_info = {'Number of Rooms': rooms, 'Size of the apartment (m^2)': sqrdm, 'Number of People': people, 'Time': time, 'Type of Service': service, 'Material Available': material}


    # Price calculation

    # base price
    service.lower()
    if service == "1":
        base_price = 10
    elif service == "2":
        base_price = 8
    elif service == "3":
        base_price = 15

    # square meters extra
    if sqrdm > 50:
        extra = 6
    elif sqrdm <= 50:
        extra = 0

    # material extra
    material.lower()
    if material == "no":
        fee = 5
    elif material == "yes":
        fee = 0

    # total cost of service
    total_cost = base_price + (rooms * 3) + extra + fee

    # PRINT ORDER SUMMARY
    d = [["Number of Rooms", rooms],
         ["Size of the apartment (m^2)", sqrdm],
         ["Number of People", people],
         ["Time", time],
         ["Type of Service", service],
         ["Material available", material]]
    print()
    print(tabulate(d, headers=["Service Details", "Option Selected"]))
    print()
    e = [[total_cost]]
    print(tabulate(e, headers=["Total Price (in €)"]))
    input("Press ENTER to continue...")

    return rooms, sqrdm, people, service, time

def cleaner(dsrooms1, dssq1, dspe1, dsse1, dsti1):
    dsrooms = float(dsrooms1)
    dssq = float(dssq1)
    dspe = float(dspe1)
    dsse = float(dsse1)
    dsti = dsti1
    col_list = ["Name", "Rooms", "Sqrdm", "People", "Service", "Time"]
    df = pd.read_csv("limpiaperfil", sep=",", usecols=col_list, index_col=False)
    finalratepercl = {}
    for i in range(0, 10):
        rate = 0
        na = df["Name"][i]
        ro = df["Rooms"][i]
        sq = df["Sqrdm"][i]
        sq1 = sq.split()
        sq2 = float(sq1[0])
        sq3 = float(sq1[2])
        pe = df["People"][i]
        pe1 = float(pe)
        se = df["Service"][i]
        ti = df["Time"][i]
        if ro == dsrooms:
            rate += 1
        if dssq > sq2 and dssq < sq3:
            rate += 1
        if dspe < pe:
            rate += 1
        if dsse == se:
            rate += 1
        if ti == dsti:
            rate += 1
        finalratepercl[na] = rate
    sort_orders = sorted(finalratepercl.items(), key=lambda x: x[1], reverse=True)
    print()
    table = None
    t = [[table]]
    print(tabulate(t, headers=["Cleaner Compatibility (0-5)"]))
    for i in sort_orders:
        print(i[0], i[1])

    print("\nThese are the most compatible cleaners according to your request.")
    final_cleaner = input("Enter your desired cleaner: ")
    print("\nCleaner confirmed!", final_cleaner, "will be there at your selected time!")


def pay():
    print("\nIn order to finalize your booking, please enter your payment information:\n")

    cardholder = input("Card Holder´s name: ")
    cardnumbers = eval(input("\nCredit Card number: "))
    expiracy = input("\nExpiracy Date: ")
    cvv = eval(input("\nCVV: "))

    payment_info = {'Card Holder': cardholder, 'Card Number': cardnumbers, 'Expiracy Date': expiracy, 'CVV': cvv}

    print("\nYour order is confirmed! Thank you for trusting Limpo.")
    ratings = input("\nHow would yo rate your experience from 1 to 5? ")
    print("Thank you! Your feedback helps us improve every day.")


def main():
    print("Welcome to LIMPO!\n")
    print("Please go ahead and sign in if you already have an account or create yours now to become part of the LIMPO community!\n")

    options = input("Do you already have an account (Enter 'y' (YES) or 'n' (NO)): ")

    if options == "YES" or options == "y":
        login()
    if options == "NO" or options == "n":
        regis()

    x1, x2, x3, x4, x5 = book_info()

    cleaner(x1, x2, x3, x4, x5)
    pay()


if __name__ == '__main__':
    main()