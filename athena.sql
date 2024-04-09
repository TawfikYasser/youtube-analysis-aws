SELECT a.title,
	a.category_id,
	b.snippet_title
FROM "ytaws-raw"."raw_statistics" a
	INNER JOIN (
		SELECT *
		FROM " ytaws_raw_cleaned"."cleaned_raw_statistics_reference_data"
	) b ON a.category_id = b.id
WHERE a.region = 'us';


SELECT * FROM "AwsDataCatalog"."ytaws-raw"."raw_statistics_reference_data" limit 10;

SELECT * FROM "AwsDataCatalog"."ytaws-raw"."raw_statistics_reference_data" limit 10;

SELECT * FROM "AwsDataCatalog"." ytaws_raw_cleaned"."cleaned_raw_statistics_reference_data" limit 10;

SELECT * FROM "ytaws-raw"."raw_statistics" where region = 'ca' limit 100;

SELECT * FROM " ytaws_raw_cleaned"."cleaned_raw_statistics_reference_data" limit 10;

