import requests
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)

CORS(app)
cors = CORS(app, resource={
r"/*":{
    "origins":"*"
}
})

@app.route('/data', methods=['GET'])
def getData():
    try:
        return jsonify([{"html_url":"http://google.com","name":"fdfdfdfd-Golf","description":"dsdfdfdfd","owner":{"login":"mark","repos_url":"https://api.github.com/users/mark/repos","site_admin":"false"}}, {"name":"Golf","description":"dummy","owner":{"login":"mark","repos_url":"https://api.github.com/users/mark/repos","site_admin":"false"}}, {"name":"ASPlus-Golf","description":"dummy","owner":{"login":"mark","repos_url":"https://api.github.com/users/mark/repos","site_admin":"false"}}, {"name":"ASPlus-Golf","description":"dummy","owner":{"login":"mark","repos_url":"https://api.github.com/users/mark/repos","site_admin":"false"}},{"name":"ASPlus-Golf","description":"dummy","owner":{"login":"mark","repos_url":"https://api.github.com/users/mark/repos","site_admin":"false"}}])
    except Exception as e:
        return f"error occurred"

@app.route('/getUsers', methods=['GET'])
def getreq():
    try:
        return jsonify({"success":"successfully done loading get users"})
    except Exception as e:
        return f"error occurred"

@app.route('/getUsers/mark', methods=['GET'])
def getmark():
    try:
        return jsonify({"success":"mark got loaded successfully"})
    except Exception as e:
        return f"error occurred"