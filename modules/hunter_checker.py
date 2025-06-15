import requests

def search_hunter(domain):
    api_key = "YOUR_HUNTER_API_KEY"  # Replace with your real Hunter.io API key
    url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if "data" in data and "emails" in data["data"]:
            emails = data["data"]["emails"]
            results = [f"{email['value']} ({email['type']})" for email in emails]
            return "\n".join(results) if results else "No emails found."
        else:
            return "Invalid response or no emails found."
    except Exception as e:
        return f"Error: {str(e)}"