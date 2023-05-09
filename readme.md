# Pet django project
Project to practice django, drf.

## Usage (Linux or Mac)

```bash
docker-compose up
```

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
``` 

```python
celery -A django_with_mypy worker -l INFO
```

```python
python manage.py migrate
```

```python
python manage.py loaddata data.json
```

```python
python manage.py createsuperuser
```

```python
python manage.py runserver
```


## License

[MIT](https://choosealicense.com/licenses/mit/)
