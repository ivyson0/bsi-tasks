from pymongo import MongoClient

# conexão com MongoDB

client = MongoClient(
    "mongodb://ivyson0:12345@localhost:27017/admin"
)

# banco de dados

db = client["gerenciamento_projetos"]

# coleções

projetos = db["projetos"]
atividades = db["atividades"]

# =========================================
# CREATE
# Inserir nova atividade
# =========================================

nova_atividade = {
    "titulo": "Documentação do Sistema",
    "status": "Pendente",
    "horas": 15,
    "projeto": "Sistema Escolar"
}

atividades.insert_one(nova_atividade)

print("CREATE realizado com sucesso!")

# =========================================
# READ
# Listar projetos e atividades
# =========================================

print("\nProjetos cadastrados:\n")

for projeto in projetos.find():

    print(f"Projeto: {projeto['nome']}")

    atividades_projeto = atividades.find({
        "projeto": projeto["nome"]
    })

    for atividade in atividades_projeto:
        print(
            f" - {atividade['titulo']} "
            f"({atividade['status']})"
        )

# =========================================
# UPDATE
# Atualizar líder de projeto
# =========================================

projetos.update_one(
    {"nome": "Sistema Escolar"},
    {"$set": {"lider": "Maria Oliveira"}}
)

print("\nUPDATE realizado com sucesso!")

# =========================================
# DELETE
# Remover atividade
# =========================================

atividades.delete_one(
    {"titulo": "Testes do Sistema"}
)

print("DELETE realizado com sucesso!")