#clientes e o admin

clientes = []

login = input()
senha = input()

admin = False
cliente = False
if login == 'admin' and senha == '123':
    admin = True
else:
    for cliente in clientes:
        print('asdas')