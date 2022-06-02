# onboarding_form_parser
Parses a generic CSV onboarding form into a vendor specific formatted CSV.

See Sample Data files for format it expects and the output that it will provide.

I wrote this with Python 3.8.5 in May 2022.

Before Running:
- Change the requestor_name, requestor_email, model fields in the top of the program

Running the Script:
- From CLI.PowerShell,Terminal
  - Navigate to where the files and script are
  - Windows: <code>python parse_form.py</code>
  - Mac: <code>python3 prase_form.py</code>

Program Flow:
- Calculate the dates, or prompt the user for them
- Parse the onboarding form into a list
- For each entry of the list, take the necessary fields for the date, model, and user address, user name, user email and assemble it into a string
- Pick a random entry in the strings, hardcoded to the middle list element
- Print out the random entry for double checking proper data is parsed
- Save the file and end the program

Features:
- Ability to hardcode fields to lessen manual work
- If this script is run on a Monday or Tuesday it will automatically fill out submission date, ship date, and intended arrival dates. If run on other days it will prompt for date in MM-DD-YY(YY) format
- If the file is named correctly "Notification Of Onboarding - MM/DD.csv" the program will automatically find it
- Program will handle improperly formatted addresses fairly well. It will utilize the correct columns if the headers stay as they are.
- After all is said an done, before saving, it will print a random entry from the formatted list as a potential error catching technique

Future Improvements:
- Error handling with improperly formatted Notification of Onboarding CSV. It will error if the data in form Month/Day is not present and will throw a NoneType error.
- Add specification of file you want to use in CLI or hardcoded field that can be modified
- Better file not found error handling, with potential prompting user for a path
- More error handling/notifying the user of improper formatted data. If a line has more columns than anticipated, it can prompt the user to look at the lines that were incorrectly formatted
- Potentially delete the existing same name file or append a _{random_num} to the end of the file name in case you run this multiple times
