from datetime import datetime, timedelta
import sys
import os
import re

headers = [
    'orderLabel','siteName','contactName','contactEmail','streetAddress1','streetAddress2',
    'city','state','zip','country','requestorName','requestorEmail','devicesRequested',
    'partNumber','deviceModel','orderDate','shipDate','receiveDate','\n'
    ]

requestor_name = 'John Smith'
requestor_email = 'john.smith@me.me'
model = "Lenovo"
class_date = ""

COUNTRY = 'USA'

def main():
    dates = get_dates()

    assembled_strings = []
    assembled_strings.append(",".join(headers))

    parsed_form = parse_form()
    for line in parsed_form:
        assembled_strings.append(assemble_string(line, dates, model))

    index = len(assembled_strings) // 2
    double_check(assembled_strings[index],index)
    save_to_file(assembled_strings)

def get_dates():
    now = datetime.today()

    dates = []
    format = "%m-%d-%Y"

    if now.weekday() in [0,1]:
        
        #Submit Date = Today
        dates.append(now.strftime(format))

        #Ship Date + += 1 or 2 days
        ship_date = now + timedelta(days = 2 if now.weekday() == 0 else 1)
        dates.append(ship_date.strftime(format))

        #Receive Date += 3 or 4 days
        receive_date = now + timedelta(days = 4 if now.weekday() == 0 else 3)
        dates.append(receive_date.strftime(format))

    else:
        dates.append(get_user_input("Enter Submit Date (MM-DD-YYYY): "))
        dates.append(get_user_input("Enter Ship Date (MM-DD-YYYY): "))
        dates.append(get_user_input("Enter Receive Date (MM-DD-YYYY): "))

    return dates

def get_user_input(question):
    response = ""

    while response == "":
        response = input(question)

    return response

def find_file():
    '''
    Look in the same directory as the program to find the csv onboarding form.
    '''
    try:
        files = os.listdir(sys.path[0])
        regex = r"^Notification of Onboarding - "
        for file in files:
            t = re.match(regex, file)
            if t is not None:
                reg_date = re.search(r"(\d+_\d+(_\d+)?).csv$", file)

                global class_date
                class_date = reg_date[1] if reg_date[1] is not None else ""

                return file

    except FileNotFoundError:
        print(f"Onboarding File Not Found or Not a CSV File")
        sys.exit()

def parse_form():

    file = find_file()
    path = os.path.join(sys.path[0], file)

    parsed_form = []

    with open(rf"{path}",mode='rt',encoding='utf-8') as f:
        f.readline() #Skip Headers
        for line in f:
            line_arr = line.split(",")
            line_arr[-1] = line_arr[-1].strip()
            line_arr[-1] = line_arr[-1].rjust(5,"0")

            parsed_form.append(line_arr)

    return parsed_form

def double_check(string,index):
    split_string = string.split(",")
    print(f"Please verify entry on line {index + 1} is correct to make sure the form was formatted correctly.")
    for i in range(len(split_string) - 1):
        print(f"{headers[i]}: {split_string[i]}")

def save_to_file(assembled_strings):

    file_name = f"Formatted_Onboarding_Form_For_Class_{class_date}.csv"
    file_path = os.path.join(sys.path[0], file_name)

    with open(file_path,mode='wt',encoding='utf-8') as f:
        for string in assembled_strings:
            f.write(string)

    print(f"File Saved as {file_name}")

def assemble_string(line, dates, model):
    string = f'Device Order - {line[0]},'
    string += f'{line[0]},' * 2
    string += f'{line[1]},'

    for i in line[-5:-1]:
        string += f'{i},'

    zip = line[-1:][0]
    adjusted_zip = zip.rjust(5,'0')
    string += f'{adjusted_zip},'

    string += f'{COUNTRY},'

    string += f'{requestor_name},'
    string += f'{requestor_email},'

    string += '1,'
    string += f'{model},'
    string += "PC,"

    for date in dates:
        string += f'{date},'

    string += '\n'

    return string


if __name__ == '__main__':
    main()
