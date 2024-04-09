SELECT *
FROM " ytaws_raw_cleaned"."raw_statistics" a
	INNER JOIN (
		SELECT *
		FROM " ytaws_raw_cleaned"."cleaned_raw_statistics_reference_data"
	) b ON a.category_id = b.id
WHERE a.region = 'us';