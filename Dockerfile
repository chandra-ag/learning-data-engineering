# 1. Start with the official Airflow image
FROM apache/airflow:2.10.5

# 2. Switch to root to install system-level software (Java)
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends default-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
# Adding a 100-second timeout and retries for poor Wi-Fi


# 3. Switch back to the airflow user for security and pip installs
USER airflow

# 4. Install the Python providers and PySpark
# This "bakes" the libraries into the image so they are ready instantly
RUN pip install --no-cache-dir \
    --default-timeout=1000 \
    --retries 5 \
    apache-airflow-providers-apache-spark==4.1.3 \
    pyspark==3.5.1
RUN pip install --no-cache-dir "apache-airflow-providers-openlineage>=1.8.0"