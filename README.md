
# The King's Fund digital archive - Django implementation

## Development setup

1. sudo apt-get update
2. sudo apt-get install python-pip
3. sudo pip install virtualenv
4. git clone git@github.com:drtjmb/kingsf.git
5. cd kingsf
6. virtualenv venv
7. source venv/bin/activate
8. pip install -r modules.txt

mysql> CREATE DATABASE kingsf CHARACTER SET utf8 COLLATE utf8_general_ci;
mysql> GRANT ALL PRIVILEGES ON kingsf.* TO 'kingsf'@'localhost' IDENTIFIED BY '.....';

## Proposed layout

kingsf (project - top level site)
: home
: search
: view

ingest (app - ingest marc and OCR data)
: marc
: abbyy_xml
: alto_xml

search (app - abstract search backend)
: index
: search
: get

wp (app - wellcome player backend)
: search
: autocomplete
: biblio
: pdf
: prepare
