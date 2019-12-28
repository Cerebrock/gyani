# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import os
import boto3
from time import strftime

exp_path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=exp_path)

s3 = boto3.client('s3', 'AKIAJZ46CC3EET5DNKAA', 'Q/f7tdaTWCe/fqSIQF7FFPBjwKSrlDx8w7hsTrcs')

@app.route('/postdata', methods = ['POST'])
def get_data(to_s3=True): 
    out_name = f"gyani/{strftime('%Y-%m-%d %H-%M-%S')}_{request.referrer}.json"
    data = request.form['data']
    bucket_name = 'unket'

    if to_s3:
        resp = s3.put_object(Bucket=bucket_name,
                  Key=out_name,
                  Body=json.dumps(data).encode())

    else:
        with open(exp_path + '\data\\' + out_name, 'a+') as out:
            out.write(data)
    return ''

if __name__ == '__main__':
    app.run(host="0.0.0.0")
