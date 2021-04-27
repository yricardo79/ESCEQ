#https://www.youtube.com/watch?v=LhsGA9PJtG0
import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost', #ip
            user='root',
            password='1234',
            db='ESCEQ'
        )

        #cursor
        self.connection.cursor()
        print("Conexión establecida exitosamente!")

    def select_user(self):
        sql = 'SELECT id_user, user_name, email FROM users WHERE user = {}'.__format__(id)

        try:
            self.cursor.excecute(sql)
            user = self.cursor.fetchone() #por que es un solo registro

            print("Id: ", user[0])
            print("Username: ", user[1])
            print("Email: ", user[2])

            pass
        except Exception as e:
            raise

    def select_all_users(self):
        sql = 'SELECT * FROM users'
        try:
            self.cursor.excecute(sql)
            users = self.cursor.fetall()

            for user in users:
                print("Id: ", user[0])
                print("Username: ", user[1])
                print("Email: ", user[2])
                print("__________________\n")

        except Exception as e:
            raise

# instancia para probar el cursor
#database> = DataBase()
#database.select_user()  # (1)

    #Actualización de un usuario por su id
    def update_user(self, id, user_name):
        sql = "UPDATE users SET user_name = '{ }' WHERE id  = { }".format(user_name, id)
        try:
            #ejecución de la sentencia
            self.cursor.excecute(sql)
            #metodo commit
            self.conection.commit()
        except Exception as e:
            raise

    def close(self):
        self.connection.close()

#instancia para probar el cursor
database = DataBase()
database.select_user(1)
database.update_user(1, 'Cambio de usuario')
database.select_user(1)
database.close()
