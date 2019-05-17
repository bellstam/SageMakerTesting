docker build -t     ml/data_access-demo .
eval $(aws ecr get-login --no-include-email --profile default --region us-west-2 | sed 's|https://||');
docker tag  ml/data_access-demo:latest $ECR_REM_DATA_ACCESS_ADDRESS;
docker push $ECR_REM_DATA_ACCESS_ADDRESS;
