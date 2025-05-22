# youtube-analysis-aws

YouTube Data Analysis Data Engineering Project using AWS

---

## 📖 TABLE OF CONTENTS

- [ABOUT](#about)
- [ARCHITECTURE](#architecture)
- [FEATURES](#features)
- [PREREQUISITES](#prerequisites)
- [INSTALLATION](#installation)
- [USAGE](#usage)
- [PROJECT STRUCTURE](#project-structure)
- [TECHNOLOGIES USED](#technologies-used)
- [CONTRIBUTING](#contributing)
- [LICENSE](#license)
- [CONTACT](#contact)

---

## 📌 ABOUT

This project demonstrates a data engineering pipeline that:

1. **Ingests** YouTube data into AWS S3.
2. **Processes** the data using AWS Glue and PySpark.
3. **Analyzes** the data using AWS Athena.
4. **Visualizes** insights with Amazon QuickSight.

---

## 🏗️ ARCHITECTURE

The pipeline follows this flow:

1. **Data Ingestion**:
   - Upload YouTube data to AWS S3 using AWS CLI.

2. **Data Processing**:
   - Use AWS Glue and PySpark to transform and clean the data.

3. **Data Analysis**:
   - Query the processed data using AWS Athena.

4. **Data Visualization**:
   - Create dashboards and visualizations using Amazon QuickSight.

![Architecture Diagram](architecture.jpeg)

---

## ✨ FEATURES

- End-to-end data pipeline on AWS.
- Automated data transformation with PySpark.
- Serverless data querying using Athena.
- Interactive dashboards with QuickSight.

---

## ✅ PREREQUISITES

Before you begin, ensure you have met the following requirements:

- AWS account with necessary permissions.
- AWS CLI installed on your machine.
- Python 3.7 or higher installed.

---

## 🚀 INSTALLATION

1. **Clone the repository**:

   ```bash
   git clone https://github.com/TawfikYasser/youtube-analysis-aws.git
   cd youtube-analysis-aws
   ```

2. **Create an IAM user** with programmatic access and note the Access Key ID and Secret Access Key.

3. **Install AWS CLI**:

   ```bash
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   unzip awscliv2.zip
   sudo ./aws/install
   ```

4. **Configure AWS CLI**:

   ```bash
   aws configure
   ```

   Enter your Access Key ID, Secret Access Key, default region, and output format.

---

## 🛠️ USAGE

1. **Upload data to S3**:

   ```bash
   aws s3 cp your_data_file.csv s3://your-bucket-name/
   ```

2. **Run PySpark ETL script**:

   ```bash
   python pyspark-etl.py
   ```

3. **Execute Athena SQL queries**:

   - Use the `athena.sql` and `athena-etl-sql.sql` files to run queries in the AWS Athena console.

4. **Visualize data with QuickSight**:

   - Refer to the `ytaws-analytcis-dashboard-quicksight.pdf` for dashboard examples.

---

## 📁 PROJECT STRUCTURE

```bash
youtube-analysis-aws/
├── architecture.jpeg                         # Architecture diagram
├── athena-etl-sql.sql                        # Athena ETL SQL script
├── athena.sql                                # Athena SQL queries
├── glue-etl-analytics.png                    # Glue ETL analytics image
├── lambda.py                                 # AWS Lambda function script
├── logical-plan_2024-04-09T16_11_39.545+02_00.png  # Logical plan image
├── pyspark-etl.py                            # PySpark ETL script
├── s3_cli_command.sh                         # S3 CLI commands
├── ytaws-analytcis-dashboard-quicksight.pdf  # QuickSight dashboard PDF
├── ytaws-parquet-analytics.py                # Parquet analytics script
└── README.md                                 # Project documentation
```

---

## 🧰 TECHNOLOGIES USED

- **AWS S3**: Object storage service.
- **AWS Glue**: Serverless data integration service.
- **AWS Athena**: Interactive query service.
- **Amazon QuickSight**: Business intelligence service.
- **PySpark**: Python API for Apache Spark.
- **AWS Lambda**: Serverless compute service.
- **AWS CLI**: Command-line interface for AWS.

---

## 🤝 CONTRIBUTING

Contributions are welcome! To contribute:

1. **Fork** the repository.
2. **Create** a new branch: `git checkout -b feature/your-feature-name`.
3. **Commit** your changes: `git commit -m 'Add some feature'`.
4. **Push** to the branch: `git push origin feature/your-feature-name`.
5. **Submit** a pull request.

Please ensure your code adheres to the project's coding standards and includes relevant tests.

---

## 📄 LICENSE

This project is licensed under the [MIT License](LICENSE).

---

## 📬 CONTACT

**Tawfik Yasser**  
GitHub: [@TawfikYasser](https://github.com/TawfikYasser)

---
