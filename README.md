# Comics (Django)
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/-Django-092E20?style=flat&logo=django&logoColor=white)
![Django REST framework](https://img.shields.io/badge/-Django%20REST%20framework-ff9900?style=flat&logo=django&logoColor=white)

## Описание проекта
Данные проект является тестовым заданием. 
На сайте комиксов реализована система оценки и отображения рейтинга для каждого комикса. 
Рейтинг основан на средней оценке, которую пользователи могут ставить комиксам от 1 до 5. 
Рейтинг обновляется в реальном времени.
***
### Запуск проекта
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/iNTENSY/test_comics.git
```
```
cd .\comics\django\
```

Cоздать и активировать виртуальное окружение
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
Перейти в папку со скриптом управления и выполнить миграции
```
cd core
```
```
python manage.py migrate
```

- Запустить проект
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
***

### Над проектом работал
[Дмитрий Даценко](https://github.com/iNTENSY)
