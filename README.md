# books-dl

Консольная утилита для загрузки книжек с [одного замечательного сайта](http://213.5.52.16/).

## Установка

```sh
pip install books-dl
```

## Использование

```
usage: books_dl [-h] [-i ID книги] [-d Директория] [-nc] [-l] [--max-file-name-length Длина] [Запрос ...]

Консольная утилита для загрузки книжек с одного замечательного сайта.

positional arguments:
  Запрос                Запрос для поиска

options:
  -h, --help            show this help message and exit
  -i ID книги, --id ID книги
  -d Директория, --directory Директория
                        Директория для загрузки книг. Если не указана, то используется текущая
  -nc, --no-cover       Не загружать обложку
  -l, --link            Вывести ссылку на книгу вместо загрузки
  --max-file-name-length Длина
                        Максимальная длина имени файла, по умолчанию 128 символов

Примечание: имя автора всегда следует вводить на русском языке, даже если искомая книжка не на нём.
```

А если вам не хочется каждый раз указывать директорию для загрузки, то можете использовать эти скрипты:

```sh
#!/usr/bin/env sh

books-dl -d ~/documents/books/ --no-cover "$*"
```

```sh
#!/usr/bin/env sh

books-dl -d ~/documents/books/ --no-cover -i "$1"
```

```sh
#!/usr/bin/env sh

books-dl -l "$*"
```
