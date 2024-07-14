run:
	@uvicorn api.main:app --reload 

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(msg)

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head

start-db:
	@poetry shell
	@docker-compose up --build -d