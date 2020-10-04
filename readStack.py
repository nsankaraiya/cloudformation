import boto3

client = boto3.client('cloudformation')

res_stackset = client.list_stacks(
    StackStatusFilter=[
        'CREATE_FAILED'|'CREATE_COMPLETE'|'ROLLBACK_FAILED'|'ROLLBACK_COMPLETE'|'DELETE_FAILED'|'UPDATE_COMPLETE'|'UPDATE_ROLLBACK_FAILED'|'UPDATE_ROLLBACK_COMPLETE',
    ]
)
for mystackName in res_stackset:
  res_stack = client.describe_stacks(
      StackName=mystackName
  )
  print res_stack.Stacks.Tags