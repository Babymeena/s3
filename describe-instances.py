import boto3
def list_ec2_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()

    for i in response['Reservations']:
        for j in i['Instances']:
            print(f"Instance ID: {j['InstanceId']}")
            

list_ec2_instances()