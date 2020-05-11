# https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
print("Printing Lists as Tabular Data")

# May require installation of tabulate:  $ pip3 install tabulate --user
print("\n1. Tabulate: https://pypi.python.org/pypi/tabulate")
from tabulate import tabulate
print()
print(tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age']))

print("\nUsing tabulate options to specify headers/table format:\n")
print(tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age'], tablefmt='orgtbl'))

# May require installation of prettytable:  $ pip3 install PrettyTable --user
print("\n2. PrettyTable: https://pypi.python.org/pypi/PrettyTable")
from prettytable import PrettyTable
print()

t = PrettyTable(['Name', 'Age'])
t.add_row(['Alice', 24])
t.add_row(['Bob', 19])
print(t)

# May require installation of texttable:  $ pip3 install texttable --user
print("\n3. texttable: https://pypi.python.org/pypi/texttable")
from texttable import Texttable
print()

t = Texttable()
t.add_rows([['Name', 'Age'], ['Alice', 24], ['Bob', 19]])
print(t.draw())

print()
