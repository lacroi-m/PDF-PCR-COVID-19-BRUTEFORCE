#!/usr/bin/python3

import os
import re
import argparse
import pyfiglet
from pikepdf import Pdf
from termcolor import colored
from datetime import datetime, timedelta

datetimeFormat = '%d%m%Y'

def IncrementChar(char):
    return chr(ord(char) + 1)

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


def bruteforce(filename: str, letters: str, date: datetime, max_date: datetime):
    passtest = ""
    testDate = date
    while True:
        passtest = letters + testDate.strftime(datetimeFormat)
        print("Testing:" + passtest)
        try:
            Pdf.open(filename_or_stream = filename, password = passtest)
            print("Password is " + passtest)
            return True
        except:
            # incorrect password
            pass

        if (testDate.strftime(datetimeFormat) == max_date.strftime(datetimeFormat)):
            # increment letters
            letters = AtoZ(letters)

            # reset date
            testDate = date
        else:
            testDate += timedelta(days=1)

    return False

def header(filename: str, letters: str, date: datetime, max_date: datetime):
   os.system("clear")
   ascii_banner = pyfiglet.figlet_format("PCR PDF CRACKER").upper()
   print(colored(ascii_banner.rstrip("\n"), 'green', attrs=['bold']))
   print(colored("PAR MAXIME LACROIX\n", 'yellow', attrs=['bold']))
   print(colored("filename: " + filename + "\nStarting at letters: " + letters + "\ndate start: " + date.strftime(datetimeFormat) + "\nmax date:   " + max_date.strftime(datetimeFormat) + "\n\n", 'white', attrs=['bold']))
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
           print("Dictoionary attack - Not ready yet")
           # TODO: setup dictoionary attack with all combinaisons
           exit()
       if selection == "2":
           print("Brut Force attack") 
           break
       if selection == "3":
           exit()

# Parse Commandline Args
parser = argparse.ArgumentParser(description='Crack numeric passwords of PDFs')
parser.add_argument('--filename', help="Full path of the PDF file", type=str)
parser.add_argument('--letters', help="Start name 3 letters: AAA will increment until ZZZ", type=str, default="AAA")
parser.add_argument('--date', help="Start date format: DDMMYYYY \"01011900\" for 1st Jan 1900", type=str, default="01011900")
parser.add_argument('--max_date', help="End date format: DDMMYYYY \"01012025\" for 1st Jan 2025", type=str, default="01012025")
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

if len(args.letters) != 3:
    print("letters must be 3 letters !\nExiting...")
    parser.print_help()
    exit()
elif args.letters.isnumeric() == True:
    print("letters must be 3 letters not numbers !\nExiting...")
    parser.print_help()
    exit()

if args.date.isnumeric() == False | args.max_date.isnumeric() == False:
    print("date or max_date argument should only contain numbers")
    print("got '" + args.date + "' instead\nExiting...")
    exit()
elif len(args.date) != 8 | len(args.max_date) != 8:
    print("date or max_date argument should only be specified length")
    parser.print_help()
    exit()

# Handle date
day   =  args.date[:2]
month =  args.date[2:4]
year  =  args.date[4:]
startDatetime = datetime(int(year), int(month), int(day))

day   =  args.max_date[:2]
month =  args.max_date[2:4]
year  =  args.max_date[4:]
maxDatetime = datetime(int(year), int(month), int(day))

header(args.filename, args.letters, startDatetime, maxDatetime)
menu()
found_password = False

print("Cracking. Please wait...")
while not found_password:
    found_password = bruteforce(args.filename, args.letters, startDatetime, maxDatetime)
if not found_password:
    print("Could not crack the password")