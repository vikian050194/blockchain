Основы технологии блокчейн. Заметки к практическим занятиям.

Для запуска примеров и сборки документации нужны пакеты и виртуальное окружение

```bash
virtualenv venv
```

Для примеров необходимо два пакета

```bash
pip install py-solc-x==1.1.0 web3[tester]==5.24.0
```

Для сборки документации используется mkdocs ([github][github-mkdocs-url], [site][site-mkdocs-url])

```bash
pip install mkdocs==1.2.2 mkdocs-material==7.3.3
```

Запускаем из корневой директории

```bash
mkdocs serve
```

[github-mkdocs-url]: https://github.com/mkdocs/mkdocs/
[site-mkdocs-url]: https://www.mkdocs.org/
