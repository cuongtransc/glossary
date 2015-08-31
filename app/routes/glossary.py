#-*- coding: utf-8 -*-

from app import app, db
from app.models import term
from flask import abort, jsonify, request
import datetime
import json

@app.route('/glossary')
def glossary():
    return app.send_static_file('glossary.html')


@app.route('/api/search', methods=['POST'])
def search():

    # fake data
    json_data = {}
    json_data['en_term'] = 'Accounting Equation'
    json_data['vi_term'] = 'Phương trình kế toán'
    json_data['en_desc'] = "A financial relationship at the heart of the accounting model: Assets = Liabilities + Owners' Equity"
    json_data['vi_desc'] = 'Phản ánh mối quan hệ tài chính, là vấn đề cốt lõi của mô hình kế toán: Tài sản = Nợ phải trả + Vốn chủ sở hữu'

    data = request.get_data()
    # json_data['en_term'] = data

    return jsonify(json_data)

# @app.route('/myapp/users', methods = ['GET'])
# def get_all_users():
#     entities = user.User.query.all()
#     return json.dumps([entity.to_dict() for entity in entities])

@app.route('/api/glossary/<string:id>', methods = ['GET'])
# def get_term(id):
#     entity = term.Term.query.get(id)
#
#     if not entity:
#         abort(404)
#     return jsonify(entity.to_dict())
#
def get_term(id):
    entity = term.Term.query.filter(term.Term.id.ilike('%{}%'.format(id))).all()

    if not entity:
        abort(404)
    # return jsonify(entity.to_dict())
    return jsonify(entity[0].to_dict())
