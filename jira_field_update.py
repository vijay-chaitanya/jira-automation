import requests
from requests.auth import HTTPBasicAuth

# Jira details
JIRA_DOMAIN = "liveramp.atlassian.net"
API_TOKEN = "yATATT3xFfGF0ta_rEZQUYFUqUABAPfX1rfnZBzyq4231Kij8XuUXD2fE8B2s7NfpLKXGpAzJZWfn4Xo7oueXlVJVacz_SP-k_junKcstp0j_3CmdK4aoK87VUngWk-M0zJyQ8fcsrVUlsUjiDF0HnZLiY08FlRx7ZLqDEQ0_KBcHHjrmBd56t3Q=565C4C74"
EMAIL = "chaitanyavijay.dola@liveramp.com"
#issue_key = "PROJECT-123"
JQL_QUERY = "project=OC AND statusCategory=Done ORDER BY created DESC"

# API Endpoint
url = f"https://{JIRA_DOMAIN}/rest/api/3/search?jql={JQL_QUERY}"
print(url)

# Headers
headers = {
    "Accept": "application/json"
}

# Make the request
response = requests.get(url, headers=headers, auth=HTTPBasicAuth(EMAIL, API_TOKEN))

# Print JSON response
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code, response.text)
