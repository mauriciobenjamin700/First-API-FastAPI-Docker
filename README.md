# Meu Primeiro Projeto Construindo uma API com Python na DIO

Para executar a API, tenha o [Python 3.12](https://www.python.org/downloads/) ou superior instalado em sua maquina.

Instale o [Poetry](https://python-poetry.org/docs/#installation) para Gerenciar os Pacotes e Dependências.

## Subindo o Servidor

Passos para Subir o Servidor manual:

- Abra o Terminal
- digite `uvicorn api.main:app --reload`

Passos para Subir o Servidor usando [MakeFile](MakeFile):

- Abra o Terminal
- Suba o banco de dados usando `make start-db`
- Ìnicie a API usando `make run`
- Crie as migrações do banco de dados com `make create-migrations d="init_db"`
- execute as migrações com `make create-migrations d="init_db"`

## Acessando o Banco de Dados

Eu uso o dbeaver, mas ferramentas como [pgadmin](https://www.pgadmin.org/download/) são uma opção valida também.

Dados de acesso:

- host: `localhost`
- port: `5432`
- database: `workout`
- user: `workout`
- password: `workout`

## Ideias Abandonadas

Passos para Subir o Servidor usando PowerShell

- Abra o Terminal
- execute `.\run.ps1 -task server`

Resolver problemas e ir pra aula 7
