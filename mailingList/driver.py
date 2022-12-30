from abc import ABC, abstractclassmethod
import csv



def merge_family(f1, f2):
    merged_row = {
        'pk': f1['pk'],
        'first_name': f1['first_name'],
        'last_name': f1['last_name'],
    }
    if len(f1['address1']) < len(f2['address1']):
        merged_row['address1'] = f2['address1'] 
    else:
        merged_row['address1'] = f1['address1']
    if len(f1['address2']) < len(f2['address2']):
        merged_row['address2'] = f2['address2']
    else: 
        merged_row['address2'] = f1['address2']
    if len(f1['city']) < len(f2['city']): 
        merged_row['city'] = f1['city']
    else: 
        merged_row['city'] = f1['city']
    if len(f1['state/province']) < len(f2['state/province']): 
        merged_row['state/province'] = f2['state/province']
    else:
        merged_row['state/province'] = f1['state/province']
    if len(f1['zip']) < len(f2['zip']):
        merged_row['zip'] = f2['zip']
    else:
        merged_row['zip'] = f1['zip']
    if len(f1['phone']) < len(f2['phone']):
        merged_row['phone'] = f2['phone']
    else: 
        merged_row['phone'] = f1['phone']
    if len(f1['email']) < len(f2['email']):
        merged_row['email'] = f2['email']
    else:
        merged_row['email'] = f1['email']
    
    return merged_row

def merge_duplicate(data, duplicate):
    merged_row = {
        'pk': data['pk'],
        'first_name': data['first_name'],
        'last_name': data['last_name'],
    }
    if len(data['address1']) < len(duplicate['address1']):
        merged_row['address1'] = duplicate['address1'] 
    else:
        merged_row['address1'] = data['address1']
    if len(data['address2']) < len(duplicate['address2']):
        merged_row['address2'] = duplicate['address2']
    else: 
        merged_row['address2'] = data['address2']
    if len(data['city']) < len(duplicate['city']): 
        merged_row['city'] = duplicate['city']
    else: 
        merged_row['city'] = data['city']
    if len(data['state/province']) < len(duplicate['state/province']): 
        merged_row['state/province'] = duplicate['state/province']
    else:
        merged_row['state/province'] = data['state/province']
    if len(data['zip']) < len(duplicate['zip']):
        merged_row['zip'] = duplicate['zip']
    else:
        merged_row['zip'] = data['zip']
    if len(data['phone']) < len(duplicate['phone']):
        merged_row['phone'] = duplicate['phone']
    else: 
        merged_row['phone'] = data['phone']
    if len(data['email']) < len(duplicate['email']):
        merged_row['email'] = duplicate['email']
    else:
        merged_row['email'] = data['email']

    return merged_row



class FaceoffStatScraper(ABC):

    def __init__(self):
        pass

    def get_query(csv_input):
        print(' ')
        print("****** Getting CSV Filt Data ******* \n")

        with open(csv_input, newline='') as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            qued = [] 

            for row in rows:
                row = {
                    'pk': row[0],
                    'first_name': row[1].lower(),
                    'last_name': row[2].lower(),
                    'address1': row[3].lower(),
                    'address2': row[4].lower(),
                    'city': row[5].lower(),
                    'state/province': row[6].lower(),
                    'zip': row[7].lower(),
                    'phone': row[8].lower(),
                    'email': row[9].lower()
                }
                qued.append(row)

        print(len(qued))
        return qued 

    def remove_duplicates(query):
        dict = {}

        for i in range(0, len(query)): 
            if query[i]['pk'] not in dict:
                for j in  range(0, len(query)): 
                    if i != j: 
                        if query[j]['pk'] not in dict:
                            if query[i]['first_name'] + query[i]['last_name'] == query[j]['first_name'] + query[j]['last_name']: 
                                res = merge_duplicate(query[i], query[j])
                                dict[res['pk']] = res
                            elif query[i]['last_name'] == query[j]['last_name']:
                                if query[i]['address1'] == query[j]['address2']:
                                    res = merge_family(query[i], query[j])
                                    dict[res['pk']] = res
                            elif query[i]['address1'] == query[j]['address1'] or query[i]['address2'] == query[j]['address2']:
                                if query[i]['address1'] == query[j]['address2']:
                                    res = merge_family(query[i], query[j])
                                    dict[res['pk']] = res 
                    else:
                        if query[i]['pk'] not in dict and query[j]['pk'] not in dict:
                            dict[query[i]['pk']] = query[i]
        return dict 

    csv_file_inputed = 'APVH_2022-EOY.txt' 

    query = get_query(csv_file_inputed)
    removed_dups = remove_duplicates(query) 

    print(removed_dups)
    results = []
    for row in removed_dups:
        print('\n')
        print(removed_dups[row])
        r = [removed_dups[row]['pk'], removed_dups[row]['first_name'], removed_dups[row]['last_name'], removed_dups[row]['address1'], removed_dups[row]['address2'], removed_dups[row]['city'], removed_dups[row]['state/province'], removed_dups[row]['zip'], removed_dups[row]['phone'], removed_dups[row]['email']] 

        results.append(r)

    print(results)
    with open('updated_list.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for row in results:
            writer.writerow(row)

FaceoffStatScraper()
