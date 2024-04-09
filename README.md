# youtube-analysis-aws
YouTube Data Analysis Data Engineering Project using AWS


1. Creating the IAM user

2. Installing the AWS CLI:
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

3. Run: aws configure to configure the cli with the IAM user account both access key and secret access key and region name.

4. Create the s3 bucket for the raw data with name: ytaws-raw-useast-1-dev (enable encryption, block all public access)

5. Unzip the dataset and now upload it to s3 using cli:

aws s3 cp . s3://ytaws-raw-useast-1-dev/youtube/raw_statistics_reference_data/ --recursive --exclude "*" --include "*.json"

6. Copy all csv files:

aws s3 cp CAvideos.csv s3://ytaws-raw-useast-1-dev/youtube/raw_statistics/region=ca/
aws s3 cp DEvideos.csv s3://ytaws-raw-useast-1-dev/youtube/raw_statistics/region=de/
aws s3 cp FRvideos.csv s3://ytaws-raw-useast-1-dev/youtube/raw_statistics/region=fr/
aws s3 cp GBvideos.csv s3://ytaws-raw-useast-1-dev/youtube/raw_statistics/region=gb/
aws s3 cp INvideos.csv s3://ytaws-raw-useast-1-dev/youtube/raw_statistics/region=in/
aws s3 cp JPvideos.csv s3://ytaws-raw-useast-1-dev/youtube/raw_statistics/region=jp/
aws s3 cp KRvideos.csv s3://ytaws-raw-useast-1-dev/youtube/raw_statistics/region=kr/
aws s3 cp MXvideos.csv s3://ytaws-raw-useast-1-dev/youtube/raw_statistics/region=mx/
aws s3 cp RUvideos.csv s3://ytaws-raw-useast-1-dev/youtube/raw_statistics/region=ru/
aws s3 cp USvideos.csv s3://ytaws-raw-useast-1-dev/youtube/raw_statistics/region=us/

7. Using AWS Glue Data Catalog (for data metadata)

* Create a crawler
* create the IAM role for glue to access s3 and for glue to acces another services through glue service role permission
* Run the crawler, now you have the metadata table in the tables of aws glue
* Now we can use the aws athena to view the data, we need to specify the output location.

8. Now we need the fix the structure of our json files using lambda, so we will create a lambda (python 3.8) function to fix the json files from s3 (we will need a new role to let lambda access the s3 data), create the env variables of lambda, then deploy and test it (add layer and increase timeout if required).

The lambda code attached.

Athena Queries attached.

9. Now we will create an ETL job using AWS Athena to process the csv files. (code attached: pyspark-etl.py)
NOW csv data moved to cleaned bucket in s3.

10. Next is to automate the process of cleaning the json files not just one json file. using lambda trigger. (DONE)

11. Combine all data and generate useful information and dashboard.

Using the AWS Glue Visual ETL, create two sources for glue tables in the cleaned database, join them on id and category it and save the result to a new bucket (ytaws-analytics-useast-1-dev), create glue database (CREATE DATABASE db_ytaws_analytics;) Then save and run the job.

12. Using AWS QuickSight for Dashboard
* Create account
* Create database from glue
* Use for analytics
* Do some visualizations



refs:

* https://aws-sdk-pandas.readthedocs.io/en/stable/tutorials/005%20-%20Glue%20Catalog.html
* https://www.kaggle.com/datasets/datasnaek/youtube-new?resource=download




