import json
import boto3
def import_credentials(file_cred="credentials.txt"):
    with open(file_cred) as fc:
        cred = fc.read()
    final_cred = json.loads(cred)
    return final_cred

def create_client():
    cred = import_credentials()
    client = boto3.client('iam', aws_access_key_id=cred['accesskey'],
                          aws_secret_access_key=cred['Secret Access Key'])
    return client

def create_IAM_user():
    client = create_client()
    client.create_user(UserName="Test")

def create_policy():
    client = create_client()
    with open("Policy Document.txt") as PD:
        document = PD.read()
    client.create_policy(PolicyName='AdministratorAccess', PolicyDocument=document)

def attach_policy():
    client = create_client()
    client.attach_user_policy(
    UserName='Test',
    PolicyArn='arn:aws:iam::097980647230:policy/AdministratorAccess')

create_IAM_user()
create_policy()
attach_policy()
