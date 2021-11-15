#!/usr/bin/env python3

__version__ = "0.0.1"
__desc__ = "Консольная утилита для загрузки книжек с одного замечательного сайта"

import argparse
import os
import sys

import requests
from bs4 import BeautifulSoup

URL = "http://213.5.52.16/"
SEARCH_ENDPOINT = "search_2.php?user_name="
HEADERS = {
    "connection": "keep-alive",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
}


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def urljoin(*args):
    return "".join((URL, *args))


def get_book_name(book):
    return " - ".join((", ".join(book["authors"]), book["name"]))


def download_book(book: dict, directory: str, download_cover: bool):
    book_name = get_book_name(book)
    book_file_path = os.path.join(directory, book_name + ".html")
    eprint(f"Загружаем книгу в {book_file_path}")
    book_text = requests.get(book["link"], headers=HEADERS).text
    with open(book_file_path, "w") as f:
        f.write(book_text)

    if download_cover:
        cover_file_path = os.path.join(directory, book_name + ".jpeg")
        eprint(f"Загружаем обложку в {cover_file_path}")
        with open(cover_file_path, "wb") as f:
            f.write(requests.get(book["cover"], headers=HEADERS).content)


def main():
    parser = argparse.ArgumentParser(description=__desc__)
    parser.add_argument("query", metavar="Запрос", type=str, help="Запрос для поиска")
    parser.add_argument(
        "-d", "--directory", metavar="Директория", type=str, help="Директория для загрузки книг. Если не указана, то используется текущая"
    )
    parser.add_argument("-nc", "--no-cover", action="store_true", help="Не загружать обложку")
    parser.add_argument("-l", "--link", action="store_true", help="Вывести ссылку на книгу вместо загрузки")
    args = parser.parse_args()

    bs = BeautifulSoup(
        requests.get("".join((URL, SEARCH_ENDPOINT, args.query)), headers=HEADERS).text,
        "html.parser",
    )

    books = []
    trs = bs.find("table", cellspacing="1", border="1").find_all("tr")
    for tr in trs:
        tds = tuple(tr.find_all("td"))
        book = {}
        book["cover"] = urljoin(tds[0].img["src"])
        book["id"] = tds[1].text
        book["name"] = tds[2].text
        book["authors"] = tuple((a.text for a in tds[5].find_all("a")))
        book["link"] = urljoin(tds[6].a["href"])
        books.append(book)

    if not books:
        eprint(f"Не найдено книг по запросу {args.query}")
        return
    for i, book in enumerate(reversed(books)):
        eprint(f"{len(books) - i}. {get_book_name(book)}")

    while True:
        try:
            index = int(input()) - 1
            break
        except TypeError:
            continue

    if args.link:
        print(books[index]["link"])
    else:
        download_book(books[index], args.directory or os.curdir, not args.no_cover)


if __name__ == "__main__":
    main()
