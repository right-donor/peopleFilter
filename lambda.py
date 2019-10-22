# .---.  _ .-.  .-.           
# : .--':_;: : .' `.          
# : `;  .-.: : `. .'.--. .--. 
# : :   : :: :_ : :' '_.': ..'
# :_;   :_;`.__;:_;`.__.':_;  
## Made on October 22nd

import json
import os
# import boto3
from boto3 import resource
from boto3.dynamodb.conditions import Key,Attr

#dynamoDB resource
dynamodb_resource = resource('dynamodb')

#DynamoDB Table
table = dynamodb_resource.Table(os.environ['table'])

def lambda_handler(event,context):
    # Check if the POST has the data required
    if(event['userID'] == '' or event['type'] == '' or event['rh'] == '' or event['city'] == ''):
        return {
            'statusCode' : 422,
            'body' : 'Unexpected number of parameters'
        }
    
    # Get the information from the DynamoDB Table
    response = table.query(
        Select='ALL_ATTRIBUTES',
        KeyConditionExpression=Key('type').eq(event['type']),
        FilterExpression=Attr('rh').eq(event['rh']) and Attr('city').eq(event['city'])
    )
    
    print(response)
    