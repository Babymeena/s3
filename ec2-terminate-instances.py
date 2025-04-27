import boto3
ec2_client = boto3.client('ec2')

response = ec2_client.terminate_instances(
    InstanceIds=['i-0b0b3e8a30482c5cc', 'i-0b1577eaba5dc1390'])

for instance in response['TerminatingInstances']:
    print("Instance Id :", instance['InstanceId'])

    