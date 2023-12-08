
### Запуск проекта
Клонируйте репозиторий и перейдите в него в командной строке
```
git clone https://github.com/iNTENSY/test_comics.git
```
```
cd .\comics\django\
```
Cоздайте и активируйте виртуальное окружение
```
python3 -m venv venv # Для Linux и macOS
python -m venv venv # Для Windows
```
```
venv/Scripts/activate # Для Windows
source venv/bin/activate # Для Linux и macOS
```
Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
Перейдите в папку со скриптом управления и выполните миграции
```
cd core
python manage.py migrate
```
Запустить проект
```
python manage.py runserver
```

### Запуск тестов

В проекте имеются тесты, чтобы запустить их напишите в командную строку:
```python
pytest
```
***
## Полная документация к API проекта:

Перечень запросов к ресурсу можно посмотреть в описании API

```
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
```