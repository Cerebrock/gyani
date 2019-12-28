# -*- coding: utf-8 -*-

import os
from time import strftime
import json
import boto3
from flask_cors import CORS
from flask import Flask, render_template, request

#exp_path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)#, template_folder=exp_path)
CORS(app)
s3 = boto3.client('s3')

bucket_name = 'unket'
folder = 'gyani'

@app.route('/postdata', methods = ['POST'])
def get_data(to_s3=True):
    out_name = folder + '/' + strftime('%Y-%m-%d_%H-%M-%S') + ".json"
    data = request.form['data']
    print(out_name)

    if to_s3:
        resp = s3.put_object(Bucket=bucket_name,
                  Key=out_name,
                  Body=json.dumps(data))
    else:
        with open(exp_path + '\data\\' + out_name, 'a+') as out:
            out.write(data)
    return ''

@app.route('/', methods = ['GET'])
def greet():
    return '<div>Server para recolección</div>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
