import get_token
import json
import http.client

# Get token
tokenizer = get_token.Token()
acces_token = tokenizer.get_token(False)


conn = http.client.HTTPSConnection("demo.neterium.cloud")

payload = ("{\"records\":[{\"type\":\"transaction\",\"object\":{\"transactionId\":\"PAY123\","
           "\"currency\":\"GBP\",\"amount\":500,\"debtor\":{\"account\":{\"id\":\"A101020110292152\"},"
           "\"name\":\"DENIS, Corentin\",\"postalAddresses\":[{\"addressLines\":[\"2021 Atwater Street\","
           "\"Suite 216\"],\"city\":\"London\",\"country\":\"uk\"}]},\"creditor\":{\"account\":{\"id\":\"GB123456789123456789\"},"
           "\"name\":\"British Electricity Ltd\",\"postalAddresses\":[{\"city\":\"Manchester\",\"country\":\"uk\"}]}}}]}")

headers = {
    'content-type': "application/json",
    'Authorization': f"Bearer {acces_token}"
    }



def make_request(method, url, payload, headers=headers):
    conn.request(method, url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    return data


# Screening of a transaction
# ?validate = False pass the value False to the validate parameter
#make_request("POST", "/api/v1/jetflow/screen/sanctions?validate=False", payload, headers)


# Create a session
#make_request("GET", "/api/v1/core/sessions/new", payload=None, headers=headers)

# Get watchlists available in our servers
#make_request("GET", "/api/v1/core/repository/lists", payload=None, headers=headers)

# Get regions
make_request("GET", "/api/v1/core/repository/regions", payload=None, headers=headers)

# Get sanctions
#make_request("GET", "/api/v1/core/repository/lists/EU/sanctions", payload=None, headers=headers)

# Get sanctions for a country
make_request("GET", "/api/v1/core/repository/lists/OFAC/sanctions/us", payload=None, headers=headers)

