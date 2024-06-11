# Alembic

O Alembic será usado para manipulação da estrutura do banco de dados.

## Como esta pasta foi criada?

```bash
alembic init alembic
```

## Configurações essênciais

No arquivo [alembic.ini](../alembic.ini) Iremos modificar

- `sqlalchemy.url = driver://user:pass@localhost/dbname` para ficar assim
- `sqlalchemy.url = postgresql+asyncpg://workout:workout@localhost/workout` de forma que o banco trabalhe de forma assincrona
