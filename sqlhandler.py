import datetime
import pymysql

#Notice that i have a bunch of old method here and i don't use all method created here, but i'll keep them for the case we change our mind somehow...
class SQLHandler:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')

    weekday_sql_column = None

    today = datetime.datetime.today().weekday()

    if today == 0:
        weekday_sql_column = 'value_monday'
    elif today == 1:
        weekday_sql_column = 'value_tuesday'
    elif today == 2:
        weekday_sql_column = 'value_wednesday'
    elif today == 3:
        weekday_sql_column = 'value_thursday'
    elif today == 4:
        weekday_sql_column = 'value_friday'
    elif today == 5:
        weekday_sql_column = 'value_saturday'
    elif today == 6:
        weekday_sql_column = 'value_sunday'

    def set_sql_table_creation(self, project):
        bd = self.db
        cursor = bd.cursor()


        sql_create_table = """create table {0} (id_register INT(11) NOT NULL AUTO_INCREMENT, CONSTRAINT pk_id_register PRIMARY KEY (id_register), value float NOT NULL, date timestamp NULL DEFAULT CURRENT_TIMESTAMP);""".format(project)



        try:
            # Execute the query above
            cursor.execute(sql_create_table)
            # Confirms the execution on DB
            bd.commit()
 
        except:
            # It does rollback if something unexpected happened suddenly
            bd.rollback()
            print("Error inserting data on sql")
    
        cursor.close()
        return 'OK'

    def set_sql_db_allocation(self, tag):
        bd = self.db
        cursor = bd.cursor()

        sql_allocation = """INSERT INTO registers_custos (name_project, value_monday, value_tuesday, value_wednesday, value_thursday, value_friday, value_saturday, value_sunday, lastweek_values) VALUES ('{0}', 0, 0, 0, 0, 0, 0, 0, 0);""".format(tag)

        try:
            # Execute the query above
            cursor.execute(sql_allocation)
            # Confirms the execution on DB
            bd.commit()
 
        except:
            # It does rollback if something unexpected happened suddenly
            bd.rollback()
            print("Error inserting data on sql")
    
        cursor.close()
        return 'OK'


    
    def set_sql_insert(self, project, value):
        bd = self.db
        cursor = bd.cursor()

        sql = """insert into `{0}` (value) values ({1});""".format(project,value)

        try:
            # Execute the query above
            cursor.execute(sql)
            # Confirms the execution on DB
            bd.commit()
 
        except:
            # It does rollback if something unexpected happened suddenly
            bd.rollback()
            print("Error inserting data on sql")
    
        cursor.close()
        return 'OK'

    def get_select_byday(self, project):
        bd = self.db
        cursor = bd.cursor()
        weekday_sql_column = self.weekday_sql_column

        sql = "SELECT value FROM {0} order by id_register desc limit 1;".format(project)
        value = 0

        try:
            # Execute SQL query
            cursor.execute(sql)
            
            # Read all lines in table
            line = cursor.fetchall()
            
            value += line[0][0]
            
        except Exception as exc:
            print("Error - ", exc)

        cursor.close()

        return value

    def get_select_lastweek_today(self, project):
        bd = self.db
        cursor = bd.cursor()

        sql = "SELECT value FROM {0} order by id_register desc limit 8;".format(project)
        value = 0

        try:
            # Execute SQL query
            cursor.execute(sql)
            
            # Read all lines in table
            line = cursor.fetchall()

            value += float(line[7][0])
            
        except Exception as exc:
            print("Error - ", exc)

        cursor.close()
        
        return value
        
    def get_select_byweek(self, project):
        bd = self.db
        cursor = bd.cursor()
        weekday_sql_column = self.weekday_sql_column

        sql = "SELECT * FROM registers_custos WHERE name_project = '{0}';".format(project)

        try:
            # Execute SQL query
            cursor.execute(sql)
            
            # Read all lines in table
            lines = cursor.fetchall()
            
            #1st index is the register's id_ in sql
            #2st is the project_name column, that's why we sum +2 in the variable below, to get the right index.
            weekday_in_number = self.today + 2

            #Initialize a var to sum all values in "weekday"_values
            sum_values = 0

            for index in range(2,9):
                sum_values += lines[0][index]
                
        except Exception as exc:
            print("Error - ", exc)
 
        cursor.close()
        return sum_values

    def get_select_lastweek(self, project):
        bd = self.db
        cursor = bd.cursor()

        sql = "SELECT value FROM {0} order by id_register desc limit 21;".format(project)

        try:
            # Execute SQL query
            cursor.execute(sql)

            # Read all lines in table
            lines = cursor.fetchall()
            print(lines)

            #Initialize a var to sum all values in "weekday"_values
            sum_values_week1 = 0

            for index in range(0,7):
                sum_values_week1 += lines[index][0]

            print(sum_values_week1)

            
                
        except Exception as exc:
            print("Error - ", exc)

        cursor.close()
        return (float(sum_values_week1))
    

    def get_select_lastweek_2(self, project):
        bd = self.db
        cursor = bd.cursor()

        sql = "SELECT value FROM {0} order by id_register desc limit 21;".format(project)

        try:
            # Execute SQL query
            cursor.execute(sql)

            # Read all lines in table
            lines = cursor.fetchall()
            print(lines)

            #Initialize a var to sum all values in "weekday"_values
            sum_values_week1 = 0

            for index in range(7,14):
                sum_values_week1 += lines[index][0]

            print(sum_values_week1)



        except Exception as exc:
            print("Error - ", exc)

        cursor.close()
        return (float(sum_values_week1))

    def get_select_period(self, project):
        bd = self.db
        cursor = bd.cursor()

        sql = "SELECT value FROM {0} order by id_register desc limit 21;".format(project)

        try:
            # Execute SQL query
            cursor.execute(sql)
            
            # Read all lines in table
            lines = cursor.fetchall()
            print(lines)

            #Initialize a var to sum all values in "weekday"_values
            sum_values_week1 = 0
            sum_values_week2 = 0

            for index in range(0,7):
                sum_values_week1 += lines[index][0]

            print(sum_values_week1)

            for index in range(7,14):
                sum_values_week2 += lines[index][0]
            print(sum_values_week2)
            
                
        except Exception as exc:
            print("Error - ", exc)
        
        cursor.close()

        diff_between_weeks = sum_values_week1 - sum_values_week2

        ten_percent_week2 = sum_values_week2 / 10
 
        if diff_between_weeks > ten_percent_week2:
            return True
        else:
            return False


