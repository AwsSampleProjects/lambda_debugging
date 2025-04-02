import json
import requests

def lambda_handler(event, context):
    url = "https://api.github.com"
    
    print("Starting request to GitHub API...")

    # Debug breakpoint (no import needed in Python 3.7+)
    breakpoint()

    try:
        response = requests.get(url)
        data = response.json()  # Automatically parses the JSON response

        return {
            "statusCode": 200,
            "body": data  # Return the parsed JSON
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

