# Meu Primeiro Projeto Construindo uma API com Python na DIO

## Subindo o Servidor

Passos para Subir o Servidor no Braçp:

- Abra o Terminal
- digite `uvicorn api.main:app --reload`

Passos para Subir o Servidor usando [MakeFile](MakeFile):

- Abra o Terminal
- digite `make run`
- Crie as migrações do banco de dados com `make create-migrations d="init_db"`

Passos para Subir o Servidor usando PowerShell

- Abra o Terminal
- digite `.\run.ps1 -task server`
- TODO: Terminar a aula 6 aos 20:55