import psycopg2

try:
    # PostgreSQL veritabanına bağlantı oluşturma
    dataBase = psycopg2.connect(
        host='localhost',
        user='postgres',  # PostgreSQL kullanıcı adı
        password='password123'  # PostgreSQL kullanıcı parolası
    )

    # cursor object oluşturma
    cursorObject = dataBase.cursor()

    # Veritabanı oluşturma
    cursorObject.execute("CREATE DATABASE postgres")

    # Bağlantıyı kapatma
    dataBase.close()

except Exception as e:
    print("Error:", e)
