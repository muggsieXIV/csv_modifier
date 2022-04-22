import csv

final = []

with open("final_test.txt", newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    qued = [] 

    def FindDoubles(eval):
        eval_name = eval[1].lower() + eval[2].lower()
        eval_address = eval[3].lower() + eval[5].lower() + eval[6].lower() + eval[7].lower()
        eval_phone = eval[8]
        eval_email = eval[9].lower()
        eval_zip = eval[7]

        set_row = eval
        print(eval)

        for row in qued:
            if len(eval_name) == row[1].lower() + row[2].lower():
                if len(eval_address) <= len(row[3]) + len(row[5]) + len(row[6]) + len(row[7]):
                    if len(eval_phone) <= len(row[8]):
                        if len(eval_email) <= len(row[9]):
                            set_row = row 
                            print(row)
        
        for join in qued:
            if len(eval_zip) >= 5:
                if len(eval_name) != row[1].lower() + row[2].lower():
                    if eval_address == row[3].lower() + row[5].lower() + row[6].lower() + row[7].lower():
                        first_names = eval[1].lower() + ' ' + row[1].lower()
                        last_names = eval[2].lower() + ' ' + eval[2].lower()
                        address = row[3].lower()
                        city = row[5].lower()
                        state = row[6].lower() 
                        zip = row[7]
                        ids = str(eval[0]) + ' ' + str(row[0])
                        if eval_phone == row[8]:
                            phone = eval_phone
                        if eval_phone != row[8]:
                            phone = str(eval[8]) + ' ' + str(row[8])
                        if eval_email == row[9]:
                            email = eval_email
                        if eval_email != row[9]:
                            email = str(eval_email + ' ' + row[9])
                        if eval[4] == row[4]:
                            address_two = row[4]
                        if eval[4].lower() != row[4].lower():
                            address_two = str(eval[4] + row[4])
                        
                        set_row = [ids, first_names, last_names, address, address_two, city, state, zip, phone, email]

        return set_row 

    for row in rows:
        if row[6].lower() == 'colorado':
            if len(row[3]) != 0:
                if len(row[5]) != 0:
                    qued.append(row)
                    print(qued)
                    print(qued)
                    print(qued)
                    print(qued)
                    print(qued)
                    print(qued)

    for eval in qued:
        print(eval)
        print(qued)
        passed = FindDoubles(eval)
        print(passed)
        final.append(passed)
        print(final)

with open('apvh2021_colorado.csv', mode='w') as csv_file:
    fieldnames = ['id', 'first', 'last', 'address', 'address_two', 'city', 'state', 'zip', 'phone', 'email']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for data in final:
        writer.writerow({'id': data[0], 'first': data[1], 'last': data[2], 'address': data[3], 'address_two': data[4], 'city': data[5], 'state': data[6], 'zip': data[7], 'phone': data[8], 'email': data[9]})

