# Project's Title
scrapy_crawler_s3

# Project's Description
In this project, our aim is to crawl a website comprehensively, storing all its content, including text and images, into an Amazon S3 bucket using Scrapy and boto3. To achieve this, we'll employ Scrapy's powerful CrawlSpider class for web crawling and utilize boto3 for interaction with the S3 service.

# Objectives:
- Capture all available text content and store them in .txt files.
- Ensure all images on the website are captured and stored
- Only scrape unique URLs to avoid duplicate content
- Only scrape internal links which belong to target website

# Implementation
Utilize Scrapy's CrawlSpider class for its ability to recursively follow links on a website. For images, leverage Scrapy's built-in pipeline, **scrapy.pipelines.images.ImagesPipeline**. For text files, implement a **custom pipeline** utilizing boto3 for S3 storage since Scrapy doesn't support .txt files by default as feed exporters.

This wil also include analysis of the entire crawler process i.e
- captured webpage
- The number of urls referenced on the webpage
- The number of images occurring on the webpage

# Install Dependencies
- conda activate your_virtual_environment
- cd to the directory where requirements.txt is located
- pip install-r requirements.txt

# Run The Scraper
- scrapy list ( to find out the all available spiders)
- scrapy crawl spider_name (here target spider is test)
- scrapy crawl test

