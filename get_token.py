import requests
import json



class Token:
    def __init__(self):
        self.url = 'https://connect-to.neterium.cloud/demo/token'
        self.data = {
            'username': 'corentin.denis@neterium.io',
            'password': 'g6@doXnEMtGs8xx#',
            'grant_type': 'password',
            'client_id': 'api'
        }
        self.filename = "token.json"
        with open(self.filename, 'r+') as f:
            self.token_access = json.load(f)["access_token"]

    def _send_token_request(self):
        response = requests.post(self.url, data=self.data)
        json_response = response.json()
        print(f"Status code: {response.status_code}")
        print(f"json response: {json_response}")
        return json_response


    def _del_file_content(self):
        with open(self.filename, "r+") as f:
            f.seek(0)
            f.truncate()

    def _update_file_content(self):
        self._del_file_content()
        token = self._send_token_request()
        with open(self.filename, "r+") as f:
            json.dump(token, f)
        self.token_access = token["access_token"]


    def get_token(self, renew_token=False):
        if renew_token:
            self._update_file_content()
            return self.token_access
        else:
            return self.token_access  # Jason response

"""# Afficher la réponse
response = 
print(response.status_code)
print(response.json())"""
