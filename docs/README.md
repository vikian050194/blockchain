Основы технологии блокчейн. Заметки к практическим занятиям.

Для запуска примеров и сборки документации нужны пакеты и виртуальное окружение

```bash
virtualenv venv
```

Для примеров необходимо два пакета

```bash
pip install -r requirements.txt
```

Для сборки документации используется mkdocs ([github][github-mkdocs-url], [site][site-mkdocs-url])

```bash
pip install -r requirements-docs.txt
```

Запускаем из корневой директории

```bash
mkdocs serve
```

[github-mkdocs-url]: https://github.com/mkdocs/mkdocs/
[site-mkdocs-url]: https://www.mkdocs.org/
