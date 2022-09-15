#!python
import gettext
from time import strptime
from datetime import datetime
from dev_aberto.dev_aberto import hello
gettext.install('cli', localedir='locale') 
from babel.dates import format_datetime

if __name__ == '__main__':
    date, name = hello()
    print(date)
    print(_('Last commit done in:'), format_datetime(datetime.strptime(date.split("T")[0], "%Y-%m-%d").date()),_(' by'), name)
