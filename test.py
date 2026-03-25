import mlflow
import os

mlflow.set_tracking_uri("https://dagshub.com/Kavya070605/mlflow.mlflow")
os.environ["MLFLOW_TRACKING_USERNAME"] = "Kavya070605"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "dagshub@0706"

with mlflow.start_run():
    mlflow.log_param("hello", "world")

print("done")