import json
import boto3


def hello(event, context):
    client = boto3.client("lambda")
    return client.list_functions()
