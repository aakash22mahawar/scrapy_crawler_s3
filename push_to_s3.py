import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
with open(r'C:\Users\AakashMahawar\anaconda3\envs\scrappy\ezee\files\0d80d7e3f1.txt', 'rb') as data:
    s3.Bucket('scrapy-aakash').put_object(Key='text_files/0d80d7e3f1.txt', Body=data)
    print('done')