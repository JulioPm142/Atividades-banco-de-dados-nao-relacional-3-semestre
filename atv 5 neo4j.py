from neo4j import GraphDatabase

uri = "neo4j+s://11135e45.databases.neo4j.io"  
username = "neo4j"       
password = "ebmhDMkhrARP-TOv_aeKRsrwp3aGwPnauqo4Rv6iuaA"         

driver = GraphDatabase.driver(uri, auth=(username, password))

session = driver.session()


def create_node_usuario(nome, sobrenome, email, telefone, cep, numero):
    create_node_query = "CREATE (n:Usuario {nome: $nome, sobrenome: $sobrenome, email: $email, telefone: $telefone, cep: $cep, numero: $numero})"
    session.run(create_node_query, nome=nome, sobrenome=sobrenome, email=email, telefone=telefone, cep=cep, numero=numero)
    print("Node criado ")

def create_node_vendedor(nome, sobrenome,cpf, telefone):
    create_node_query = "CREATE (n:Vendedor {nome: $nome, sobrenome: $sobrenome, cpf: $cpf, telefone: $telefone})"
    session.run(create_node_query, nome=nome, sobrenome=sobrenome, cpf=cpf,telefone=telefone)
    print("Node criado ")

def create_node_Produto(nome ,preco, descricao):
    create_node_query = "CREATE (n:Produto {nome: $nome, preco: $preco, descricao: $descricao})"
    session.run(create_node_query,nome=nome, preco=preco, descricao=descricao)
    print("Node criado ")


def create_node_Venda(usu_id, ven_id, prod_id, quantidade, valor):
    create_node_query = "CREATE (n:Venda {usu_id: $usu_id, ven_id: $ven_id, prod_id: $prod_id, quantidade: $quantidade, valor: $valor})"
    session.run(create_node_query, usu_id=usu_id, ven_id=ven_id, prod_id=prod_id, quantidade=quantidade, valor=valor)
    print("Node criado ")


def listar_nomeUsuarios():
    query = "MATCH (n:Usuario) RETURN n"
    result = session.run(query)
    print("================ Clientes ================")
    
    for record in result:
        node = record["n"]
        nome = node["nome"]
        
        print("Nome:", nome)
        print("")

    print("==========================================")


def listar_id(entidade):
    query = f"MATCH (n:{entidade}) RETURN n"
    result = session.run(query)
    print("================ "+entidade+" ================")
    
    for record in result:
        node = record[0]  
        usuario_id = node.id
        nome = node["nome"]
        
        print("Nome:", nome," ID:", usuario_id)

        print("")

    print("==========================================")

def listar_usuarios():
    query = "MATCH (n:Usuario) RETURN n"
    result = session.run(query)
    print("================ Clientes ================")
    
    for record in result:
        node = record["n"]
        name = node["nome"]
        sobrenome = node["sobrenome"]
        email = node["email"]
        telefone = node["telefone"]
        cep = node["cep"]
        numero = node["numero"]
        
        print("Nome:", name)
        print("Sobrenome:", sobrenome)
        print("Email:", email)
        print("Telefone:", telefone)
        print("CEP:", cep)
        print("Número:", numero)
        print("")

    print("==========================================")


def listar_produto():
    query = "MATCH (n:Produto) RETURN n"
    result = session.run(query)
    print("================ Produtos ================")
    
    for record in result:
        node = record["n"]
        nome = node["nome"]
        preco = node["preco"]
        descricao = node["descricao"]
        
        print("Nome:", nome)
        print("Preço:", preco)
        print("Descrição:", descricao)
        print("")

    print("==========================================")

def listar_nomeVendedor():
    query = "MATCH (n:Vendedor) RETURN n"
    result = session.run(query)
    print("================ Vendedor ================")
    
    for record in result:
        node = record["n"]
        name = node["nome"]
        
        print("Name:", name)
        print("")

    print("==========================================")

