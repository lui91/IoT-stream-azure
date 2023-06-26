# Databricks notebook source
# MAGIC %md
# MAGIC # Read new streaming data

# COMMAND ----------

# MAGIC %md
# MAGIC ## Connect with blobstorage

# COMMAND ----------


storage_account = "syntweetsstorage"
#SP
# secret
service_credential = "pkE8Q~DTMP1ocLK.~leloIz5fzqYdHBX2KGasbOd"
# porperties
app_id = "4ced5214-f937-4cef-b680-5395a174647c"
dir_id = "6497bc6d-7e82-48c2-b571-9e9489ce1a4c"

# COMMAND ----------


spark.conf.set("fs.azure.account.auth.type." + storage_account + ".dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type." + storage_account + ".dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id." + storage_account + ".dfs.core.windows.net", app_id)
spark.conf.set("fs.azure.account.oauth2.client.secret." + storage_account + ".dfs.core.windows.net", service_credential)
spark.conf.set("fs.azure.account.oauth2.client.endpoint." + storage_account + ".dfs.core.windows.net", "https://login.microsoftonline.com/" + dir_id +"/oauth2/token")


# COMMAND ----------

spark.conf.set("delta.checkpointRetentionDuration", "0")
spark.conf.set("delta.logRetentionDuration", "0")

# COMMAND ----------

data = spark.read.load(f"abfss://data@{storage_account}.dfs.core.windows.net/coffee_data")

# COMMAND ----------

data.display()

# COMMAND ----------

data_stream = spark.readStream.format("delta").load(f"abfss://data@{storage_account}.dfs.core.windows.net/coffee_data")

# COMMAND ----------

data_stream.display()

# COMMAND ----------


