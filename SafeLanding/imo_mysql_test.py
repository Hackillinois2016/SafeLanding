import mysql.connector
import sys

def getIMOSQLQuery(zipCodeList):
    map_table_open = file("diseases_map.txt",'r').read().splitlines()
    map_table_dict = {}
    for line in map_table_open:
        splitted = line.split('#',1)
        map_table_dict[splitted[0]] = splitted[1]

    cnx = mysql.connector.connect(user='USER', password='PASSWORD', host='HOST', port='PORT', database='DATABASE')

    cursor = cnx.cursor()

    zipCodeString = ""
    for x in zipCodeList:
        zipCodeString += x + ","
    zipCodeString = zipCodeString[:-1]

    query = ("SELECT search_result, Count(*) as count FROM requestlog "
            "WHERE zip in ({}) and id > 100000000 and "
            "search_result in (\"Cough\",\"Sinusitis\",\"Chronic sinusitis\",\"Acute sinusitis\",\"URI (upper respiratory infection)\",\"Upper respiratory disease\",\"Upper respiratory infection\",\"Acute upper respiratory infection\",\"Bronchitis\",\"Acute bronchitis\",\"Pneumonia\",\"PNA (pneumonia)\",\"Pharyngitis\",\"Acute pharyngitis\",\"Fever\",\"Fever, unspecified\",\"Sore throat\",\"Acute bronchiolitis\",\"RSV (acute bronchiolitis due to respiratory syncytial virus)\",\"Bronchiolitis\",\"HCV (hepatitis C virus)\",\"Hepatitis C\",\"Strep pharyngitis\",\"Strep throat\",\"Flu\",\"Influenza\",\"MRSA (methicillin resistant staph aureus) culture positive\",\"Bordetella pertussis bacterium\",\"HIV (human immunodeficiency virus infection)\",\"Human immunodeficiency virus (HIV) disease\",\"AIDS\",\"Chicken pox\",\"Rhinovirus\",\"HPV (human papilloma virus) anogenital infection\",\"Human papilloma virus\",\"Measles, mumps and rubella virus vaccine (MMR), live, for subcutaneous use\",\"Other viral agents as the cause of diseases classified elsewhere\",\"Viral infection\",\"Viral syndrome\",\"Viral illness\",\"Measles\") "
            "GROUP BY search_result ORDER BY count DESC".format(zipCodeString))

    zipcode = "85286"

    cursor.execute(query)

    count_tuples = []

    for (SearchResult, Count) in cursor:
        count_tuples.append([SearchResult, Count])

    for count_tuple in count_tuples:
        count_tuple[0] = map_table_dict[count_tuple[0]]

    diseases = set([row[0] for row in count_tuples])

    result_count_tuples = []
    for disease in diseases:
        count = 0
        for tuple in count_tuples:
            if tuple[0] == disease:
                count += tuple[1]
        result_count_tuples.append([disease, count])

    result_count_tuples.sort(key=lambda x: x[1], reverse=True)

    cursor.close()

    cnx.close()

    return result_count_tuples

def getDiseases(tupleList):
    diseaseList = []
    for x in tupleList:
        diseaseList.append(x[0])
    return diseaseList

def getCounts(tupleList):
    countList = []
    for x in tupleList:
        countList.append(x[1])
    return countList