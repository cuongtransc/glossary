# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 21:12:40 2015

@author: coc
"""

from pprint import pprint

from elasticsearch import Elasticsearch

ES_HOST = {
    "host": "localhost",
    "port": 9200
}

INDEX_NAME = 'glossary'

es = Elasticsearch(hosts=[ES_HOST])



# create ES client, create index
query = '''
en_term:accout~
'''

pprint(es.search(index=INDEX_NAME, q=query))

result = es.search(index=INDEX_NAME, q='en_term:acount~')

print(result['hits']['total'])




es.search(index=INDEX_NAME, q='credit',
          fields=['en_term^10', '_all'])


es.search(index=INDEX_NAME, body={'query': {'match': {'_all': 'credit!'}}})



es.search(index=INDEX_NAME, body={'query': {'match': {'_all': 'tôi yêu em !'}}})

          fields=['en_term^10', '_all'])

          , indices_boost=['vi_term'])


results = es.search(index=INDEX_NAME, q='zzzzzzzz')


t = results['hits']['hits'][0]


es.search(index=INDEX_NAME, q='tôi yêu em!')

es.search(index=INDEX_NAME, body={'query': {'match':{'_all': 'tôi yêu em!'}}})


es.search(index=INDEX_NAME, q='en_term:credit')


es.search(q='en_term:credit!')

es.search(q='credit')

matches = es.search(q='credit')
hits = matches['hits']['hits']
print(hits)

es.indices.get_alias()


es.search(q='ke toan')



# es config

from elasticsearch.client import IndicesClient

es.indices.get_alias()


es.indices.get_settings()



es.get_settings('glossary')

es.indices.update_aliases



import requests
import json

res = requests.get('http://localhost:9200')
print(res.content)


res  = requests.get('http://localhost:9200/glossary/_analyze?analyzer=my_analyzer&text="Là tài liệu đầu tiên được xây dựng để đề xuất ý tưởng về dự án với các thành phần cốt lõi"')
print(res.content)

for token in json.loads(res.content.decode('utf-8'))['tokens']:
    print(token['token'])



es.search(q='team')


es.search(q='liệu đầu')

es.search(q='xây dựng nhóm')

es.search(q='Là tài liệu đầu tiên')




requests.get('http://127.0.0.1:5000/secrets')

requests.get('http://127.0.0.1:5000/secrets', auth=('admin', 'secret')).content

