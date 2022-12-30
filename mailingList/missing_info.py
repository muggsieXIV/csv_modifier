import csv

missing_info = [] 
with open("APVH_2022-EOY.txt", newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:
        if len(row[3]) == 0:
            print(row)
            missing_info.append(row)
        if len(row[5]) == 0:
            if row not in missing_info:
                print(row)
                missing_info.append(row)
        if len(row[6]) == 0:
            if row not in missing_info:
                print(row)
                missing_info.append(row)

    print('missing info')
    print(len(missing_info))

with open('missing_info.csv', mode='w') as csv_file:
    fieldnames = ['id', 'first', 'last', 'address', 'address_two', 'city', 'state', 'zip', 'phone', 'email']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for data in missing_info:
        writer.writerow({'id': data[0], 'first': data[1], 'last': data[2], 'address': data[3], 'address_two': data[4], 'city': data[5], 'state': data[6], 'zip': data[7], 'phone': data[8], 'email': data[9]})
