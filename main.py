import requests
import os

URL= 'https://api.github.com/repos/shradaya/GA-2/dispatches'
Headers= {
    'Authorization': f"Bearer {os.environ['REPOSITORY_TOKEN']}",
    'Accept': 'application/vnd.github.v3+json',
    'Content'-Type: 'application/json',
}
Body= {
    'event_type': 'custom_event_type'
}


requests.post(URL, data=Body, headers=Headers)