import boto3
from datetime import datetime, timedelta


class ByTags:

    def __init__(self, linked_account, tag_key):
        self.linked_account = linked_account
        self.tag_key = tag_key

    client = boto3.client('ce')

    dayvalue = 0

    today = datetime.today().strftime('%Y-%m-%d')
                                                                                                
    yesterday = ((datetime.today() + timedelta(days= - 1)).strftime('%Y-%m-%d'))
    
    def get_cost_by_tags(self, tag):
        ''' This method consumes aws's API to track all costs based on
            specific TAGS. It tracks costs of a day before the run period. '''

        linked_account = self.linked_account
        tag_key = self.tag_key

        client=self.client
        dayvalue = self.dayvalue
        
        today = self.today
        yesterday = self.yesterday

        if tag != '':
            response = client.get_cost_and_usage(
            TimePeriod = {
                'Start': yesterday,
                'End': today,
            },
            Granularity = 'DAILY',
            Filter = {
                "And": [{
                    "Dimensions": {
                        "Key": "LINKED_ACCOUNT",
                        "Values": [linked_account,]
                    }
                }, 
                {
                    "Tags": {
                        "Key": tag_key,
                        "Values": [tag]
                    }
                }]
            },
            Metrics = ["BlendedCost"],
            GroupBy = [
                {
                    'Type': 'DIMENSION',
                    'Key': 'SERVICE'
                },
                {
                    'Type': 'DIMENSION',
                    'Key': 'USAGE_TYPE'
                }
            ]
        )
        for results in response['ResultsByTime']:
            for groups in results['Groups']:
                value_iter = groups['Metrics']['BlendedCost']['Amount']
                dayvalue += float(value_iter)
        return dayvalue
