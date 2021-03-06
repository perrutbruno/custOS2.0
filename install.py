from sqlhandler import SQLHandler

print('- - INSTALLATION SCRIPT FOR THE CUSTOS - - ')

#Tag Value you want to track the costs
#These tags should be set as string divided by comma ','
#Ex: tags = ['PROJECT1', 'PROJECT2', ...]
tags = ["PROJECT1","PROJECT2", "PROJECT3", "PROJECT4"]

#DB address
db_address = '10.0.0.139'

#DB Username
db_user = 'custosuser'

#DB password
db_pass = 'custospass'

#DB name
db_name = 'custos'

#Instiate the database object to interact with
sql_actions = SQLHandler(db_address, db_user, db_pass, db_name)

#Create in our database (as set above) our tables and columns
for tag in tags:
    #Replace '/' with '_' because of mariadb's rules of table names
    sql_actions.set_sql_table_creation(tag.replace("/", "_"))
    print("\n" + tag + " table being created")

print('- - CREATED SUCCESFULLY - -')


