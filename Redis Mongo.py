import pymongo
import redis
import json
import ast
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://juliopm:07062004@teste.zxwczlg.mongodb.net/?retryWrites=true&w=majority")
db = client.test

global mydb
mydb = client.Biblioteca
# !Er07062004

r = redis.Redis(
  host='redis-14788.c261.us-east-1-4.ec2.cloud.redislabs.com',
  port=14788,
  password='ky13qMTPa5bEXOZH7dR391koVR6pqAf5')


def findSortUser():
    #sort
    global mydb
    mycol = mydb.Usuario
    print("\n####SORT####")
    mydoc=mycol.find().sort("nome")
    dados=[]
    for x in mydoc:
        print(x)
        dados.append(x)
    return dados



def insertUser(cpf,nome,sobrenome,endereco,telefone):
    #inser
    global mydb
    mycol=mydb.Usuario
    print("\n####INSERT####")
    mydict = { "CPF":cpf,"Nome":nome,"Sobrenome":sobrenome,"Endereco":endereco,"Telefone":telefone}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def deleteUser(nome,cpf):
    #delete
    global mydb
    mycol=mydb.Usuario
    print("\n####Delete####")
    mydict = { "Nome":nome,"CPF":cpf}
    mycol.delete_one(mydict)

def updateUser(cpf,escolhaUpdate,NovoValor):
    #update
    global mydb
    mycol=mydb.Usuario
    print("\n####Update####")
    mydict = { "CPF":cpf }

    if escolhaUpdate==1:   
        newvalues = { "$set": { "CPF":NovoValor } }
        
    elif escolhaUpdate==2:   
        newvalues = { "$set": { "Nome":NovoValor } }

    elif escolhaUpdate==3:   
        newvalues = { "$set": { "Sobrenome":NovoValor } }
        
    elif escolhaUpdate==4:   
        newvalues = { "$set": { "Endereco":NovoValor } }
        
    elif escolhaUpdate==5:   
        newvalues = { "$set": { "Telefone":NovoValor } }


    mycol.update_one(mydict, newvalues)



def findSortLivro():
    #sort
    global mydb
    mycol = mydb.Livro
    print("\n####SORT####")
    mydoc=mycol.find().sort("nome")
    for x in mydoc:
        print(x)

def insertLivro(nome,descricao,autor):
    #inser
    global mydb
    mycol=mydb.Livro
    print("\n####INSERT####")
    mydict = { "Nome":nome,"Descricao":descricao,"Autor":autor}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def deleteLivro(nome):
    #delete
    global mydb
    mycol=mydb.Livro
    print("\n####Delete####")
    mydict = { "Nome":nome}
    mycol.delete_one(mydict)

def updateLivro(titulo,escolhaUpdate,NovoValor):
    #update
    global mydb
    mycol=mydb.Livro
    print("\n####Update####")
    mydict = { "Nome":titulo}


    if escolhaUpdate==1:   
        newvalues = { "$set": { "Nome":NovoValor } }
        
    elif escolhaUpdate==2:   
        newvalues = { "$set": { "Descricao":NovoValor } }

    elif escolhaUpdate==3:  
        
        Anome=str(input(" Novo nome do Autor: "))
        Asobrenome=str(input(" Novo sobrenome do Autor: ")) 
        novoAutor={"Nome":Anome,"SobreNome":Asobrenome}

        newvalues = { "$set": { "Autor":novoAutor } }

    mycol.update_one(mydict, newvalues)
        


def findSortAutor():
    #sort
    global mydb
    mycol = mydb.Autor
    print("\n####SORT####")
    mydoc=mycol.find().sort("nome")
    for x in mydoc:
        print(x)
    return mydoc

def insertAutor(nome,sobrenome,livros):
    #inser
    global mydb
    mycol=mydb.Autor
    print("\n####INSERT####")
    mydict = { "Nome":nome,"Sobrenome":sobrenome,"Livros":livros}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def deleteAutor(nome):
    #delete
    global mydb
    mycol=mydb.Autor
    print("\n####Delete####")
    mydict = { "Nome":nome}
    mycol.delete_one(mydict)

def updateAutor(titulo,escolhaUpdate,NovoValor):
    #update
    global mydb
    mycol=mydb.Livro
    print("\n####Update####")
    mydict = { "Nome":titulo}

    if escolhaUpdate==1:   
        newvalues = { "$set": { "Nome":NovoValor } }
        
    elif escolhaUpdate==2:   
        newvalues = { "$set": { "Descricao":NovoValor } }

    elif escolhaUpdate==3:  
        
        Anome=str(input(" Novo nome do Autor: "))
        Asobrenome=str(input(" Novo sobrenome do Autor: ")) 
        novoAutor={"Nome":Anome,"SobreNome":Asobrenome}

        newvalues = { "$set": { "Autor":novoAutor } }
        
    mycol.update_one(mydict, newvalues)

