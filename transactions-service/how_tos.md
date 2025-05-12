## Database migrations with Alembic

## Alembic init
Initialize a new alembic scripts directory

```sh
poetry run alembic init alembic
```

### Create a new revision:
```sh
poetry run alembic revision -m "create account table"
```