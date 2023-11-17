lint:
	python3 -m isort app && python3 -m black app
runserver:
	cd app && python3 manage.py runserver
