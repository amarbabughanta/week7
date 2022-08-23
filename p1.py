import mysql.connector
from mysql.connector import errorcode

try:
   cm_connection = mysql.connector.connect(
      user ="aganta",
      password="aganta1234",
      host ="127.0.0.1",
      port="3307",
      database="grocery")

except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Invalid credentials")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database not found")
   else:
      print("Cannot connect to database:", err)

else:
   # Execute database operations...

   my_cursor = cm_connection.cursor()

   player_query = ("SELECT brand_id, brand_name FROM brand")

   my_cursor.execute(player_query)

   # Display results
   for row in my_cursor.fetchall():
      print("{}   {}".format(row[0], row[1]))
   my_cursor.close()
   # displaying particular record
   print("displaying particular record")
   brand_cursor = cm_connection.cursor()
   brand_query = ("SELECT brand.Brand_id,category.Category_id")
   brand_query += (" FROM brand JOIN category on brand.Brand_id=category.Category_id")
   brand_query += (" WHERE brand.brand_id = %s")

   rep_last = input("Enter brand_id ")

   rep_data = (rep_last,)  # Comma required for single value tuple
   brand_cursor.execute(brand_query, rep_data)
   for row in brand_cursor.fetchall():
      print("{} {} ".format(row[0], row[1]))
      brand_cursor.close()

   print("This is example is more complex. It uses functions, dictionaries and conditionals")
   # This is example is more complex. It uses functions, dictionaries and conditionals.

   import mysql.connector
   from mysql.connector import errorcode


   def get_status():
      statuses = {1: "gel", 2: "cleaner", 3: "toothpaste"}
      for key in statuses:
         print("{}. {}".format(key, statuses[key]))
      status = int(input("Enter Category_name or 0 for all orders: "))
      if 0 < status <= 3:
         return statuses[status]
      else:
         return "all"


   # main program

   # connect to DB
   try:
      cm_connection = mysql.connector.connect(
         user="aganta",
         password="aganta1234",
         host="127.0.0.1",
         port="3307",
         database="grocery")

   except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Invalid credentials")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database not found")
      else:
         print("Cannot connect to database:", err)

   else:
      Category_name = get_status()

      orders_cursor = cm_connection.cursor()
      orders_query = ("SELECT *")
      orders_query += ("FROM category")

      if Category_name == "all":
         print("\n**All category**")
         print("{} {} {}".format("category_id", "Category_name", "quantity"))
         print("-" * 77)
         orders_cursor.execute(orders_query)
         for (category_id, Category_name, quantity) in orders_cursor:
            print("{} {} {}".format(category_id, Category_name, quantity), end="")
         # if shippedDate is None:
         #    print(" Not Shipped", end="")
         # else:
         #    print(" {:%m/%d/%Y} ".format(shippedDate), end="")
         print(" {}".format(Category_name))
      else:
         orders_query += (" WHERE Category_name = %s")
         status_data = (Category_name,)
         orders_cursor.execute(orders_query, status_data)
         print("\n**Status: {}**".format(Category_name))
         print("{} {} {}".format("category_id", "Category_name", "quantity"))
         for (category_id, Category_name, quantity) in orders_cursor:
            print("{} {} {}\n".format(category_id, Category_name, quantity), end="", )
         # if shippedDate is None:
         #    print(" Not Shipped")
         # else:
         #    print(" {:%m/%d/%Y} ".format(shippedDate))

      orders_cursor.close()
      # cm_connection.close()
      # Example of displaying a one-to-many relationship
      print(".....Example of displaying a one-to-many relationship.......")
      import mysql.connector
      from mysql.connector import errorcode

      # connect to DB
      try:
         cm_connection = mysql.connector.connect(
            user="aganta",
            password="aganta1234",
            host="127.0.0.1",
            port="3307",
            database="grocery")

      except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
         else:
            print("Cannot connect to database:", err)

      else:
         select_clause = "SELECT Store_id,Store_name"
         from_clause = "FROM store"
         # from_clause += " JOIN order_details  ON order_details.customer_id = customer_details.customer_id"
         where_clause = "WHERE Store_id = 's1' and Store_name='gel store'"
      order_clause = "ORDER BY Store_id"
      orders_query = "{} {} {} {}".format(select_clause, from_clause, where_clause, order_clause)

      orders_cursor = cm_connection.cursor()
      orders_cursor.execute(orders_query)

      prev_orderNumber = ""  # identifies new order
      for (Store_id, Store_name) in orders_cursor:
         if Store_id != prev_orderNumber:
            prev_orderNumber = Store_id
            print("\ncustomer id: {} required by {}".format(Store_id, Store_name))
            print("customer id")
            print("   {}".format(Store_id))
            # print("   {}".format(customer_name))

            print("Ordered From")
      print("  {}  ".format(Store_name))
      # Insert an customer
      print(".....Insert an customer.....")
      import mysql.connector
      from mysql.connector import errorcode
      import random

      # connect to DB
      try:
         cm_connection = mysql.connector.connect(
            user="aganta",
            password="aganta1234",
            host="127.0.0.1",
            port="3307",
            database="grocery")

      except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
         else:
            print("Cannot connect to database:", err)

      else:
         office_query = "SELECT item_id,stock,quantity,price FROM glosary_items"
         office_cursor = cm_connection.cursor()
         office_cursor.execute(office_query)
         for row in office_cursor.fetchall():
            print("{}. {} {} {}".format(row[0], row[1], row[2], row[3]))
         office_cursor.close()

         itemid = input("Enter item id ")
         stock = input("Enter stock ")
         quantity = input("Enter quantity ")
         price = input("Enter price ")

         employee_query = ("INSERT INTO glosary_items "
                           "(item_id,stock,quantity,price)"
                           "VALUES (%s, %s, %s, %s)")

         employee_data = (itemid,stock,quantity,price)
         try:
            employee_cursor = cm_connection.cursor()
            employee_cursor.execute(employee_query, employee_data)
            cm_connection.commit()
            print("Added item")
            employee_cursor.close()
         except mysql.connector.Error as err:
            print("\nitem not added")
            print("Error: {}".format(err))
      cm_connection.close()
      print("......Update an customer.......")
      # Update an customer
      import mysql.connector
      from mysql.connector import errorcode

      try:
         cm_connection = mysql.connector.connect(
            user="aganta",
            password="aganta1234",
            host="127.0.0.1",
            port="3307",
            database="grocery")

      except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials")
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database not found")
         else:
            print("Cannot connect to database:", err)

      else:
         employee_last = input("Enter item_id ")
         column = input("Enter item to update (item_id, stock, quantity, price) ")
         prompt = "Enter new value for {} ".format(column)
         value = input(prompt)

         employee_query = ("UPDATE glosary_items SET " + column + "=%s WHERE item_id=%s")
         employee_data = (value, employee_last)
         try:
            employee_cursor = cm_connection.cursor()
            employee_cursor.execute(employee_query, employee_data)
            print("1")
            cm_connection.commit()
            print("Updated item")
            employee_cursor.close()
         except mysql.connector.Error as err:
            print("\nitem not updated")
            print("Error: {}".format(err))
            cm_connection.close()


            # Delete an customer
# Delete an customer
   print("Delete an customer")
   import mysql.connector
   from mysql.connector import errorcode

   # connect to DB
   try:
      cm_connection = mysql.connector.connect(
         user="aganta",
         password="aganta1234",
         host="127.0.0.1",
         port="3307",
         database="grocery")

   except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("Invalid credentials")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("Database not found")
      else:
         print("Cannot connect to database:", err)

   else:
      employee_last = input("Enter item id to delete ")

      employee_query = ("DELETE FROM  glosary_items "
                        "WHERE item_id = %s")
      employee_data = (employee_last,)
      try:
         employee_cursor = cm_connection.cursor()
         employee_cursor.execute(employee_query, employee_data)
         cm_connection.commit()
         print("Deleted item")
         employee_cursor.close()
      except mysql.connector.Error as err:
         print("\ncustomer not item")
         print("Error: {}".format(err))
      cm_connection.close()



   print ("Sucess!")
   cm_connection.close()





