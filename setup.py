import setuptools

from books_dl import __desc__, __version__


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="books-dl",
    version=__version__,
    author="Layerex",
    author_email="layerex@dismail.de",
    description=__desc__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Layerex/books-dl",
    classifiers=[
        "Development Status :: 6 - Mature",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    py_modules=["books_dl"],
    entry_points = {
        "console_scripts": [
            "books-dl = books_dl:main",
        ],
    },
    install_requires=["beautifulsoup4", "requests"],
)
