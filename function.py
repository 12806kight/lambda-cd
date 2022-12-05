import json

def lambda_handler(event, context):
    # TODO implement
    #Try 2
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
