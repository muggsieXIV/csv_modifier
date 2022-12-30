
# fields = [
#     Customer First Name	
#     Customer Last Name	
#     Date of birth	
#     Customer Gender	
#     Customer Address1	
#     Customer Address2	
#     City	
#     State/Province	
#     Zip/Postal Code	
#     Customer Email	
#     Head of Household		
# ]

"""
This script finds a head of house and populates an athlete with missing information.
"""

import csv 
from abc import ABC


class CorrectDB(ABC):

    def read_csv():
        result = []
        with open('12-29-22-data.csv', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                result.append(row)
        return result

    def write_to_csv(data):
        with open('results.csv', 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for d in data:
                csv_writer.writerow(d)

    def correct_data(data):
        result = []
        for eval in data:
            if eval not in result:
                if eval[-1] == 'Yes':
                    result.append(eval)
                    print('Found a head of house, adding to results...')

                if eval[-1] == 'No':
                    last_name = eval[1].lower()
                    address = eval[4].lower() 

                    for row in data:
                        if row[-1] == 'Yes':

                            if row[1].lower() == last_name and row[4].lower() == address:

                                print(address + ' ' + last_name)
                                print(row[4].lower() + ' ' + row[1].lower())
                                print('Found matching athlete, correcting rows, adding to results...')

                                email_address = eval[-2]
                                print(email_address)
                                if len(email_address) < 2: 
                                    print(row[-2])
                                    email_address = row[-2]

                                    athlete = [
                                        eval[0],
                                        eval[1],
                                        eval[2],
                                        eval[3],
                                        row[4],
                                        row[5],
                                        row[6],
                                        row[7], 
                                        row[8],
                                        email_address,
                                        eval[10]
                                    ]
                                    print('eval')
                                    print(eval)
                                    print('row')
                                    print(row)
                                    print('athlete')
                                    print(athlete)
                                    print('Inserted')
                                    result.append(athlete)
        return result

    data = read_csv() 
    corrected_data = correct_data(data)
    write_to_csv(corrected_data)

CorrectDB