###--------Code----
import json
import boto3


def lambda_handler(event, context):
    s3 = boto3.clinet("s3")
    data = json.loads(event["Records"][0]["body"])
    s3.put_object(Bucket="sqs_bucket", Key="sqs_data.json", Body=json.dump(data))

    return {
    'statusCode': 200,
    'body': json.dump('Successfully Created')
    }

###-----------------