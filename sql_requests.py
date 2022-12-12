import psycopg2


def db_conn():
    conn = psycopg2.connect(host='localhost', database='Web-bank', user='postgres', password='889988', port='5432')
    return conn

class SQLInputRequest():
    def __init__(self, SqlRequest):
        self.SqlRequest = SqlRequest

    def SqlRequestMany(self, fetch_count=int) -> list:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute(self.SqlRequest)
        data = cur.fetchmany(fetch_count)
        cur.close()
        cur.close()

        return data

    def SqlRequestAll(self) -> list:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute(self.SqlRequest)
        data = cur.fetchall()
        cur.close()
        cur.close()

        return data

    def SqlRequestOne(self) -> list:
        conn = db_conn()
        cur = conn.cursor()
        cur.execute(self.SqlRequest)
        data = cur.fetchone()
        cur.close()
        cur.close()

        return data


class SQLRequests():
    def __init__(self, table):
        self.table = table

    def SelectRequest(self, specify) -> list:
        if specify is None: specify = '*'
        conn = db_conn()
        cur = conn.cursor()
        cur.execute(f"SELECT {specify} FROM {self.table};")
        data = cur.fetchall()
        cur.close()
        conn.close()

        return data


    def DeleteDataRequest(self, specify):
        conn = db_conn()
        cur = conn.cursor()
        cur.execute(f'DELETE FROM {self.table} WHERE {specify}')
        conn.commit()
        cur.close()
        conn.close()

    def InsertIntoCustomerRequest(self, id=int, firstname=str, secondname=str):
        conn = db_conn()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO {self.table}(id, firstname, secondname)" "VALUES (%s, %s, %s)", (id, firstname, secondname))
        conn.commit()
        cur.close()
        conn.close()

    def CountIdReq(self):
        conn = db_conn()
        cur = conn.cursor()
        cur.execute(f'SELECT max(id) FROM {self.table}')
        data = cur.fetchone()
        cur.close()
        conn.close()
        for i, v in enumerate(data):
            data = v
            break
        if data is None: data = 0

        return data