def findAutor(nome):
    global db
    mycol=mydb.Autor
    a = mycol.find_one({"Nome":nome})
    return a


def SincRedisMongo(id,cpf,nome,sobrenome,endereco,telefone):
    #update
    print(id)
    mycol = mydb['Usuario']
    print("\n#### Update ####")
    mydict = { "_id": ObjectId(id) }
    newvalues = {'$set': {'CPF': cpf, 'Nome': nome, 'Sobrenome': sobrenome, 'Endereco': endereco, 'Telefone': telefone}}

    mycol.update_one(mydict, newvalues)

while True:
    escolhaBanco=str(input("Utilizar 1-Mongo 2-Redis "))
    if escolhaBanco=='1':
        while True:
            escolha=int(input('Escola uma opcao: \n 1-Usuario \n 2-Livro  \n 3-Autor \n '))

            if escolha == 1:
                escolha2=int(input('Escola uma opcao: \n 1-Visualizar \n 2-Adicionar \n 3-Deletar \n 4-Atualizar \n '))
                if escolha2 == 1:
                    findSortUser()

                if escolha2 == 2:
                    cpf=str(input('insira o cpf: '))
                    nome=str(input('insira o nome: '))
                    sobrenome=str(input('insira o sobrenome: '))
                    endereco=str(input('insira o endereco: '))
                    telefone=str(input('insira o telefone: '))
                    insertUser(cpf,nome,sobrenome,endereco,telefone)
                if escolha2== 3:
                    findSortUser()
                    nome=str(input('insira o nome: '))
                    cpf=str(input('insira o cpf: '))
                    deleteUser(nome,cpf)

                if escolha2 == 4:     
                    escolhaUpdate=int(input("Escola uma opcao: \n 1-CPF \n 2-Nome \n 3-Sobrenome \n 4-Endereco \n 5-Telefone \n"))
                    cpf=str(input("Adicione o CPF do Usuário que será atualizado: "))
                    NovoValor=str(input('Novo valor: '))

                    updateUser(cpf,escolhaUpdate,NovoValor)
            
            elif escolha == 2: 
                escolha2=int(input('Escola uma opcao: \n 1-Visualizar \n 2-Adicionar \n 3-Deletar \n 4-Atualizar \n '))
                if escolha2 == 1:
                    findSortLivro()

                if escolha2 == 2:
                    nome=str(input('insira o título do livro: '))
                    descricao=str(input('insira a descrição: '))
                    AutorExiste=str(input("O Autor já existe ?  \n 1-Sim 2-Não \n"))

                    def pegaDados():
                        a=findSortAutor()
                        for x in a:
                            print(a["Nome"])
                        
                        nome=str(input("Qual o nome do Autor? "))
                        b=findAutor(nome)
                        print(b["_id"])
                        return b


                    if AutorExiste == '1':
                        autor=pegaDados()
                        Lautor={"_id":autor["_id"],"Nome":autor["Nome"],"Sobrenome":autor["Sobrenome"]}
                        
                        
                    else:
                        Anome = str(input("Nome do Autor: "))
                        Asobrenome= str(input("Sobrenome do Autor: "))
                        autor={"Nome":Anome,"Sobrenome":Asobrenome}
                        livros=''
                        insertAutor(Anome,Asobrenome,livros)
                        autor=pegaDados()
                        Lautor={"_id":autor["_id"],"Nome":autor["Nome"],"Sobrenome":autor["Sobrenome"]}
                    autor=Lautor
                    insertLivro(nome,descricao,autor)

                if escolha2== 3:
                    findSortLivro()
                    nome=str(input("Título do Livro: "))        
                    deleteLivro(nome)

                if escolha2 == 4:
                    escolhaUpdate=int(input("Escola uma opcao para alterar: \n 1-Título \n 2-Descrição \n 3-Autor \n"))
                    findSortLivro()
                    titulo=str(input("Qual o titulo do livro que deve ser alterado? "))
                    NovoValor=str(input("Qual o novo valor? "))

                    updateLivro(titulo,escolhaUpdate,NovoValor)
            
            elif escolha == 3: 
                escolha2=int(input('Escola uma opcao: \n 1-Visualizar \n 2-Adicionar \n 3-Deletar \n 4-Atualizar \n '))
                if escolha2 == 1:
                    findSortAutor()

                if escolha2 == 2:
                    nome=str(input('insira o título do livro: '))
                    sobrenome=str(input('insira a descrição: '))
                    quantLivro=int(input("Quantos livros o Autor escreveu?"))
                    livros=[]
                    for x in range(quantLivro):
                        Lnome = str(input("Nome do livro: "))
                        Ldescricao= str(input("Sobrenome do Autor: "))
                        livroDic={"nome":Lnome,"descricao":Ldescricao}
                        livros.append(livroDic)

                    insertAutor(nome,sobrenome,livros)

                if escolha2== 3:
                    findSortLivro()
                    nome=str(input("Título do Livro"))        
                    deleteAutor(nome)

                if escolha2 == 4:
                    escolhaUpdate=int(input("Escola uma opcao para alterar: \n 1-Nome \n 2-Sobrenome \n 3-Livro \n"))
                    findSortAutor()
                    nome=str(input("Qual o nome do autor que deve ser alterado? "))

                    if escolhaUpdate==3:
                        quantLivro=int(input("Quantos livros substituir? "))
                        livros=[]
                        for x in range(quantLivro):
                            Lnome = str(input("Nome do livro: "))
                            Ldescricao= str(input("Descrição do livro"))
                            livroDic={"nome":Lnome,"descricao":Ldescricao}
                            livros.append(livroDic)
                        NovoValor=livros
                    else:
                        NovoValor=str(input("Qual o novo valor? "))

                    updateAutor(nome,escolhaUpdate,NovoValor)




    def login():
            loginName=str(input("Usuario: "))
            loginPass=str(input("Senha: "))
            r.set('Name',loginName)
            r.expire('Name',100)
            r.set('Pass',loginPass)
            r.expire('Pass',100)


    if escolhaBanco=='2':
        while True:
            Nome=r.get('Name')
            Nome=str(Nome)  
            if Nome=='None':
                login()


            if Nome!="None":
                escolhaRedis=str(input('Qual função deseja realizar? \n 1-Logar, \n 2-sincronizar Mongo -> Redis, \n 3-Sincronizar Redis -> Mongo \n 4-Editar \n 5=Listar'))
                print('Você está na opção de Usuários')
                BancoRedis=r.get('Usuario')
                convetedRedis=BancoRedis.decode('utf-8')
                convetedRedis = convetedRedis.replace("ObjectId(", "").replace(")", "")
                convetedRedis = ast.literal_eval(convetedRedis)
                if escolhaRedis=="1":
                    login()
                    
                elif escolhaRedis=="2":
                    print("Banco Mongo:")
                    a=findSortUser()
                    a = str(a)
                    r.set('Usuario',a)
                    BancoRedis=r.get('Usuario')
                    print("Banco Redis: ")
                    print(BancoRedis)
                    print("BANCO SINCRONIZADO")
                    break
                

                elif escolhaRedis=="3":
                    Json=convetedRedis
                    print(Json)
                    for x in Json:
                        id=x["_id"]
                        cpf=x["CPF"]
                        nome=x["Nome"]
                        sobrenome=x["Sobrenome"]
                        endereco=x["Endereco"]
                        telefone=x["Telefone"]

                        SincRedisMongo(id,cpf,nome,sobrenome,endereco,telefone)
                    break

                    # BancoRedis=r.get('Usuario')
                    # DicBanco=BancoRedis.decode('utf-8')
                    # a=str(DicBanco).split("},")
                    # novoDic=[]
                    # count=0
                    # count2=0
                    # for x in a:
                    #     count+=1
                    #     if count!=len(a):
                    #         x=x+'}'
                    #     novoDic.append(x)
                        
                    # for x in novoDic:
                    #     count2+=1
                    #     x=x[1:-1]
                    #     x=x.replace("'", "\"")
                    #     if count2!=len(novoDic):
                    #         x=x+'}'
                    #     print(x,'\n')

                    #     x=x[x.index(',')+2:]
                    #     x='{'+x
                    #     print('x',x)

                    #     xJson=json.loads(x)
                    #     print('json',xJson)


                elif escolhaRedis=="4":
                    print("========================================")
                    print("Usuários: ")
                    for x in convetedRedis:
                        
                        print("Nome:",x["Nome"])
                    print("========================================")
                    editNome=str(input("Qual o nome do Usuário a ser editado? "))
                    for x in convetedRedis:
                        if x["Nome"]==editNome:
                            atributo=str(input("Qual dado alterar? 1-CPF, 2-Nome, 3-Sobrenome, 4-Endereco, 5-Telefone "))
                            opcoes = {
                                '1': 'CPF',
                                '2': 'Nome',
                                '3': 'Sobrenome',
                                '4': 'Endereco',
                                '5': 'Telefone'
                            }
                            if atributo in opcoes:
                                atributo = opcoes[atributo]
                            else:
                                print("Opção inválida!")
                            
                            x[f"{atributo}"] = str(input("Qual o novo valor? "))

                    print(convetedRedis)
                    r.set('Usuario',str(convetedRedis))
                    break

                elif escolhaRedis=='5':
                    print("===============Usuários=================")
                    for x in convetedRedis:
                        
                        print("Id:",x["_id"])
                        print("Nome:",x["Nome"])
                        print("CPF:", x["CPF"])
                        print("Sobrenome:", x["Sobrenome"])
                        print("Endereco:", x["Endereco"])
                        print("Telefone:", x["Telefone"])
                        print('')
                    print("========================================")

                    break

                            




                    





            
            


                



                



