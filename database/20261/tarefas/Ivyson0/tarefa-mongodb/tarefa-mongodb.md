# Resumo sobre MongoDB

O MongoDB é um Sistema Gerenciador de Banco de Dados NoSQL orientado a documentos. Diferente dos bancos relacionais tradicionais, ele utiliza documentos no formato BSON/JSON para armazenar dados de forma flexível e dinâmica.

Principais características do MongoDB:

* Modelo orientado a documentos;
* Estrutura flexível sem esquema rígido;
* Alta escalabilidade;
* Suporte a replicação e alta disponibilidade;
* Integração simples com aplicações modernas;
* Armazenamento em coleções e documentos.

Nesta atividade foi utilizada a linguagem Python juntamente com a biblioteca PyMongo para realizar a comunicação com o banco de dados.

---

# Configuração do MongoDB com Docker

Foi utilizado Docker para executar o servidor MongoDB localmente.

Imagem utilizada:

```bash
mongo
```

Porta configurada:

```text
27017
```

Usuário criado:

```text
Usuário: ivyson0
Senha: 12345
```

Banco criado:

```text
AtividadesProj
```

---

# Estrutura das Coleções

O sistema foi modelado utilizando as seguintes coleções:

## empregados

Armazena os dados dos empregados do departamento.

Campos principais:

* nome
* cargo
* idade
* salario

## projetos

Armazena os projetos cadastrados.

Campos principais:

* nome
* lider
* prazo_meses
* orcamento

## atividades

Armazena as atividades vinculadas aos projetos.

Campos principais:

* titulo
* status
* horas
* projeto

---

# Script de Inicialização

Arquivo:

```text
tarefa_mongo/init_mongo.py
```

O script realiza:

* conexão com MongoDB;
* criação das coleções;
* inserção de dados iniciais;
* limpeza de dados antigos.

---

# Programa CRUD

Arquivo:

```text
tarefa_mongo/crud_mongo.py
```

O programa foi desenvolvido em Python utilizando a biblioteca PyMongo para realizar operações CRUD no banco MongoDB.

Operações implementadas:

* Create: inserção de uma nova atividade em um projeto;
* Read: listagem dos projetos e suas atividades;
* Update: atualização do líder de um projeto;
* Delete: remoção de uma atividade cadastrada.

---

# Replica Sets no MongoDB

Replica Set é um conjunto de servidores MongoDB utilizado para garantir alta disponibilidade e tolerância a falhas através da replicação de dados.

Os principais membros de um Replica Set são:

* Primary: servidor principal que recebe operações de escrita;
* Secondary: mantém cópias atualizadas dos dados do primário;
* Arbiter: participa das votações, mas não armazena dados.

---

# Configuração de Replica Set com Docker

Para transformar o MongoDB em um Replica Set de três membros é necessário:

1. Criar múltiplos containers MongoDB;
2. Utilizar o parâmetro `--replSet`;
3. Inicializar o Replica Set no mongo shell.

Exemplo:

```bash
docker run -d --name mongo1 mongo --replSet rs0

docker run -d --name mongo2 mongo --replSet rs0

docker run -d --name mongo3 mongo --replSet rs0
```

Inicialização:

```javascript
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017" },
    { _id: 1, host: "mongo2:27017" },
    { _id: 2, host: "mongo3:27017", arbiterOnly: true }
  ]
})
```

