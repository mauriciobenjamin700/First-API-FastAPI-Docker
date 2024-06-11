# script.ps1

# Menu para chamar as funções
param (
    [Parameter(Mandatory=$true)]
    [ValidateSet("server", "create-migrations", "migrations")]
    [string]$task,
    
    [string]$migrationMessage
)

# Função para rodar o servidor Uvicorn
function Run-Server {
    uvicorn api.main:app --reload
}

# Função para criar migrações
function Create-Migrations {
    param (
        [string]$d
    )
    $env:PYTHONPATH = "$env:PYTHONPATH;$PWD"
    alembic revision --autogenerate -m $d
}

# Função para rodar migrações
function Run-Migrations {
    $env:PYTHONPATH = "$env:PYTHONPATH;$PWD"
    alembic upgrade head
}

switch ($task) {
    "server" {
        Run-Server
    }
    "create-migrations" {
        if ($migrationMessage) {
            Create-Migrations -d $migrationMessage
        } else {
            Write-Host "Por favor, forneça uma mensagem para a migração usando o parâmetro -migrationMessage."
        }
    }
    "migrations" {
        Run-Migrations
    }
}
