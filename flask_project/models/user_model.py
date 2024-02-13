# from datetime import datetime,timedelta

import mysql.connector
import json
from flask import make_response,jsonify

class user_model():
    def __init__(self):
        self.con=mysql.connector.connect(host='localhost',user='root',
                                         password='Ashish4N',
                                         database="flask_user"
                                         )
        self.con.autocommit=True
        self.cur = self.con.cursor(dictionary=True)

    
    def user_getAll(self):
        return "user added sucessfully"
    
    def getAllUser(self):
        self.cur.execute("SELECT * from users")
        result=self.cur.fetchall()
        if len(result)>0:
            return {"payload":result}
        else:
            return "No data found" 
    
    def addUser(self,data):
        self.cur.execute(f"INSERT INTO users(id,name,email,phone,role,password) VALUES ("
                         f"'{data['id']}', "
                        f"'{data['name']}', "
                        f"'{data['email']}', "
                        f"'{data['phone']}', "
                        f"'{data['role']}', " 
                        f"'{data['password']}'" 
                        ")"
                        )
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)
       
    def addMultipleUser(self,data):
        qry="INSERT INTO users(id,name,email,phone,role,password) VALUES"
        for userdata in data:
           
            qry+= f"('{userdata['id']}','{userdata['name']}','{userdata['email']}','{userdata['phone']}', '{userdata['role']}','{userdata['password']}'),"
           
       
        finalqry=qry.rstrip(",")
        self.cur.execute(finalqry)
        
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)
                        
    def updateUser(self,data,id):
        
        
        qry="UPDATE users SET "
        # for key in data:
        #     if key!='id':
        #         qry+=f"{key}='{data[key]}',"
        # qry=qry[:-1]+f"where id={data['id']}" 
        for key in data:
            if key!='id':
                qry += f"{key}='{data[key]}',"
        qry = qry[:-1]+" WHERE id ="+id        
        # qry = qry[:-1] + f" WHERE id = {data['id']}"
        print(qry)
        # return "updated"       
        self.cur.execute(qry)
        if self.cur.rowcount>0:
            return  make_response({"message":"CREATED_SUCCESSFULLY"},201)
        else:
             return  make_response({"message":"Nothing to update"},204)
         
    
    def get_avatar_path_model(uid):
                         
            
            
            