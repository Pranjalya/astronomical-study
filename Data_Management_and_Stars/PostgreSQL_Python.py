# psycopg2 is a connector between PostgreSQL and Python
import psycopg2
import numpy as np


def select_all(table):
    """
    Selecting all rows of a table
    """
    # Establish connection
    conn = psycopg2.connect(dbname='db', user='grok')
    # Establish cursor
    cursor = conn.cursor()
    try:
        # Execute query
        cursor.execute('SELECT * from '+table+';')
        records = cursor.fetchall()
    except:
        return []
    return records


def column_stats(table, column):
    """
    Finding mean and median of a table
    """
    conn = psycopg2.connect(dbname='db', user='grok')
    # Establish cursor
    cursor = conn.cursor()
    try:
        # Execute query
        cursor.execute('SELECT '+column+' from '+table+';')
        records = cursor.fetchall()
    except:
        return []
    values = []
    for row in records:
        values.append(row)
    values = np.array(values)
    return (np.mean(values), np.median(values))


# Producing same result as SQL queries using Python
# Query :
# SELECT p.radius/s.radius AS radius_ratio
# FROM Planet AS p
# INNER JOIN star AS s USING (kepler_id)
# WHERE s.radius > 1.0
# ORDER BY p.radius/s.radius ASC;

def query(file1, file2):
    table1 = np.loadtxt(file1, delimiter=',', usecols=(0, 2))
    table2 = np.loadtxt(file2, delimiter=',', usecols=(0, 5))
    ans = []
    for row1 in table1:
        for row2 in table2:
            if(row1[1] > 1 and row1[0] == row2[0]):
                ans.append([row2[1]/row1[1]])
    ans = np.array(ans)
    args = np.argsort(ans[:, 0])
    return ans[args]
