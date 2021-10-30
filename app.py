from flask import Flask, jsonify, request
import operator
import csv
import typeDict
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/api/user/propensity-type', methods=['GET'])
def getPropersityType():  # put application's code here
    userType = request.args['userPropensityType']
    memberType = request.args['memberPropensityType']

   #읽기모드로 csv파일 열기
    f = open('scope.csv','r')
    csvR = csv.reader(f)

    # data에 csv값 list로 저장
    data = list(csvR)

    #csv 파일 닫기
    f.close()

    # 가중치
    weight= 2

    #data에 가중치 더한 값 추가 data[본인성향][상대방성향]
    data[typeDict.type[userType]][typeDict.type[memberType]] = int(data[typeDict.type[userType]][typeDict.type[memberType]]) + weight

    #user의 성향인 사람들이 추천한 값을 딕셔너리 형태로 변환
    dic = {}
    for i, d in zip(typeDict.propersityTypeList, data[typeDict.type[userType]][1:]):
        dic[i] = int(d)

    #내림차순으로 정렬 (추천 많은 순)
    sortDic = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True))
    print(sortDic)
    recommendedTypeList = list(sortDic.keys())

    #가중치 더한 값 다시 뺴기
    data[typeDict.type[userType]][typeDict.type[memberType]] = int(
        data[typeDict.type[userType]][
            typeDict.type[memberType]]) - weight

    return jsonify({'status': "200", 'msg': "팀원평가 저장 완료", "data":{'userPropensityType': userType, 'recommendedPropensityType': recommendedTypeList}})


@app.route('/api/rating', methods=['POST'])
def saveMemberRating():
    # 평가자
    rater = request.json['rater']

    # 피평가자 리스트
    userList = request.json['userList']

    # csv파일 읽기 모드로 열기
    f = open('scope.csv','r')
    csvR = csv.reader(f)

    # 리스트로 저장
    data = list(csvR)

    # csv 파일 닫기
    f.close()

    # csv파일 쓰기 모드로 열기
    f = open('scope.csv', 'w', newline="")
    csvW = csv.writer(f)

    # 유저 평가 정보를 data에 저장
    for i in userList:
        data[typeDict.type[rater]][
            typeDict.type[i]] = int(
            data[typeDict.type[rater]][
                typeDict.type[i]]) + 1
    # 바뀐 data를 csv 파일에 저장
    csvW.writerows(data)

    # csv 파일 닫기
    f.close()

    return jsonify({'status': "200", 'msg': "팀원평가 저장 완료"})

if __name__ == '__main__':
    app.run()
