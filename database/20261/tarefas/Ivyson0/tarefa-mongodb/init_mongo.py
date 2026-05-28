# init_mongo.py

from pymongo import MongoClient

# conexão com MongoDB

client = MongoClient(
"mongodb://ivyson0:12345@localhost:27017/admin"
)

# banco de dados

db = client["gerenciamento_projetos"]

# coleções

empregados = db["empregados"]
projetos = db["projetos"]
atividades = db["atividades"]

# limpar dados antigos

empregados.delete_many({})
projetos.delete_many({})
atividades.delete_many({})

# =========================

# EMPREGADOS

# =========================

empregados_docs = [
{
"nome": "Ivyson Wanderson",
"cargo": "Desenvolvedor",
"idade": 22,
"salario": 4500
},

{
"nome": "João Silva",
"cargo": "Gerente",
"idade": 35,
"salario": 7000
},

{
"nome": "Maria Oliveira",
"cargo": "Analista",
"idade": 30,
"salario": 5200
}
]

empregados.insert_many(empregados_docs)

# =========================

# PROJETOS

# =========================

projetos_docs = [
{
"nome": "Sistema Escolar",
"lider": "João Silva",
"prazo_meses": 6,
"orcamento": 50000
},

{
"nome": "App Delivery",
"lider": "Ivyson Wanderson",
"prazo_meses": 4,
"orcamento": 30000
},

{
"nome": "Portal RH",
"lider": "Maria Oliveira",
"prazo_meses": 8,
"orcamento": 75000
}
]

projetos.insert_many(projetos_docs)

# =========================

# ATIVIDADES

# =========================

atividades_docs = [
{
"titulo": "Modelagem Banco de Dados",
"status": "Em andamento",
"horas": 12,
"projeto": "Sistema Escolar"
},

{
"titulo": "Implementar API",
"status": "Pendente",
"horas": 20,
"projeto": "App Delivery"
},

{
"titulo": "Testes do Sistema",
"status": "Concluída",
"horas": 10,
"projeto": "Portal RH"
}
]

atividades.insert_many(atividades_docs)

print("Banco inicializado com sucesso!")
