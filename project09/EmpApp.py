from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file
from config import *
from pymysql import connections
import os
import boto3
# import rds_db as db

app = Flask(__name__)

bucket = custombucket
region = customregion

db_conn = connections.Connection(
    host=customhost,
    port=3306,
    user=customuser,
    password=custompass,
    db=customdb

)
output = {}
table = 'empdata'

@app.route('/')
def index():
    
    return render_template('AddEmp.html')

@app.route('/insert',methods = ['POST'])
def insert():
    
    if request.method == 'POST':
       ename = request.form['ename']
       email = request.form['email']
       ephno = request.form['ephno']
       exp = request.form['exp']
       apt = request.form['apt']
       gdscore = request.form['gdscore']
       hrscore = request.form['hrscore']
       location = request.form['location']
       emp_resume = request.files['emp_resume']
       db.insert_details(ename,email,ephno,exp,apt,gdscore,hrscore,location)
       details = db.get_details()
       print(details)
       for detail in details:
           var = detail
       return render_template('AddEmpOutput.html',var=var)



if __name__ == "__main__":
    
    app.run(debug=True)

# def insert_details(ename,email,ephno,exp,apt,gdscore,hrscore,location):
#     cur=conn.cursor()
#     cur.execute("INSERT INTO empdata (ename,email,ephno,exp,apt,gdscore,hrscore,location) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (ename,email,ephno,exp,apt,gdscore,hrscore,location))
#     conn.commit()

# def get_details():
#     cur=conn.cursor()
#     cur.execute("SELECT *  FROM empdata")
#     details = cur.fetchall()
#     return details