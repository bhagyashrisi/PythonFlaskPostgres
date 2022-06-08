from flask import Flask, jsonify, request
from flask_migrate import Migrate
from demo import model
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bhagya@localhost:5432/staff'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
model.db.init_app(app)
migrate = Migrate(app, model.db)

@app.route('/register_user', methods=['POST'])
def registration():
    if request.is_json:
        data = request.get_json()
        print(data)
        new_user = model.User(id=data['id'], username=data['username'], email=data['email'], password_hash=generate_password_hash(data['password']), joined_at=data['joinedat'])
        model.db.session.add(new_user)
        model.db.session.commit()
        return {"message": f"user record {new_user.username} has been created successfully."}
    else:
        return {"error": "The request payload is not in JSON format"}

@app.route('/login', methods=['POST'])
def login():
    print('Getting userdata')
    try:
      data = request.get_json()
      print(data)
      rows = model.User.query.filter_by(username=data['username']).first()
      if not rows:
        return {'status':'USER404', 'message': 'user not found'} #returning empty response
      else:
        result = [
              {
                  'id': rows.id,
                  'username': rows.username,
                  'password_hash':rows.password_hash,
                  'joined_at': rows.joined_at,
                  'email': rows.email
              } ]
        checkResp=check_password_hash(rows.password_hash,data['password'])
        print(checkResp)
        if checkResp == True:             
          return jsonify(result)  # returning response
        else:
          return {'status':'PASS500','message':'invalid password'}

    except Exception as error:
      print(error)
      return str(error)

         
if __name__ == "__main__":
  app.run(debug=True)