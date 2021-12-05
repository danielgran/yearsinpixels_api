import os
import sys

testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))


try:
    import mysql.connector

    connection = mysql.connector.connect(user='root', database='yearsinpixels', password='somepass')
    connection.close()
    disable_mysql_testcase = False
except:
    disable_mysql_testcase = True
