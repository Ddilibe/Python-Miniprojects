#!/usr/bin/env python
"""
    Script for trying to establish a connection with MySQL
"""
import MySQLdb

if __name__ == '__main__':
    instant = {
            'host' : 'localhost',
            'port' : 3306,
            'user' : 'root',
            #'passwd' : '',
            'db' : 'employee',
            #     'charset' : 'utf8'
            }
    conn = MySQLdb._mysql.connect(**instant)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows():
        print(row)
    cur.close()
    conn.close()
