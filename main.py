import MySQLdb

cxn = MySQLdb.connect(user='root', passwd='025kula')
cur = cxn.cursor()

cur.execute('show databases')
print(cur.fetchall())
