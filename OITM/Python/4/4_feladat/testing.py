import pandas as pd
import re

excel_file_path = 'emails.xlsx'

df = pd.read_excel(excel_file_path, sheet_name='EMAILS')

# load all the emails into a list

listofemails = list(df.iloc[:, 0])

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
# Define a function for

counter = 0
counter_non = 0
# for validating an Email
def check(email):
    global counter
    global counter_non
    if type(email) != str:
        print("Invalid Email")
        counter_non += 1
        return
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        print("Valid Email:", email)
        counter += 1
 
    else:
        print("Invalid Email:", email)
        counter_non += 1

for email in listofemails:
    check(email)

print(counter)
print(counter_non)