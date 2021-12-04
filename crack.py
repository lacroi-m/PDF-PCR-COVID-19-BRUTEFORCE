#!/usr/bin/python3

import os
import re
import argparse
import pyfiglet
from pikepdf import Pdf
from termcolor import colored

def IncrementChar(char):
    return chr(ord(char) + 1)

charAfterNine = IncrementChar('9')

def AtoZ(last):
    # TODO: Check last is expected / is cap letters and 3 characters 

    last2 = False
    last1 = False
    last0 = False

    if last[2] == 'Z' and last[1] != 'Z':
        last2 = True
        x = IncrementChar(last[1])

    if last[1] == 'Z' and last[0] != 'Z':
        last1 = True
        x = IncrementChar(last[0])

    if last2 == True:
        return  last[0] + x + 'A'

    if last1 == True:
        return  x + 'A' + last[2]

    x = IncrementChar(last[2])
    return  last[0] + last[1] + x


def Dates(last):
    # TODO: Check last is expected / is numeric and 8 characters 

    day0 =   last[0]
    day1 =   last[1]
    month2 = last[2]
    month3 = last[3]
    year4 =  last[4]
    year5 =  last[5]
    year6 =  last[6]
    year7 =  last[7]

    # Reset
    if day0 == '3' and day1 == '1':
        day0 = "0"
        day1 = "0" 
        month3 = IncrementChar(month3)

    if month2 == '1' and month3 == '2':
        month2 = '0' 
        month3 = '0'
        year7 = IncrementChar(year7)

    # Increment
    if year7 == charAfterNine:
        year7 = '0'
        year6 = IncrementChar(year6)
    if year6 == charAfterNine:
        year6 = '0'
        year5 = IncrementChar(year5)
    if year5 == charAfterNine:
        year5 = '0'
        year4 = IncrementChar(year4)
    if year4 == charAfterNine:
        print("OUT DATE")
        exit()

    if month3 == charAfterNine:
        month3 = '0'
        month2 = IncrementChar(month2)

    day1 = IncrementChar(day1)
    if day1 == charAfterNine:
        day1 = '0'
        day0 = IncrementChar(day0)

    # build string
    return day0 + day1 + month2 + month3 + year4 + year5 + year6 + year7

def bruteforce(filename, letters, date, max_date):
    passtest = ""
    testDate = date
    while True:
        passtest = letters + testDate
        print("Testing:" + passtest)
        try:
            Pdf.open(filename_or_stream = filename, password = passtest)
            print("Password is " + passtest)
            return True
        except:
            # incorrect password
            pass

        if (testDate == max_date):
            # increment letters
            letters = AtoZ(letters)

            # reset date
            testDate = date
        else:
            testDate = Dates(testDate)

    return False

def header(filename: str, letters: str, date: str, max_date: str):
   os.system("clear")
   ascii_banner = pyfiglet.figlet_format("PCR PDF CRACKER").upper()
   print(colored(ascii_banner.rstrip("\n"), 'green', attrs=['bold']))
   print(colored("PAR MAXIME LACROIX\n", 'yellow', attrs=['bold']))
   print(colored("filename: " + filename + "\nStarting at letters: " + letters + "\ndate start: " + date + "\nmax date:   " + max_date + "\n\n", 'white', attrs=['bold']))
   return

def menu():
    menu = {}
    menu['1']="Dictionary Attack. (fast)"
    menu['2']="Brut Force Attack. (slow)"
    menu['3']="Exit"

    while True: 
       options=list(menu.keys())
       options.sort()
       for entry in options: 
          print(entry, menu[entry])
       print(colored("\n[?] Please select an option: ",'green'),end='')
       selection=input()
       if selection == "1":
           print("Dictoionary attack")
       if selection == "2":
           print("Brut Force attack") 
           break
       if selection == "3":
           exit()

# Parse Commandline Args
parser = argparse.ArgumentParser(description='Crack numeric passwords of PDFs')
parser.add_argument('--filename', help="Full path of the PDF file", type=str)
parser.add_argument('--letters', help="Start name 3 letters: AAA", type=str, default="AAA")
parser.add_argument('--date', help="Start date format: DDMMYYYY \"01011900\" for 1st Jan 1990", type=str, default="01011900")
parser.add_argument('--max_date', help="End date format: DDMMYYYY \"01012050\" for 1st Jan 2050", type=str, default="01012050")
args = parser.parse_args()

# Check
if args.filename is None:
    parser.print_help()
    exit()
elif os.path.isfile(args.filename) == False:
    print("file '" + args.filename + "' does not exist\nExiting...")
    exit()
elif args.filename.endswith('.pdf') == False:
    print("file '" + args.filename + "' does not have .pdf extension\nExiting...")
    exit()

header(args.filename, args.letters, args.date, args.max_date)
menu()
found_password = False

print("Cracking. Please wait...")
while not found_password:
    print("Trying to crack starting with " + args.filename + args.date)
    found_password = bruteforce(args.filename, args.letters, args.date, args.max_date)
if not found_password:
    print("Could not crack the password")