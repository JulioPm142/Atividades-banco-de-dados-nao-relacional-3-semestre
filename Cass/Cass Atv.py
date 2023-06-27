from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {
    'secure_connect_bundle': './secure-connect-fatec.zip'
}
auth_provider = PlainTextAuthProvider('juliopm142@gmail.com', '!07062004Er')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

session.set_keyspace('biblioteca')

table_name = 'usuario'

def Inserir(tabela):
    if tabela==1:
        id=int(input('Qual o id do Usuário? '))
        cpf=str(input('Qual o Cpf do Usuário? '))
        nome=str(input('Qual o Nome do Usuário? '))
        sobrenome=str(input('Qual o sobrenome do Usuário? '))
        email=str(input('Qual o Email do Usuário? '))
        favoritos = []
        addFavorito = input("Adicionar um Produto favorito? s/n ")
        if addFavorito == 's':
            addFavorito = int(input("Quantos produtos adicionar aos favoritos? "))
            selecionar(3)
            for x in range(addFavorito):
                favoritos.append(str(input("Qual o Id do Produto? ")))
            favoritos_string = ','.join(favoritos)
        else:
            favoritos_string = ""

        insert_query = f"INSERT INTO usuario (id, cpf, nome, sobrenome, email, favoritos) VALUES ({id}, '{cpf}', '{nome}', '{sobrenome}', '{email}', '{favoritos_string}')"


    if tabela==2:
        id=int(input('Qual o id do Vendedor? '))
        cpf=str(input('Qual o Cpf do Vendedor? '))
        nome=str(input('Qual o Nome do Vendedor? '))
        NumeroProdutos=int(input('Quantos produtos adicionar ao vendedor?'))
        produtos=[]

        for x in range(NumeroProdutos):
            cadaProduto=[]
            selecionar(3)
            Produto_id=str(input('id do Produto: '))
            cadaProduto=[Produto_id]
            produtos.append(cadaProduto)
        todosProds=''
        cadaProduto=''
        for x in produtos:
            for y in x:
                cadaProduto+= str(y)+','
            
        todosProds= todosProds + str(cadaProduto)


        insert_query = f"INSERT INTO vendedor (id, cpf, nome, produtos) VALUES ({id}, '{cpf}', '{nome}','{str(todosProds)}')"

    if tabela==3:
        Produto_Id = str(input('Id do produto: '))
        Produto_Nome=str(input('Nome Produto: '))
        Produto_Preco=str(input('Preço Produto: '))
        Produto_Descricao=str(input('Descricao Produto: '))
        insert_query = f"INSERT INTO produto (id, nome, preco, descricao) VALUES ({Produto_Id}, '{Produto_Nome}', '{Produto_Preco}','{Produto_Descricao}')"

    if tabela==4:
        id_compra=str(input('Qual o id da Compra? '))
        selecionar(1)
        id_Cliente=str(input('Qual o id do Comprador? '))
        selecionar(2)
        id_Vendedor=str(input('Qual o id Vendedor? '))
        selecionar(3)
        id_Produto=str(input('Qual o id do produto? '))
        Valor=str(input('Qual o valor da compra? '))
        Data_conpra=str(input('Qual a data? ex: 01/01/1111 '))
        insert_query = f"INSERT INTO compra (id_compra,id_Cliente, id_Vendedor,id_Produto,Valor,Data_conpra) VALUES ('{id_compra}','{id_Cliente}',' {id_Vendedor}', '{id_Produto}','{Valor}','{Data_conpra}')"
        
    print(insert_query)
    session.execute(insert_query)
    print("Dados inseridos com sucesso! ")


def selecionar(tabela):
    if tabela==1:
        tabelaNome='Usuarios'
        select_query = f"SELECT * FROM usuario"

    elif tabela==2:
        tabelaNome='Vendedor'
        select_query = f"SELECT * FROM Vendedor"

    elif tabela==3:
        tabelaNome='Produto'
        select_query = f"SELECT * FROM produto"

    elif tabela==4:
        tabelaNome='Compra'
        select_query = f"SELECT * FROM compra"

    rows = session.execute(select_query)
    
    print(f'=========== {tabelaNome} ========= \n')
    for row in rows:
        print(row)

    print(f'\n================================')
