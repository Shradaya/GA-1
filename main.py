import requests

URL= 'https://api.github/com/repos/shradaya/GA-2/dispatches'
Headers= {
    'Authorization': 'Bearer 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',
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json',
}
Body= {
    'event_type': 'custom_event_type'
}


requests.post(URL, data=Body, headers=Headers)