from uuid import uuid1
import boto3
from config import DB_REGION_NAME, DB_ENDPOINT_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


class YDBClient:
    def __init__(self):
        self.ydb_client = boto3.resource('dynamodb',
                                         region_name=DB_REGION_NAME,
                                         endpoint_url=DB_ENDPOINT_URL,
                                         aws_access_key_id=AWS_ACCESS_KEY_ID,
                                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    def get_replica(self):
        table = self.ydb_client.Table('replica')
        response = table.update_item(Key={'replica_id': 0},
                                     ReturnValues="UPDATED_NEW",
                                     ExpressionAttributeValues={":inc": 1},
                                     UpdateExpression='ADD count :inc', )
        replica_id = response['Attributes'].get('count', 0)
        return str(replica_id)

    async def create_message(self, msg):
        table = self.ydb_client.Table('guests')
        guest_id = uuid1().hex
        table.put_item(
            Item={
                'guest_id': guest_id,
                'guest_name': msg.author,
                'guest_message': msg.message
            }
        )
        return guest_id

    async def get_messages(self):
        table = self.ydb_client.Table('guests')
        items = []
        scan_kwargs = {}
        done = False
        start_key = None
        response = {}
        while not done:
            if start_key:
                scan_kwargs['ExclusiveStartKey'] = start_key
            response = table.scan(**scan_kwargs)
            items += response.get('Items', [])
            start_key = response.get('LastEvaluatedKey', None)
            done = start_key is None
        return items, response
