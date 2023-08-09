import cx_Oracle

# Replace the following placeholders with your database credentials
username = 'scott'
password = 'scott'
dsn = 'localhost:1521/orcl'  # Use correct hostname, port, and service name

try:
    # Connect to the database
    conn = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    cursor = conn.cursor()
    if conn:
        print("Connected to the Oracle database!")
    query= " select * from tab"
    cursor.execute(query)

    for i in cursor:
        print(i)

    # Perform your database operations here (e.g., execute queries)

    # Close the connection when done
    cursor.close()
    conn.close()

except cx_Oracle.DatabaseError as e:
    print(f"Error connecting to Oracle: {e}")
