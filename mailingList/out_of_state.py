import csv

with open("apvh2021csv.txt", newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')

    qued = [] 

    for row in rows:
        if row[6].lower() != 'colorado':
            qued.append(row)
    
    print(len(qued))

with open('clients_out_state.csv', mode='w') as csv_file:
    fieldnames = ['id', 'first', 'last', 'address', 'address_two', 'city', 'state', 'zip', 'phone', 'email']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for data in qued:
        writer.writerow({'id': data[0], 'first': data[1], 'last': data[2], 'address': data[3], 'address_two': data[4], 'city': data[5], 'state': data[6], 'zip': data[7], 'phone': data[8], 'email': data[9]})
