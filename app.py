from flask import Flask, render_template, jsonify, request, redirect, url_for
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/api/user/propensity-type',methods=['GET'])
def saveTestResult():  # put application's code here
    userPropensityType = request.form['userPropensityType']
    memberPropensityType = request.form['memberPropensityType']
    #csv파일 열기

    #csv파일에 값 추가

    #csv 파일 읽기

    #csv 파일에서 값 가져오기

    #csv 파일에서 값 삭제

    #csv 파일 닫기

    return 'Hello World!'


@app.route('/api/rating',method=['POST'])
def saveMemberRating():  # put application's code here
    rater = request.form['rater']
    userList = request.form['userList']

    #csv파일 열기

    # for user in userList:
        #유저 평가 정보를 csv 파일에 저장

    #csv 파일 닫기

    return 'Hello World!'



if __name__ == '__main__':
    app.run()
