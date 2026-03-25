https://dagshub.com/Kavya070605/mlflow.mlflow

import dagshub
dagshub.init(repo_owner='Kavya070605', repo_name='mlflow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)