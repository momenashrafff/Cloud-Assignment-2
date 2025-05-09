import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    for record in event['Records']:
        # The SQS message body contains the SNS notification JSON
        sns_message = json.loads(record['body'])
        order_data = json.loads(sns_message['Message'])
        
        # Insert into DynamoDB
        table.put_item(Item=order_data)
        
        print(f"Order inserted: {order_data['orderId']}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Order processed successfully!')
    }

