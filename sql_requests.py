import psycopg2


def db_conn():
    conn = psycopg2.connect(host='localhost', database='Web-bank', user='postgres', password='889988', port='5432')
    return conn


class SQLRequests():
    def __init__(self, table=str):
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


def createNewCustomer(id, firstname, secondname, thirdname, birthday, phone, email, currency, code, passport):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO customers(id, firstname, secondname, thirdname, birthday, phone, email, currency, code, passport)' 'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (id, firstname, secondname, thirdname, birthday, phone, email, currency, code, passport))
    conn.commit()
    cur.close()
    conn.close()

def createNewAccount(code_card, id_customer, amount, type, pulldate, cvv):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO accounts(id, id_customer, amount, account_type, pulldate, cvv)' 'VALUES (%s, %s, %s, %s, %s, %s)', (code_card, id_customer, amount, type, pulldate, cvv))
    conn.commit()
    cur.close()
    conn.close()

def createNewMotgage(id, id_customer, amount, date_take, date_retrieve, term, contribution):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO mortgage(id, id_customer, amount, date_take, date_retrieve, term, contribution)' 'VALUES (%s, %s, %s, %s, %s, %s, %s)', (id, id_customer, amount, date_take, date_retrieve, term, contribution))
    conn.commit()
    cur.close()
    conn.close()

def createNewCredit(id, id_customer, amount, date_take, date_retrieve, credit_type):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO credits(id, id_customer, amount, date_take, date_retrieve, credit_type)' 'VALUES (%s, %s, %s, %s, %s, %s)', (id, id_customer, amount, date_take, date_retrieve, credit_type))
    conn.commit()
    cur.close()
    conn.close()

def createNewCreditInformation(id, id_customer, personal_revenue, education, family_status, foreign_passport, car, pledhe):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO credit_information(id, id_customer, personal_revenue, education, family_status, foreign_passport, car, pledhe)' 'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (id, id_customer, personal_revenue, education, family_status, foreign_passport, car, pledhe))
    conn.commit()
    cur.close()
    conn.close()

def createNewDeposit(id, id_customer, currency, amount, date_open, term, rate, percent_on_acc):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO deposits(id, id_customer, currency, amount, date_open, term, rate, percent_on_account)' 'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (id, id_customer, currency, amount, date_open, term, rate, percent_on_acc))
    conn.commit()
    cur.close()
    conn.close()

