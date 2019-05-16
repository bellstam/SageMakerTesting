docker build -t ml/model-demo .
eval $(aws ecr get-login --no-include-email --profile default --region us-west-2 | sed 's|https://||');
docker tag ml/model-demo:latest $ECR_REM_ADDRESS;
docker push $ECR_REM_ADDRESS;
