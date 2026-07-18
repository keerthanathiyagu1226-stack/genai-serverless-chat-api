# Serverless GenAI Chat API using AWS Bedrock

## Project Overview

A serverless Generative AI Chat API built using AWS Lambda, API Gateway, AWS SAM, and Amazon Bedrock.

The application accepts user prompts through a REST API and generates AI responses using the Google Gemma 3 12B IT foundation model.

## Architecture

User
 |
API Gateway
 |
AWS Lambda
 |
Amazon Bedrock Runtime
 |
Google Gemma 3 12B IT


## Tech Stack

- AWS Lambda
- Amazon API Gateway
- Amazon Bedrock
- Google Gemma 3 12B IT Model
- AWS SAM
- Python
- Docker
- AWS CloudFormation
- IAM


## Features

- Serverless AI chatbot API
- Natural language response generation
- Local testing using SAM CLI
- Docker-based Lambda execution
- Automated deployment using SAM
- Secure AWS IAM access


## API Endpoint

POST:

https://s8jvmvvg33.execute-api.us-east-1.amazonaws.com/Prod/chat


## Sample Request

```json
{
  "message": "Explain Docker containers"
}
Sample Response
{
  "question": "Explain Docker containers",
  "answer": "Docker containers are..."
}
Deployment

Build:

sam build

Deploy:

sam deploy --guided
Local Testing

Start API:

sam local start-api

Test:

curl -X POST http://127.0.0.1:3001/chat \
-H "Content-Type: application/json" \
-d '{"message":"Explain Kubernetes"}'
AWS Services Used
Lambda
API Gateway
Bedrock
IAM
CloudFormation
CloudWatch
Author

Keerthana T

