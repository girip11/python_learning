import requests

resp = requests.get("https://httpstat.us/200")

print(resp.status_code)
for header in resp.headers:
    print(f"{header}: {resp.headers[header]}")
