import requests
import os

URL= 'https://api.github.com/repos/shradaya/GA-2/dispatches'
Headers= {
    'Authorization': f"Bearer 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", #{os.environ['REPOSITORY_TOKEN']}",
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json',
}
Body= {
    'event_type': 'custom_event_type'
}


response = requests.post(URL, json=Body, headers=Headers)
print(response)
