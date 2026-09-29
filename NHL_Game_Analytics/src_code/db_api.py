
import pymysql as db
from nhl_const import create_tbl_sql

def get_db_conn(db_name):
    try:
        db_conn = db.connect(host='localhost',user = 'root' , password = '123456',database = db_name)
    except Exception as e:
        print("Error")
    return db_conn

def execute_sql(sql,values=None,output=False):

    conn = get_db_conn('nhl_gaming')
    cursor = conn.cursor()
    if not values:
        cursor.execute(sql)
        if output:
            data = cursor.fetchall()
    else:
        cursor.execute(sql,values)
        cursor.execute('commit')
    conn.close()
    if output:
        return data

def db_tbl_handle(tbl_list,is_drop=False):
    conn=get_db_conn('nhl_gaming')
    cursor = conn.cursor()
    for tbl in tbl_list:
        if is_drop:
            sql = f""" DROP TABLE IF EXISTS {tbl}"""
        else:
            sql = create_tbl_sql[tbl]
        cursor.execute(sql)

        cursor.execute('commit')
    cursor.close()

