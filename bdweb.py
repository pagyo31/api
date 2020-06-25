import pymysql
from flask import Flask, jsonify, request


conexao = pymysql.connect( #conectando ao banco de dados
    host= '3306',
    user= 'root',
    passwd= '',
    database= 'python'
)

app = Flask(__name__)

clientes = []

cursor = conexao.cursor() #cria um cursor para navegr pelo banco de dados
cursor.execute("SELECT * FROM clientes")
for c in cursor:
    clientes.append(c)

print(clientes)

@app.route('/',)
def home():
    return jsonify(clientes), 200

@app.route('/', methods=['POST'])
def post():
    data = request.get_json()
    user = data["user"]
    passw = data["pass"]
    add_sql = "INSERT INTO clientes(user,pass) VALUES (%s,%s)" #adicionadno o dado mesmo na tabela
    valor = (user, passw) #valor q serao acrescentados na tabela
    cursor.execute(add_sql,valor)
    conexao.commit() #para realmente efetivar qualquer troca na tabela
    print(cursor.rowcount,"inserida com sucesso")
    clientes.append(data)
    return jsonify(clientes), 201


if __name__ == '__main__':
    app.run(debug=True,port=0000)
