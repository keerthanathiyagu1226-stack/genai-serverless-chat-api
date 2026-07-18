import json
import boto3

bedrock = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)


def lambda_handler(event, context):

    body = json.loads(event.get("body", "{}"))

    user_message = body.get("message", "")

    response = bedrock.converse(
        modelId="google.gemma-3-12b-it",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "text": user_message
                    }
                ]
            }
        ],
        inferenceConfig={
            "maxTokens": 300,
            "temperature": 0.7
        }
    )

    answer = response["output"]["message"]["content"][0]["text"]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "question": user_message,
            "answer": answer
        })
    }
