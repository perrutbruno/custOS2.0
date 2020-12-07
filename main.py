from bytags import ByTags
from sqlhandler import SQLHandler
from mailer import Mailer
import datetime
from post_rocketapi import RocketChat

#Your AWS Linked Account number
linked_account = '0123456789'

#Tag Key to track costs
tag_key = 'PROJETO' #In our case the Tag Key was named PROJETO, which means PROJECT in pt-br.  We use to tag our instances, rds, etc with this name to track the costs based on the                                                                                                 # project that the referred service run.

#Tag Value you want to track the costs
tags = ["PROJECT1","PROJECT2", "PROJECT3", "PROJECT4"]

#DB address (YOUR DB ADDRESS)
db_address = '10.0.0.139'

#DB Username (YOUR DB USER)
db_user = 'custosuser'

#DB password (YOUR DB USER'S PASS)
db_pass = 'custospass'

#DB name (YOUR DB NAME)
db_name = 'custos'

#Instantiate the ByTags object to interact with AWS's api in its method
costs_get_daily = ByTags(linked_account, tag_key)

#Instiate the database object to interact with
sql_actions = SQLHandler(db_address, db_user, db_pass, db_name)

#Instantiate rocketChat object to send alerts via rocketchat
RocketChat = RocketChat('rocketchat alterdata')

#Daily comparative and daily usage value updater per project
for tag in tags:
    if "/" in tag:
        tag = tag.replace("/", "_")
    elif "-" in tag:
        tag = tag.replace("-", "_")
    elif " " in tag:
        tag = tag.replace(" ", "_")

    #Get daily expenses value of the project and Update today's project value in sql
    expenses_value_today = costs_get_daily.get_cost_by_tags(tag)
    
    #Insert into database current values
    sql_actions.set_sql_insert(tag, expenses_value_today)
    
    #Get current value by period (last week - two weeks ago)
    todays_value_comparative = sql_actions.get_select_period(tag)

    #Get value of last week (last 7 days)
    last_weeks = sql_actions.get_select_lastweek(tag)

    #Get value of last week x2 (last 14 days)
    last_weeks_2 = sql_actions.get_select_lastweek_2(tag)

    #If today's expenses value for the project is greater than 10% of last week's value, it alerts by email
    if todays_value_comparative == True:
        
        #New method to send alerts via our rocketchat channel
        RocketChat.rocketchat_api_alert(f'The project {tag} has exceeded the maximum threshold of use rate. It has increased its value in more than 10 per cent of the past weeks medium value. LAST WEEK = {last_weeks} / 2 WEEKS AGO = {last_weeks_2}. ')

