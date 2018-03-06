import click
import psycopg2
from collections import namedtuple
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

POSTGRES_DB = 'docker'
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'manager'
PGPASSWORD = 'manager'
POSTGRES_HOST = 'postgres'


@click.command()
@click.option('--namedb', help='The name of new database')
@click.option('--username', help='The username of new database')
@click.option('--password', help='The password of new database')
def create_database(**kwargs):
    connect = psycopg2.connect(
        user=POSTGRES_USER,
        host=POSTGRES_HOST,
        password=POSTGRES_PASSWORD,
    )
    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    params = namedtuple('params', 'basename, username, password')
    new_base = params(
        basename=kwargs.get('namedb'),
        username=kwargs.get('username'),
        password=kwargs.get('password')
    )
    if new_base:
        cursor = connect.cursor()
        cursor.execute(f'CREATE DATABASE {new_base.basename};')
        cursor.execute(
            f"CREATE USER {new_base.username}",
            f"WITH PASSWORD '{new_base.password}';"
        )
        cursor.execute(
            f'GRANT ALL PRIVILEGES ON DATABASE',
            f'{new_base.basename} TO {new_base.username};'
        )
        cursor.execute(f'ALTER ROLE {new_base.username}  SUPERUSER;')
        cursor.close()
        connect.close()


if __name__ == '__main__':
    create_database()
