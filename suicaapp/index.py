from bottle import route, run, template

@route('/api/user/<id:int>')
def index(id):
    return template('<b>残高が {{id}}円です。JR線改札には入れません。チャージしてください。</b>', id=id)

run(host='localhost', port=8080)
