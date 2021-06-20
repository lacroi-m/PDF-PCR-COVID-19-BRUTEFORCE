from pikepdf import Pdf
import argparse
import re


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
        day1 = "1" 
        month3 = IncrementChar(month3)

    if month2 == '1' and month3 == '2':
        month2 = '0' 
        month3 = '1'
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

    if month3 == charAfterNine:
        month3 = '0'
        month2 = IncrementChar(month2)

    day1 = IncrementChar(day1)
    if day1 == charAfterNine:
        day1 = '0'
        day0 = IncrementChar(day0)

    return day0 + day1 + month2 + month3 + year4 + year5 + year6 + year7


def crack_password(digits, filename, pattern, pn, date):
    passtest = ""

    while True:
        passtest = pn + date
        print("Testing :" + passtest)
        try:
            Pdf.open(filename_or_stream = filename, password = passtest)
            print("Password is " + passtest)
            return True
        except:
            # incorrect password
            pass

        date = Dates(date)
    return False

# Parse Commandline Args
parser = argparse.ArgumentParser(description='Crack numeric passwords of PDFs')
parser.add_argument('filename', help="Full path of the PDF file")
parser.add_argument('startLetters', '--start-name', help="Start name 3 letters: AAA", type=str, default="AAA")
parser.add_argument('startDate', '--start-date', help="Start date format: DDMMYYYY \"01011900\" for 1st Jan 1990", type=str, default="01011900")
args = parser.parse_args()

found_password = False
print("Cracking. Please wait...")
while not found_password:
    print("Trying to crack starting with " + start-name + parser.start-date)
    found_password = crack_password(digits, args.filename, pattern, args.startLetters, parser.startDate)
    digits += 1
if not found_password:
    print("Could not crack the password")