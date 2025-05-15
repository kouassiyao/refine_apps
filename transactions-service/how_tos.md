## Database migrations with Alembic

## Alembic init
Initialize a new alembic scripts directory

```sh
poetry run alembic init alembic
```

### Create a new revision:
After modifying the models run following command (before that make sure the target_metadata is set to Base metadata)
```sh
poetry run alembic revision --autogenerate -m "create vendors table"
```

### Apply some db migrations
Apply all migrations scripts from current alembic version to head
```sh
poetry run alembic upgrade head
```