def listar_vendedor():
    query = "MATCH (n:Vendedor) RETURN n"
    result = session.run(query)
    print("================ Vendedor ================")
    
    for record in result:
        node = record["n"]
        nome = node["nome"]
        sobrenome = node["sobrenome"]
        cpf = node["cpf"]
        telefone = node["telefone"]

        
        print("Nome:", nome)
        print("Sobrenome:", sobrenome)
        print("Telefone:", telefone)
        print("CPF:", cpf)
        print("")

    print("==========================================")

def listar_Venda():
    query = "MATCH (n:Venda) RETURN n"
    result = session.run(query)
    print("================ Vendas ================")
    
    for record in result:
        node = record["n"]

        id = node.id
        usu_id = node["usu_id"]
        prod_id = node["prod_id"]
        ven_id = node["ven_id"]
        quantidade = node["quantidade"]
        valor = node["valor"]

        print("id da Venda: ", id)
        print("id do Usuário: ", usu_id)
        print("id do Produto: ", prod_id)
        print("id do Vendedor: ", ven_id)
        print("quantidade: ", quantidade)
        print("valor: ", valor)
        print("")

    print("==========================================")


def listar_nomeProduto():
    query = "MATCH (n:Produto) RETURN n"
    result = session.run(query)
    print("================ Produtos ================")
    
    for record in result:
        node = record["n"]
        name = node["nome"]
        
        print("Name:", name)
        print("")

    print("==========================================")

def listarIdVenda():
    query = "MATCH (n:Venda) RETURN n"
    result = session.run(query)
    print("================ Vendas ================")
    
    for record in result:
        node = record[0]  
        id = node.id
        
        print("id:", id)
        print("")

    print("==========================================")  

def delete_node_Venda(node_id):
    delete_relationships_query = "MATCH (v:Venda) WHERE id(v) = $node_id MATCH (v)-[r]-() DELETE r"
    session.run(delete_relationships_query, node_id=node_id)
    delete_node_query = "MATCH (n:Venda) WHERE id(n) = $node_id DELETE n"
    session.run(delete_node_query, node_id=node_id)
    print("Venda node with id =", node_id, "deleted")


def criar_relacionamento(id_usuario, id_produto, tipo_relacionamento):
    with driver.session() as session:
        query = """
        MATCH (usuario:Usuario), (produto:Produto)
        WHERE ID(usuario) = $id_usuario AND ID(produto) = $id_produto
        CREATE (usuario)-[:%s]->(produto)
        """ % tipo_relacionamento

        session.run(query, id_usuario=id_usuario, id_produto=id_produto)

def criar_relacionamentoVenProd(nome_vendedor, id_produto, tipo_relacionamento):
    with driver.session() as session:
        query = """
        MATCH (vendedor:Vendedor), (produto:Produto)
        WHERE vendedor.nome = $nome_vendedor AND ID(produto) = $id_produto
        CREATE (vendedor)-[:%s]->(produto)
        """ % (tipo_relacionamento)

        session.run(query, nome_vendedor=nome_vendedor, id_produto=id_produto)
        print("Relação criada")


