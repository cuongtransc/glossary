__author__ = 'Tran Huu Cuong'

#import pymongo
import csv


from app import app, db
from app.models import term
from flask import abort, jsonify, request
import datetime
import json

#from pymongo import MongoClient

#client = MongoClient('mongodb://localhost:27017/')

#db = client.dict_financial

path_dir = 'data'
filename = 'dict_financial_accounting.csv'

path_file = '{}/{}'.format(path_dir, filename)

with open(path_file) as csvfile:
    # data = csv.reader(csvfile, delimiter=';', quotechar ='"')
    reader = csv.DictReader(csvfile, delimiter=';')

    for row in reader:
        # if index > 10:
        #     break
        #          a = {'en_term' : row[0], 'en_desc' : row[1], 'vi_term' : row[2], 'vi_desc' : row[3]}
        # #		collection = db.dicts
        # #		collection.insert(a);
        #          print('%s: %s' % (a.get('en_term'), a.get('vi_term')))

        entity = term.Term(
            id = row['en_term'].strip().lower(),
            en_term = row['en_term'].strip(),
            en_desc = row['en_desc'].strip(),
            vi_term = row['vi_term'].strip(),
            vi_desc = row['vi_desc'].strip()
        )

        db.session.add(entity)

        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            # raise
        finally:
            db.session.close()
        # continue using session without rolling back
        # db.session.commit()

