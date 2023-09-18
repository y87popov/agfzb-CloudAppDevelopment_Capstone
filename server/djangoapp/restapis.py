import requests
import json
from .models import CarDealer, DealerReview
# import related models here
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_dealerships(request):
    if request.method == "GET":
        context = {}

        state = request.GET.get("st")
        dealerId = request.GET.get("dealerId")
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/IBM-Course-Yordan_YordansSpace/dealership-package/get-dealership"

        try:
            if state:
                dealerships = get_dealers_from_cf(url, st=state)
            elif dealerId:
                dealerships = get_dealers_from_cf(url, dealerId=dealerId)
            else:
                dealerships = get_dealers_from_cf(url)
        except Exception as e:
            # Handle the error and set dealerships to an empty list or display an error message
            dealerships = []
            context["error"] = f"An error occurred while fetching dealerships: {e}"

        context["dealership_list"] = dealerships
        print(context["dealership_list"])

        return render(request, "djangoapp/index.html", context=context)


def get_request(url, **kwargs):
    
    # If argument contain API KEY
    api_key = kwargs.get("KIepUqkGJn2eEF2C3USaFGVKMIqYEYUC_ya-tMs6JiAc")
    print("GET from {} ".format(url))
    try:
        if api_key:
            params = dict()
            params["text"] = kwargs["text"]
            params["version"] = kwargs["version"]
            params["features"] = kwargs["features"]
            params["return_analyzed_text"] = kwargs["return_analyzed_text"]
            response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))
        else:
            # Call get method of requests library with URL and parameters
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")

    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, payload, **kwargs):
    print(kwargs)
    print("POST to {} ".format(url))
    print(payload)
    response = requests.post(url, params=kwargs, json=payload)
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):

    results = []

    # Call get_request with a URL parameter

    json_result = get_request(url)

    

    if json_result and "body" in json_result:

        # Get the list of dealerships from the response

        dealerships = json_result["body"]

        

        for dealer in dealerships:

            if "doc" in dealer and "address" in dealer["doc"]:

                dealer_doc = dealer["doc"]

                

                # Create a CarDealer object with values from the dealer document

                dealer_obj = CarDealer(

                    address=dealer_doc.get("address"),

                    city=dealer_doc.get("city"),

                    id=dealer_doc.get("id"),

                    lat=dealer_doc.get("lat"),

                    long=dealer_doc.get("long"),

                    st=dealer_doc.get("st"),

                    zip=dealer_doc.get("zip")

                )

                

                results.append(dealer_obj)

    

    return results


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



