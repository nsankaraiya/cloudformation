import boto3
import json

client = boto3.client('cloudformation')

res_stackset = client.list_stacks(
  StackStatusFilter=[
    'CREATE_COMPLETE','UPDATE_COMPLETE',
  ]
)
print (res_stackset)
print (res_stackset['StackSummaries'])
temp = [res_stackset['StackSummaries'][0]['StackName']]
for mystackName in temp:
  print (mystackName)
  res_stack = client.describe_stacks(
    StackName=mystackName
  )
  for j in res_stack['Stacks'][0]['Tags']:
    print(j['Key'])
    print(j['Value'])
