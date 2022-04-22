import csv 


# This function removes unecessary data from csv file data
# In this case, the data set needed is row[0], which is the email address


final = []

with open("resQRanchData.txt", newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    que = [] 

    for row in rows:
        print(row)
        if not row[0]:
            print('No row data found, dropping row')
        else:
            que.append(row[0])

    print(que)

with open('filtered.csv', mode='w') as csv_file: 
    fieldnames = ['email']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    final = que

    writer.writeheader()
    for data in final:
        writer.writerow({'email': data})

