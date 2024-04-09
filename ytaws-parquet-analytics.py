import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1712674591615 = glueContext.create_dynamic_frame.from_catalog(database=" ytaws_raw_cleaned", table_name="raw_statistics", transformation_ctx="AWSGlueDataCatalog_node1712674591615")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1712674553280 = glueContext.create_dynamic_frame.from_catalog(database=" ytaws_raw_cleaned", table_name="cleaned_raw_statistics_reference_data", transformation_ctx="AWSGlueDataCatalog_node1712674553280")

# Script generated for node Join
Join_node1712674624100 = Join.apply(frame1=AWSGlueDataCatalog_node1712674553280, frame2=AWSGlueDataCatalog_node1712674591615, keys1=["id"], keys2=["category_id"], transformation_ctx="Join_node1712674624100")

# Script generated for node Amazon S3
AmazonS3_node1712674816002 = glueContext.getSink(path="s3://ytaws-anlaytics-useast-1-dev", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=["region", "category_id"], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1712674816002")
AmazonS3_node1712674816002.setCatalogInfo(catalogDatabase="db_ytaws_analytics",catalogTableName="final_analytics")
AmazonS3_node1712674816002.setFormat("glueparquet", compression="snappy")
AmazonS3_node1712674816002.writeFrame(Join_node1712674624100)
job.commit()