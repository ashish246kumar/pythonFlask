from app import app
from models.user_model import user_model
from flask import request
obj=user_model()


@app.route("/home")
def home():
    
    return obj.user_getAll()
    
@app.route("/all_user")
def get_allUser():
    return obj.getAllUser()

@app.route("/addUser",methods=["POST"])
def addUser():
    return obj.addUser(request.form)

@app.route("/addMultiUser",methods=["POST"])
def addMultipleUser():
   
    return obj.addMultipleUser(request.json)

@app.route("/user/patch/<id>", methods=["PATCH"])
def updateOnlyfiewfieldOfUser(id):
    return obj.updateUser(request.form,id)

@app.route("/user/avatar/<uid>", methods=["GET"])
def upload_avatar(uid):
    self.cur.execute(f"SELECT avatar FROM users WHERE id={uid}")
    result = self.cur.fetchall()
    if len(result)>0:
        
        print(type(result))
        return {"payload":result}
    else:
        return "No Data Found"
    
    
    