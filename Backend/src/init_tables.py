import boto3
from config import DB_REGION_NAME, DB_ENDPOINT_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


def init_tables(client):
    client.create_table(
        TableName='guests',
        KeySchema=[
            {
                'AttributeName': 'guest_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'guest_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'guest_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'guest_name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'guest_message',
                'AttributeType': 'S'
            },
        ]
    )

    client.create_table(
        TableName='replica',
        KeySchema=[
            {
                'AttributeName': 'replica_id',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'replica_id',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'count',
                'AttributeType': 'N'
            },
        ]
    )


def add_replica(client):
    table = client.Table('replica')
    table.put_item(
        Item={
            'replica_id': 0,
            'count': 1,
        }
    )
    return table


if __name__ == '__main__':
    ydb_client = boto3.resource('dynamodb',
                                region_name=DB_REGION_NAME,
                                endpoint_url=DB_ENDPOINT_URL,
                                aws_access_key_id=AWS_ACCESS_KEY_ID,
                                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    init_tables(ydb_client)
    replica_table = add_replica(ydb_client)
    messages_table = ydb_client.Table('guests')

    print("Table(replica) status:", replica_table.table_status)
    print("Table(messages) status:", messages_table.table_status)
