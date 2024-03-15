import requests
import boto3

s3 = boto3.client('s3', region_name="us-east-1")

url = 'https://a.espncdn.com/combiner/i?img=/i/headshots/mlb/players/full/4654313.png'
data = requests.get(url).content

with open('bryce.png', 'wb') as f:
    f.write(data)

bucket = 'ds2002-svc8ft'
local_file = 'bryce.png'

with open(local_file, 'rb') as f:
    file = str(f.read())

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = file,
    ACL = 'public-read'
)

expires_in = 604800

url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': local_file},
    ExpiresIn=expires_in,
)

print(url)

https://ds2002-svc8ft.s3.amazonaws.com/bryce.png?AWSAccessKeyId=ASIA3FLD3OOGJ6IS4PUF&Signature=x%2F2jnWDpxDkTnCOtFACnHAo04Lc%3D&x-amz-security-token=FwoGZXIvYXdzEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDA%2B3%2F0qGUK1DsLvYCCLEAdntipHkJ8lD4M804B7bmonIFv%2FPBllWkytiAzxe6ZdfNAXP0LtsFV6Zr%2FAxtZuszkNNJX5pSCd6m2nB%2Ff8XxzNyP%2B39PsAzcThux4s%2BRrDPOI%2FamlJwu94v0XPonzN5cn0fMzzattYZBJL50rArL9mObDQaMMEg4eFN3QMbYWF%2FS3jYygWvA%2FJm6q7kEp9VGqxVf7CtScch427hTOYD5ZIwNZaGMVQYIImC1JUMZN%2FI9%2FvShkxC8YoNU%2FJzzuvsNEtWPoAo2crSrwYyLVk92TEnf%2FrDRbFdRICQCCZyhtaQLFdIOccBJ12Lg3nhIviDcdtFQeBLZK6YnQ%3D%3D&Expires=1711144500

