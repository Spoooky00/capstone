import pymysql.cursors

from app import app
from config import mysql
from flask import Flask, render_template, request, redirect, jsonify



# Route to render the login page
@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

# Route to render the clinic_admin page
@app.route('/clinic_admin')
def clinic_admin():
    return render_template('clinic_admin.html')

# Route to render the events page
@app.route('/events')
def events():
    return render_template('events.html')

# Route to render the account_management page
@app.route('/account_management',methods=['GET','POST'])
def account_management():
    if request.method == 'GET':
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT* from `account_management`")
            accountmanagement = cursor.fetchall()
            print(accountmanagement)
            return render_template('account_management/account_management2.html', data=accountmanagement)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    if request.method == 'POST':
        print("hello")

#update
@app.route('/updateAM/<int:id>',methods=['GET','POST'])
def updateAM(id):
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT* from `account_management` where Am_ID = %s", id)
        accountmanagement = cursor.fetchall()
        print(accountmanagement)
        return render_template('updateAM.html', data=accountmanagement)
    if request.method == 'POST':
        _Username = request.form['Username']
        _Password = request.form['Password']
        _Email = request.form['Email']
        _Role = request.form['Role']

        if request.form:
            query = "update account_management set Username=%s , Email=%s, Password=%s, Role=%s where Am_ID=%s"
            bindData = (_Username,_Email,_Password,_Role,id)
            conn = mysql.connect()
            cursor = conn.cursor()
            print(query,bindData)
            cursor.execute(query,bindData)
            conn.commit()
            return redirect('/account_management')
#add
@app.route('/addAm',methods=['POST'])
def addAm():
    if request.method == 'POST':
        print("result : "+str(request.json))
        _Username = request.json['Username']
        _Email = request.json['Email']
        _Role = request.json['Role']
        if request.json:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "insert into account_management(Username,Email,Role) values(%s,%s,%s)"
            bindData = (_Username,_Email,_Role)
            cursor.execute(query,bindData)
            conn.commit()
            return redirect('/account_management')
    #render_template('addDL.html')


# Route to render the patient_masters_record page
@app.route('/patient_masters_record')
def patient_masters_record():
    return render_template('patient_masters_record.html')

#########################DAILY LOGS ROUTES
# Route to render the daily_logs page
@app.route('/daily_logs',methods=['GET','POST'])
def daily_logs():
    if request.method == 'GET':
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT* from `patient_permanent_records` JOIN `daily_logs` on `patient_permanent_records`.`User_NFC_ID` = `daily_logs`.`User_NFC_ID`;")
            dailylogs = cursor.fetchall()
            print(dailylogs)
            return render_template('daily_logs.html', data=dailylogs)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    if request.method == 'POST':
        print("hello")

#update
@app.route('/updateDL/<int:id>',methods=['GET','POST'])
def updateDL(id):
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT* from `patient_permanent_records` JOIN `daily_logs` on `patient_permanent_records`.`User_NFC_ID` = `daily_logs`.`User_NFC_ID` where `DL_ID`=%s;",id)
        dailylogs = cursor.fetchall()
        print(dailylogs)
        return render_template('updateDl.html', data=dailylogs)
    if request.method == 'POST':
        _NFC = request.form['NFC']
        _Concern  = request.form['DL_Concern']
        _TI = request.form['DL_TI']
        _TO  = request.form['DL_TO']
        if request.form:
            query = "update daily_logs set DL_Concerm=%s, DL_Timein=%s, DL_Timeout=%s where DL_ID=%s"
            bindData = (_Concern,_TI,_TO,_NFC)
            conn = mysql.connect()
            cursor = conn.cursor()
            print(query,bindData)
            cursor.execute(query,bindData)
            conn.commit()
            return redirect('/daily_logs')
#add
@app.route('/addDL',methods=['POST'])
def addDL():
    if request.method == 'POST':
        print("result : "+str(request.json))
        _nfc = request.json['nfc']
        _concern = request.json['concern']
        _ti = request.json['ti']
        _to = request.json['to']
        if request.json:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "insert into daily_logs(USER_NFC_ID,DL_Concerm,DL_Timein,DL_Timeout) values(%s,%s,%s,%s)"
            bindData = (_nfc,_concern,_ti,_to)
            cursor.execute(query,bindData)
            conn.commit()
            return redirect('/daily_logs')
    #render_template('addDL.html')


#########################INVENTORY ROUTES
# Route to render the inventory page
@app.route('/inventory',methods=['GET','POST'])
def inventory():
    if request.method == 'GET':
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT* from `inventory`")
            inventory = cursor.fetchall()
            print(inventory)
            return render_template('Inventory/Inventory.html', data=inventory)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    if request.method == 'POST':
        print("hello")

#update
@app.route('/updateinventory/<int:id>',methods=['GET','POST'])
def updateinventory(id):
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
             "SELECT* from `inventory` where Item_ID = %s",id)
        inventory = cursor.fetchall()
        print(inventory)
        return render_template('inventory/updateInventory.html', data=inventory)
    if request.method == 'POST':
        _name = request.form['Item_name']
        _Quantity = request.form['Quantity']
        _Manufacturer = request.form['Manufacturer']
        _Description = request.form['Description']
        _code = request.form['Item_code']
        _expiry = request.form['Item_expiry']
        _type = request.form['Item_type']


        if request.form:
            query = "update inventory set Item_name=%s, Quantity=%s ,Manufacturer=%s , Description=%s , Item_code=%s , Item_expiry=%s , Item_type=%s  where Item_ID = %s"
            bindData = (_name,_Quantity, _Manufacturer,_Description,_code,_expiry,_type,id)
            conn = mysql.connect()
            cursor = conn.cursor()
            print(query,bindData)
            cursor.execute(query,bindData)
            conn.commit()
            return redirect('/inventory')
#add
@app.route('/addinventory',methods=['POST'])
def addinventory():
    if request.method == 'POST':
        print("result : "+str(request.json))
        _name = request.json['Item_name']
        _quantity = request.json['Quantity']


        if request.json:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "insert into inventory(Item_name,Quantity,Manufacturer,Description,Item_code,Item_expiry,Item_type) values(%s,%s,%s,%s,%s,%s)"
            bindData = (_name,_quantity)
            cursor.execute(query,bindData)
            conn.commit()
            return redirect('/Inventory')


if __name__ == '__main__':
    app.run(debug=True)
