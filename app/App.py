#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/userList', methods=['GET'])
def getUserList():
    tasks = [
        {
            'id': 1,
            'name': u'Mr.zhong',
            'gender': 1
        },
        {
            'id': 2,
            'name': u'A01',
            'gender': 2
        },
        {
            'id': 3,
            'name': u'A02',
            'gender': 2
        },
        {
            'id': 4,
            'name': u'A02',
            'gender': 1
        }
    ]
    return jsonify({'list': tasks})


if __name__ == '__main__':
    app.run()
