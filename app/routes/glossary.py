# -*- coding: utf-8 -*-

from app import app
from app.models import term
from flask import abort, jsonify, request


# from pprint import pprint
from elasticsearch import Elasticsearch
ES_HOST = {
    "host": "localhost",
    "port": 9200
}
INDEX_NAME = 'glossary'

es = Elasticsearch(hosts=[ES_HOST])



@app.route('/glossary')
def glossary():
    return app.send_static_file('glossary.html')


@app.route('/api/glossary/<string:id>', methods=['GET'])
def get_term(id):
    entity = term.Term.query.get(id)

    if not entity:
        abort(404)
    return jsonify(entity.to_dict())


@app.route('/api/search', methods=['GET'])
def search():
    max_results = request.args.get('max_results', 10)
    max_results = int(max_results)

    query = request.args.get('query')
    entities = term.Term.query.filter(term.Term.id.ilike('%{}%'.format(query))).all()

    if not entities:
        abort(404)

    # return json.dumps([entity.to_dict() for entity in entities[:max_results]])
    return jsonify({'results': [entity.to_dict() for entity in entities[:max_results]]})


@app.route('/api/v2/search', methods=['GET'])
def es_search():
    # max_results = request.args.get('max_results', 10)
    # max_results = int(max_results)
    #
    # query = request.args.get('query')
    # entities = term.Term.query.filter(term.Term.id.ilike('%{}%'.format(query))).all()
    #
    # if not entities:
    #     abort(404)
    #
    # # return json.dumps([entity.to_dict() for entity in entities[:max_results]])
    # return jsonify({'results': [entity.to_dict() for entity in entities[:max_results]]})


    # remote_addr = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    app.logger.info('{} - {}'.format(request.remote_addr, request.url))

    query = request.args.get('q')

    results = es.search(index=INDEX_NAME, q=query)

    hits = results['hits']['hits']

    if not hits:
        abort(404)

    return jsonify({'results': hits})

