import boto3

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='AKIATCVRX4SFLGPWXGOJ',
aws_secret_access_key='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'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

object = s3.Object('bike-predictor', 'file_name.txt')

result = object.put(Body=open('D:\GIT\git.txt', 'rb'))

res = result.get('ResponseMetadata')

if res.get('HTTPStatusCode') == 200:
    print('File Uploaded Successfully')

else:
    print('File Not Uploaded')