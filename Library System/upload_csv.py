#!/usr/bin/env python3

import csv
import Security

def upload_csv():
    mydb = Security.connect_to_database()
    if mydb is None:
        return False

    cursor = mydb.cursor()
    with open('BooksDataset.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            sql = """
            INSERT INTO Books (Title, Author, Publication, Genre)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (row[0], row[1], row[2], row[3]))

    mydb.commit()
    cursor.close()

    print("Data inserted successfully!")

upload_csv()