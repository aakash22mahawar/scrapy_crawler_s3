import csv
from itemadapter import ItemAdapter
import hashlib
import os
import boto3

class EzeePipeline:

    def __init__(self):
        self.s3 = boto3.client('s3')

    def process_item(self, item, spider):
        folder_path = r'C:\Users\AakashMahawar\anaconda3\envs\scrappy\ezee\files'
        # Generate filename using a unique identifier, e.g., URL
        url_hash = hashlib.sha1(item['url'].encode()).hexdigest()
        filename = f'{url_hash[:10]}.txt'  # Shortened filename

        # Combine folder path with filename
        filepath = os.path.join(folder_path, filename)

        # Write text data to the generated filename
        with open(filepath, 'w', encoding='utf-8') as f:
            # Write the URL of the page
            f.write("URL: " + item['url'] + "\n\n")
            f.write("-" * 100 + "\n\n")  # Separator

            # Write each element as a separate row
            for line in item['text_data']:
                line = line.strip()
                if line:
                    f.write(line + '\n')
            f.write("-" * 100 + "\n\n")  # Separator

        # Upload the file to S3
        with open(filepath, 'rb') as file_content:
            self.s3.put_object(
                Bucket="proco-take-home-assignment-aakash",
                Key=f'aakash_mahawar/text-files/{filename}',
                Body=file_content
            )

        # Write webpage info to a separate CSV file
        with open('webpage_info.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['url', 'num_urls', 'num_images']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header if file is empty
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({
                'url': item['url'],
                'num_urls': item['num_urls'],
                'num_images': item['num_images']
            })

        return item
