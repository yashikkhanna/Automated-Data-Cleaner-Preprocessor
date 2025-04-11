import psycopg2

DB_HOST="localhost"
DB_PORT="5432"
DB_NAME="demodb"
DB_USER="postgres"
DB_PASSWORD="Toshik@121"

try:
    connection=psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cursor=connection.cursor()
    print("Postgree Sql Connection successful!")

    # testing query
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    tables=cursor.fetchall()
    print("tables in database:")
    for table in tables:
        print(table[0])

    # close connection
    cursor.close()
    connection.close()
    print("connection closed!")

except Exception as e:
    print(f"Error connecting to postgres: {e}")