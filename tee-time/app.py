import json
import requests
from bs4 import BeautifulSoup

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # Available Warm Springs Tee Times
    try:

        url = "https://web2.myvscloud.com/wbwsc/idboisewt.wsc/search.html?Action=Start&SubAction=&secondarycode=2&begindate=07%2F17%2F2021&numberofplayers=2&begintime=12%3A00+am&numberofholes=18&display=detail&module=gr&multiselectlist_value=&grwebsearch_buttonsearch=yes"

        # payload = "{\n\"phone\": \"202-555-0116\",\n\"password\": \"Password1@\"\n}"
        params = {
            "Action": "Start",
            "begindate": "07/17/2021",
            "numberofplayers": 4,
            "begintime": "12%3A00+am",
            "numberofholes": 18,
            "display": "detail",
            "module": "gr",
            "grwebsearch_buttonsearch": "yes"
        }

        headers = {
        'Content-Type': 'application/json'
        # 'Cookie': '_webtracsessionid=373c52db6210bee2ecf6712a276fd141fbf576e4cd7668ef894a2deaa541d54b2ea9d25315c490ce41d5fa428081b38debeda628d3074d1eccea437baf176c11; _CookiesEnabled=Yes; _mobile=no'
        }

        response = requests.request("GET", url, headers=headers, params = params) #data = payload

        print(response.text.encode('utf8'))
    except Exception as e:
        print(e)



    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
