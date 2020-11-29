## Storage

Создадим виртуальное окружение
```
virtualenv -p python3.8.5 venv
```
После этого в директории проекта должна появиться директория `venv`.

Активируем её и установим необходимые пакеты
```
source venv/bin/activate
pip install -r requirements.txt
```