while True:
    entidade=int(input("Deseja realizar operação em qual entidade? \n 1-Usuário \n 2-Vendedor \n 3-Produto \n 4-Compra \n "))
    if entidade==1:
        funcao=funcao=int(input('Qual opção deseja utilizar? \n 1-Create \n 2-Read \n 3-Update \n 4-Delete \n 5-Relação \n'))
        if funcao == 1:
            print("adicione informações sobre o usuário:")
            nome = input('Nome: ')
            sobrenome = input('Sobrenome: ')
            email = input('Email: ')
            telefone = input('Telefone: ')
            cep = input('CEP: ')
            numero = input('Número: ')
            create_node_usuario(nome, sobrenome, email, telefone, cep, numero)
            
        
        if funcao==2:
            listar_usuarios()

        if funcao==3:

            listar_nomeUsuarios()
            print('Qual o nome do usuario que deseja alterar?')
            nome=str(input('Nome: '))

            dado = int(input('Qual opção deseja alterar? \n 1-Nome \n 2-Sobrenome \n 3-Email \n 4-Telefone \n 5-CEP \n 6-Numero \n'))

            if dado == 1:
                novo_nome = str(input('Adicone o novo nome: '))
                session.run("MATCH (n:Usuario {nome: $nome}) SET n.nome = $novo_nome", nome=nome, novo_nome=novo_nome)
            
            if dado == 2:
                novo_sobrenome = str(input('Adicione o novo sobrenome: '))
                session.run("MATCH (n:Usuario {nome: $nome}) SET n.sobrenome = $novo_sobrenome", nome=nome, novo_sobrenome=novo_sobrenome)
            
            if dado == 3:
                novo_email = str(input('adicione o novo email: '))
                session.run("MATCH (n:Usuario {nome: $nome}) SET n.email = $novo_email", nome=nome, novo_email=novo_email)
            
            if dado == 4:
                novo_telefone = str(input('adicione o novo telefone: '))
                session.run("MATCH (n:Usuario {nome: $nome}) SET n.telefone = $novo_telefone", nome=nome, novo_telefone=novo_telefone)
            
            if dado == 5:
                novo_cep = str(input('adicione o novo CEP: '))
                session.run("MATCH (n:Usuario {nome: $nome}) SET n.cep = $novo_cep", nome=nome, novo_cep=novo_cep)
            
            if dado == 6:
                novo_numero = str(input('Adicione o novo número: '))
                session.run("MATCH (n:Usuario {nome: $nome}) SET n.numero = $novo_numero", nome=nome, novo_numero=novo_numero)
        
        if funcao==4:       
            listar_nomeUsuarios()
            print('Qual o nome do usuario que deseja deletar?')
            nome=str(input('Nome: '))
            delete_relationships_query = "MATCH (u:Usuario {nome: $nome})-[r]-() DELETE r"
            session.run(delete_relationships_query, nome=nome)
            query = "MATCH (n:Usuario {nome: $nome}) DELETE n"
            session.run(query, nome=nome)
            print('usuario deletado')
    

    if entidade==2:
        funcao=int(input('Qual opção deseja utilizar? \n 1-Create \n 2-Read \n 3-Update \n 4-Delete \n 5-Criar Relação \n 6-Deletar Relações \n'))
        if funcao == 1:
            print("adicione informações sobre o Vendedor:")
            nome = input('Nome: ')
            sobrenome = input('Sobrenome: ')
            cpf = input('CPF: ')
            
            telefone = input('Telefone: ')         
            create_node_vendedor(nome, sobrenome, cpf, telefone)
            adiconarProd=input("deseja relacionar um produto a este vendedor? s/n ")
            if adiconarProd=='s':
                listar_id("Produto")
                prod_id=int(input("qual o id do produto?"))
                criar_relacionamentoVenProd(nome,prod_id,"Vende")
                print("Relação criada!")
            

        if funcao ==2:
            listar_vendedor()

        if funcao==3:
            listar_nomeVendedor()
            print('Qual o nome do Vendedor que deseja alterar?')
            nome=str(input('Nome: '))

            dado = int(input('Qual opção deseja alterar? \n 1-Nome \n 2-Sobrenome \n 3-CPF \n 4-Produto \n 5-Telefone \n '))

            if dado == 1:
                novo_nome = str(input('Adicone o novo nome: '))
                session.run("MATCH (n:Vendedor {nome: $nome}) SET n.nome = $novo_nome", nome=nome, novo_nome=novo_nome)
            
            if dado == 2:
                novo_sobrenome = str(input('Adicione o novo sobrenome: '))
                session.run("MATCH (n:Vendedor {nome: $nome}) SET n.sobrenome = $novo_sobrenome", nome=nome, novo_sobrenome=novo_sobrenome)
            
            if dado == 3:
                novo_cpf = str(input('adicione o novo CPFl: '))
                session.run("MATCH (n:Vendedor {nome: $nome}) SET n.cpf = $novo_cpf", nome=nome, novo_cpf=novo_cpf)
            
            if dado == 4:
                novo_produto = str(input('adicione o novo Produto: '))
                session.run("MATCH (n:Vendedor {nome: $nome}) SET n.produto = $novo_produto", nome=nome, novo_produto=novo_produto)
            
            if dado == 5:
                novo_telefone = str(input('adicione o novo telefone: '))
                session.run("MATCH (n:Vendedor {nome: $nome}) SET n.telefone = $novo_telefone", nome=nome, novo_telefone=novo_telefone)
            
        if funcao==4:
            listar_nomeVendedor()
            print('Qual o nome do Vendedor que deseja deletar?')
            nome=str(input('Nome: '))
            delete_relationships_query = "MATCH (v:Vendedor {nome: $nome})-[r]-() DELETE r"
            session.run(delete_relationships_query, nome=nome)
            delete_node_query = "MATCH (n:Vendedor {nome: $nome}) DELETE n"
            session.run(delete_node_query, nome=nome)
            print('Vendedor deletado')

        if funcao==5:
            listar_nomeVendedor()
            nome_vendedor = input('Qual o nome do vendedor? ')
            listar_id("Produto")
            id_produto = int(input('Qual o ID do produto? '))
            criar_relacionamentoVenProd(nome_vendedor, id_produto, "Vende")

        if funcao==6:
            listar_nomeVendedor()
            nome = input('Qual o nome do vendedor? ')
            delete_relationships_query = "MATCH (v:Vendedor {nome: $nome})-[r]-() DELETE r"
            session.run(delete_relationships_query, nome=nome) 
            print("relações deletadas")       

    if entidade==3:
        funcao=int(input('Qual opção deseja utilizar? \n 1-Create \n 2-Read \n 3-Update \n 4-Delete \n 5-Relação \n'))
        if funcao == 1:
            print("adicione informações sobre o Produto:")
            nome = input('Nome: ')
            descricao = input('Descricao: ')
            preco= input('Preço: ')
            create_node_Produto(nome, preco, descricao)
            

        if funcao ==2:
            listar_produto()

        if funcao==3:
            listar_nomeProduto()
            print('Qual o nome do Produto que deseja alterar?')
            nome=str(input('Nome: '))

            dado = int(input('Qual opção deseja alterar? \n 1-Nome \n 2-Descrição \n 3-Preço  \n '))

            if dado == 1:
                novo_nome = str(input('Adicone um novo nome: '))
                session.run("MATCH (n:Produto {nome: $nome}) SET n.nome = $novo_nome", nome=nome, novo_nome=novo_nome)
            
            if dado == 2:
                novo_desc = str(input('Adicione uma nova descrição: '))
                session.run("MATCH (n:Produto {nome: $nome}) SET n.descricao = $novo_desc", nome=nome, novo_desc=novo_desc)
            
            if dado == 3:
                novo_preco = str(input('adicione um novo Preço: '))
                session.run("MATCH (n:Produto {nome: $nome}) SET n.preco = $novo_preco", nome=nome, novo_preco=novo_preco)            
            
        if funcao==4:
            listar_nomeProduto()
            print('Qual o nome do Produto que deseja deletar?')
            nome=str(input('Nome: '))

            delete_relationships_query = "MATCH (p:Produto {nome: $nome})-[r]-() DELETE r"
            session.run(delete_relationships_query, nome=nome) 
                      
            query = "MATCH (n:Produto {nome: $nome}) DELETE n"
            session.run(query, nome=nome)
            print('Produto deletado')            


    if entidade==4:
        funcao=int(input('Qual opção deseja utilizar? \n 1-Create \n 2-Read \n 3-Delete \n'))
        if funcao == 1:
            listar_id("Usuario")
            usu_id = int(input("Qual o id do usuário que está realizando a compra? "))
            listar_id("Vendedor")
            ven_id = int(input("Qual o id do Vendedor que está realizando a venda? "))
            listar_id("Produto")
            prod_id = int(input("Qual o id do Produto que deseja comprar? "))

            quantidade = int(input("Quantidade de itens: "))
            valor = float(input("Valor comprado: "))

            id_usuario = usu_id
            id_produto = prod_id
            tipo_relacionamento = "COMPRA"

            create_node_Venda(usu_id, ven_id, prod_id, quantidade, valor)
            criar_relacionamento(id_usuario, id_produto, tipo_relacionamento)

            
            

        if funcao ==2:
            listar_Venda()       
            
        if funcao == 3:
            listar_Venda()

            venda_id = int(input('Qual o id da venda que deseja deletar?'))

            delete_node_Venda(venda_id)





