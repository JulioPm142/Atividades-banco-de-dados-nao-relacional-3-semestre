import pymongo

client = pymongo.MongoClient("mongodb+srv://juliopm:****@teste.zxwczlg.mongodb.net/?retryWrites=true&w=majority")
db = client.test

##print(db)

global mydb
mydb = client.mercadolivre

def findSortUser():
    #sort
    global mydb
    mycol = mydb.Usuario
    print("\n####SORT####")
    mydoc=mycol.find().sort("nome")
    for x in mydoc:
        print(x)

def findUserEndereco(cpf):
    global mydb
    mycol=mydb["Usuario"]
    myquery={"CPF":cpf}
    TodosEnderecos=mycol.find(myquery)
    
    return TodosEnderecos


def insertUser(nome,cpf,sobrenome,Email,endereco):
    #inser
    global mydb
    mycol=mydb.Usuario
    print("\n####INSERT####")
    mydict = { "Nome":nome,"Sobrenome":sobrenome,"Email":Email,"CPF":cpf,"Endereco":endereco,"Favortios":[]}
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
        newvalues = { "$set": { "Nome":NovoValor } }
        
    elif escolhaUpdate==2:   
        newvalues = { "$set": { "Sobrenome":NovoValor } }

    elif escolhaUpdate==3:   
        newvalues = { "$set": { "Email":NovoValor } }
        
    elif escolhaUpdate==4:   
        newvalues = { "$set": { "CPF":NovoValor } }
        
    elif escolhaUpdate==5:   
        newvalues = { "$set": { "Endereco":NovoValor } }

    elif escolhaUpdate==6:   
        newvalues = { "$set": { "Favoritos":NovoValor } }

    mycol.update_one(mydict, newvalues)


while True:
    escolha=int(input('Escola uma opcao: \n 1-Visualizar \n 2-Adicionar \n 3-Deletar \n 4-Atualizar \n '))
    if escolha == 1:
        findSortUser()

    elif escolha == 2:
        nome=str(input('Nome do Usuário: '))
        sobrenome=str(input('Sobrenome do Usuário: '))
        Email=str(input('Email do Usuário: '))
        cpf=str(input('Cpf do Usuário: '))
        Endereco=[]
        NumEnderecos=int(input('Quantos endereços deseja adicionar?: '))
        for x in range(NumEnderecos):
            x+=1
            estado=str(input('Adicione o ' + str(x) +'º Estado: '))
            cidade=str(input('Adicione a ' +str(x)+'º Cidade: '))
            bairro=str(input('Adicione o ' +str(x)+'º Bairro: '))
            rua=str(input('Adicione a ' +str(x)+'º Rua: '))
            numero=str(input('Adicione o ' +str(x)+'º Número: '))
            DicionarioEndereco={"Estado": estado,"Cidade": cidade,"Bairro": bairro,"Rua": rua,"Numero": numero}
            Endereco.append(DicionarioEndereco)
            x-=1
            
            
        insertUser(nome,cpf,sobrenome,Email,Endereco)
        
    elif escolha == 3:
        nome=str(input('Nome do Usuário: '))
        cpf=str(input('Cpf do Usuário: '))
        deleteUser(nome,cpf)

    elif escolha == 4:
        cpf=str(input('Cpf atual do Usuário: '))
          
        escolha2=int(input('o que deve ser alterado? \n 1-Nome \n 2-Sobrenome \n 3-Email \n 4-Cpf: \n 5-Endereco \n 6-'))
        if escolha2==1:
            NovoValor=str(input('Novo nome do Usuário: '))
            
        elif escolha2==2:
            NovoValor=str(input('Novo Sobrenome do Usuário: '))
            
        elif escolha2==3:
            NovoValor=str(input('Novo Email do Usuário: '))          

        elif escolha2==4:
            NovoValor=str(input('Novo Cpf do Usuário: '))
            updateUser(cpf,escolha2,NovoValor)

        if escolha2==5:
            Listaenderecos=[]
            enderecos=findUserEndereco(cpf)
            for x in enderecos:
                a=x["Endereco"]
                print(a)
                for y in a:
                    Listaenderecos.append(y)

            escolhaEndereco=int(input('Qual endereço deseja alterar? 1º-1, 2º-2 etc...'))
            escolhaEndereco-=1

            Nestado=str(input('Adicione o Estado: '))
            Ncidade=str(input('Adicione a Cidade: '))
            Nbairro=str(input('Adicione o Bairro: '))
            Nrua=str(input('Adicione a Rua: '))
            Nnumero=str(input('Adicione o Número: '))
            NDicionarioEndereco={"Estado": Nestado,"Cidade": Ncidade,"Bairro": Nbairro,"Rua": Nrua,"Numero": Nnumero}
            
            Listaenderecos.pop(escolhaEndereco)
            Listaenderecos.append(NDicionarioEndereco)
            updateUser(cpf,5,Listaenderecos)



        