def atualizar(tabela):
    selecionar(tabela)
    if tabela==1:
        ID_usuario=int(input('Qual o id do usuario que deseja alterar? '))
        coluna=int(input('Qual Coluna deseja atualizar? 1-Id, 2-Cpf, 3-Nome, 4-Sobrenome, 5-Email, 6-Favoritos '))
        NovoValor=str(input('Qual o novo valor? '))
        if coluna == 1:
            update_query = f"UPDATE usuario SET id = {NovoValor} WHERE id = {ID_usuario}"

        elif coluna == 2:
            update_query = f"UPDATE usuario SET cpf = '{NovoValor}' WHERE id = {ID_usuario}"

        elif coluna == 3:
            update_query = f"UPDATE usuario SET nome = '{NovoValor}' WHERE id = {ID_usuario}"

        elif coluna == 4:
            update_query = f"UPDATE usuario SET sobrenome = '{NovoValor}' WHERE id = {ID_usuario}"

        elif coluna == 5:
            update_query = f"UPDATE usuario SET email = '{NovoValor}' WHERE id = {ID_usuario}"

        elif coluna == 6:
            favoritos = []
            addFavorito = int(input("Quantos produtos adicionar aos favoritos? "))
            selecionar(3)
            for x in range(addFavorito):
                favoritos.append(str(input("Qual o Id do Produto? ")))
                favoritos.append(',')
            NovoValor = ''.join(favoritos)
            update_query = f"UPDATE usuario SET favoritos = '{NovoValor}' WHERE id = {ID_usuario}"



    elif tabela==2:
        ID_Vendedor=int(input('Qual o id do vendedor que deseja alterar? '))
        coluna=int(input('Qual Coluna deseja atualizar? 1-Id, 2-Cpf, 3-Nome, 4-Produto'))
        NovoValor=str(input('Qual o novo valor? '))
        if coluna==1:
            update_query = f"UPDATE vendedor SET id = {NovoValor} WHERE id = {ID_Vendedor}"
        
        if coluna==2:
            update_query = f"UPDATE vendedor SET cpf = '{NovoValor}' WHERE id = {ID_Vendedor}"

        if coluna==3:
            update_query = f"UPDATE vendedor SET nome = '{NovoValor}' WHERE id = {ID_Vendedor}"

        if coluna==4:
            NumeroProdutos=int(input('Quantos produtos adicionar ao vendedor?'))
            produtos=[]
            for x in range(NumeroProdutos):
                cadaProduto=[]
                Produto_Nome=str(input('Id do Produto: '))
                cadaProduto=[Produto_Nome]
                produtos.append(cadaProduto)
            todosProds=''
            cadaProduto=''
            for x in produtos:
                for y in x:
                    cadaProduto+= str(y)+','
            todosProds= todosProds + str(cadaProduto)
            NovoValor=todosProds

            update_query = f"UPDATE vendedor SET produtos = '{NovoValor}' WHERE id = {ID_Vendedor}"

    elif tabela==3:
        ID_usuario=int(input('Qual o id do produto que deseja alterar? '))
        coluna=int(input('Qual Coluna deseja atualizar? 1-Id \n 2-Nome \n 3-Preço \n 4-Descricao'))
        NovoValor=str(input('Qual o novo valor? '))
        if coluna==1:
            update_query = f"UPDATE produto SET id = {NovoValor} WHERE id = {ID_usuario}"
        
        if coluna==2:
            update_query = f"UPDATE produto SET nome = '{NovoValor}' WHERE id = {ID_usuario}"

        if coluna==3:
            update_query = f"UPDATE produto SET preco = '{NovoValor}' WHERE id = {ID_usuario}"
        
        if coluna==4:
            update_query = f"UPDATE produto SET descricao = '{NovoValor}' WHERE id = {ID_usuario}"

    elif tabela==4:
        ID_usuario=int(input('Qual o id da compra que deseja alterar? '))
        coluna=int(input('Qual Coluna deseja atualizar? 1-Id compra \n 2-Id Cliente \n 3-Id Vendedor \n 4-Id Produto \n 5-Valor \n6-Data da compra \n'))
        NovoValor=str(input('Qual o novo valor? '))
        if coluna==1:
            update_query = f"UPDATE compra SET id_compra = {NovoValor} WHERE id_compra = '{ID_usuario}'"
        
        if coluna==2:
            update_query = f"UPDATE compra SET id_Cliente = '{NovoValor}' WHERE id_compra = '{ID_usuario}'"

        if coluna==3:
            update_query = f"UPDATE compra SET id_Vendedor = '{NovoValor}' WHERE id_compra = '{ID_usuario}'"
        
        if coluna==4:
            update_query = f"UPDATE compra SET id_Produto = '{NovoValor}' WHERE id_compra = '{ID_usuario}'"        

        if coluna==5:
            update_query = f"UPDATE compra SET Valor = '{NovoValor}' WHERE id_compra = '{ID_usuario}'"  

        if coluna==6:
            update_query = f"UPDATE compra SET Data_conpra = '{NovoValor}' WHERE id_compra = '{ID_usuario}'"            


    session.execute(update_query)

    print("Data updated successfully.")

def deletar(tabela):
    if tabela==1:
        selecionar(1)
        ID_usuario=str(input('Qual o id do cliente a ser deletado'))
        delete_query = f"DELETE FROM usuario WHERE id = {ID_usuario}"

    if tabela==2:
        selecionar(2)
        ID_vendedor=str(input('Qual o id do vendedor a ser deletado'))
        delete_query = f"DELETE FROM vendedor WHERE id = {ID_vendedor}"

    if tabela==3:
        selecionar(3)
        ID_produto=str(input('Qual o id do produto a ser deletado'))
        delete_query = f"DELETE FROM produto WHERE id = {ID_produto}"

    if tabela==4:
        selecionar(4)
        ID_compra=str(input('Qual o id da compra a ser deletada'))
        delete_query = f"DELETE FROM compra WHERE id_Compra = '{ID_compra}'"

    session.execute(delete_query)

    print("Data deletada com sucesso.")


while True:
    funcao=int(input('Em qual Função deseja Realizar?  \n 1-Criar \n 2-Ler \n 3-Atualizar \n 4-Deletar \n'))
    tabela=int(input('Em qual Tabela deseja adicionar?  \n 1-Usuário \n 2-Vendedor \n 3-Produto \n 4-Compra \n'))
    if funcao==1:
        Inserir(tabela)

    elif funcao==2:
        selecionar(tabela)

    elif funcao==3:
        atualizar(tabela)

    elif funcao==4:
        deletar(tabela)

    else:
        break




# session.execute("""
# CREATE TABLE IF NOT EXISTS Compra (
#     id_Compra TEXT PRIMARY KEY,
#     id_Cliente TEXT,
#     id_Vendedor TEXT,
#     id_Produto TEXT,
#     Valor TEXT,
#     Data_conpra TEXT
# )""")
# print("Table 'Compra' created successfully")

