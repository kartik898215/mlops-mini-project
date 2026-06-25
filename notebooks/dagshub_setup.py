import dagshub
import mlflow

mlflow.set_tracking_uri("https://dagshub.com/kartik898215/mlops-mini-project.mlflow")
 
dagshub.init(repo_owner='kartik898215', repo_name='mlops-mini-project', mlflow=True)


with mlflow.start_run():
    mlflow.log_param('parameter_name','value')
    mlflow.log_metric('metric name', 1)     
    
    
    
    
  

