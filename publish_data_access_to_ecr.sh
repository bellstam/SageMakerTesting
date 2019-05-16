#!/bin/sh

# construct the ECR name.
account=$(aws sts get-caller-identity --query Account --output text)
#region=$(aws configure get region)
region=us-west-2
tag=latest

fullname="${account}.dkr.ecr.${region}.amazonaws.com/ml/data_access-demo:${tag}"

# If the repository doesn't exist in ECR, create it.
# The pipe trick redirects stderr to stdout and passes it /dev/null.
# It's just there to silence the error.
aws ecr describe-repositories --repository-names "ml/data_access-demo" > /dev/null 2>&1

# Check the error code, if it's non-zero then know we threw an error and no repo exists
if [ $? -ne 0 ]
then
    aws ecr create-repository --repository-name "ml/data_access-demo" > /dev/null
fi

# Get the login command from ECR and execute it directly
$(aws ecr get-login --region ${region} --no-include-email)

# Build the docker image, tag it with the full name, and push it to ECR
docker build  -t "ml/data_access-demo:${tag}" data_access/
docker tag "ml/data_access-demo:${tag}" ${fullname}

docker push ${fullname}
