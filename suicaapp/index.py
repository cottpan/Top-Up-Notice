from bottle import route, run, template

@route('/api/user/<id:int>/<balance:int>')
def index(id,balance):
    return template('<b>ユーザ{{id}}様</b></br></br><b>残高が {{balance}}円です。JR線改札には入れません。チャージしてください。</b>', id=id , balance=balance)

run(host='localhost', port=8080)
