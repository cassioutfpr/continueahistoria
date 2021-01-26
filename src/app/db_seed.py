import sys
import os.path
sys.path.append(os.path.abspath('./'))

from src.app.lib.utils import dbutils

seeds = [
    "INSERT INTO Users (name, email, password) VALUES ('Luiz', 'luizagnern@gmail.com', '123456');",
    "INSERT INTO Users (name, email, password) VALUES ('Cassio', 'cassioutfpr@gmail.com', '123456');",
]

print('Seeding database')
for seed in seeds:
    dbutils.execute_statement(seed)

print('Finished seeding')
