---
## Setup bot

1. Clone this repository

2. Change the name of `.env.dist` to `.env` and set all environment variables as you need

3. Change password for redis in build/redis.conf (`requirepass` and `masterauth`). Set same password in `.env` 
   (`REDIS_PASSWORD`).

4. Change project name and other information in `pyproject.toml`

5. `make project-start` to start project with docker-compose or `make help` if you want to know more about make commands

---
## Development

If you want to lint your code: \
```make lint``` \
This will start isort, blue and ruff to src and tests folders

You can manually run any instrument by: \
`make ruff`, `make blue` or `make isort`

### Migrations
`make generate NAME=<name>` \
Generate alembic revision for migration with given name

`make migrate` \
Apply migrations to the target database
