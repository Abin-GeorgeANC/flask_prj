#app/user./user_logic.py
from flask_restful import Resource
from app.user.user_tables import User


class GetUser(Resource):
    def get(self):
        user= User.query.all()
        if user:
            return{'username':user.username,'email':user.email}, 200
        else:
            return {"message":"user not found"}, 404
        