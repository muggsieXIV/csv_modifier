import csv


needs_merging = []
with open("apvh2021csv.txt", newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    qued=[]
    for row in rows:
        qued.append(row)

    for eval in qued:
        eval_name = eval[1].lower() + eval[2].lower()

        for row in qued:
            if eval_name == row[1].lower() + row[2].lower():
                if eval[0] != row[0]:
                    if eval not in needs_merging:
                        needs_merging.append(eval)
                    if row not in needs_merging:
                        needs_merging.append(row)
        
    print(needs_merging)
    print('needs_merging: ')
    print(len(needs_merging))

with open('clients_needing_merging.csv', mode='w') as csv_file:
    fieldnames = ['id', 'first', 'last', 'address', 'address_two', 'city', 'state', 'zip', 'phone', 'email']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for data in needs_merging:
        writer.writerow({'id': data[0], 'first': data[1], 'last': data[2], 'address': data[3], 'address_two': data[4], 'city': data[5], 'state': data[6], 'zip': data[7], 'phone': data[8], 'email': data[9]})
