from psycopg import Connection
from psycopg.conninfo import make_conninfo

from psycopg_basics.statements import *


conn_info = make_conninfo(host='localhost', port=5432, dbname='postgres')

with Connection.connect(conninfo=conn_info, options='-c search_path=demo') as conn:
    with conn.cursor() as cursor:

        # create a user
        cursor.execute(create_user_stmt, ('Dan',))
        id = cursor.fetchone()[0]

        # get the user
        cursor.execute(get_user_stmt, (id,))
        user = cursor.fetchone()
        print(user)
