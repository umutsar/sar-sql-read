import pymysql

def read_data():
    connection = pymysql.connect(
        host="hostname", # Your Hostname: for example "srv991.hstgr.io"
        user="username", # username of your database
        password="passwd", # Password of your database
        db="database_name", # Your database's name
        charset='utf8mb4', # (Optional) Your database chatset
        cursorclass=pymysql.cursors.DictCursor
    )


    with connection.cursor() as cursor:
        # Verileri getirme
        sql = "SELECT * FROM products" # products is optional. You can change it according to your database table.
                                     # You can change sql queries and you can make creative program. 
        cursor.execute(sql)
        result = cursor.fetchall()
        
        for row in result:
            print(row)
    
    return result

data_result = read_data() # Finish command, data are coming here.

# Example output: 
# {'Id': 3, 'product_name': 'Türkish cafe', 'hot_or_cool': 'hot', 'price': 60.0, 'description': 'description3', 'pieces': 44}    
# {'Id': 5, 'product_name': 'Flat White', 'hot_or_cool': 'cool', 'price': 10.0, 'description': 'description4', 'pieces': 32}
# {'Id': 1, 'product_name': 'Latte', 'hot_or_cool': 'cool', 'price': 31.0, 'description': 'description1', 'pieces': 15}
# {'Id': 2, 'product_name': 'Americano', 'hot_or_cool': 'hot', 'price': 50.5, 'description': 'description2', 'pieces': 12}
