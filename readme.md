# custOS[cust Observer Script]

A system created for the DevOps department at the company that i work for, to monitor expenses based in AWS Tags. We put tags in our projects to track their expenses and so we can understand how much each project costs monthly. You're supposed to tag your projects at AWS with tag key "PROJECT" and tag name "PROJECT NAME" as explained in main.py and install.py, though this can be easilly configured in the script

# How to build
To run this project you should have the packet boto3

# How does this alert works
We discussed internally in the devops team that we should monitor project costs in all services (EC2, RDS, etc.) by getting their respective values and compare them. It gets day by day the weekly value and compare the same period but in the last week (last 7 days x last 14 days). If its greater than 10% of last weeks value, it alerts us on our Slack alternative (we use rocketchat).

# How to:

First of all, create a db and configure it's name on ``` install.py ``` and ``` main.py ```. You're supposed to set the variable names indicated as comments on the code. An important part is to set the var **tags** where you set your tags of project names to track their costs.

After all vars set at these two files, run the ``` install.py ```. So, you're good to start running the script. This script is meant to be run as a cronjob. I use this script running at 01:01AM so i can check his alerts immediately on the next day in the morning.

> In order to this script run, you need to install and configure AWSCLI on the target machine and boto3 module with pip.

**Cronjob line**
``` 1 1 * * * python main.py >/dev/null 2>&1 ```

