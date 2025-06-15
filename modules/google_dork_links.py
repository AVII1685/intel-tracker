def run_google_dork_links(phone_number):
    try:
        dorks = [
            f'"{phone_number}" site:facebook.com',
            f'"{phone_number}" site:linkedin.com',
            f'"{phone_number}" site:twitter.com',
            f'"{phone_number}" site:instagram.com',
            f'"{phone_number}" site:truecaller.com',
            f'"{phone_number}" site:pastebin.com',
            f'"{phone_number}" site:whois.domaintools.com'
        ]
        google_urls = [f"https://www.google.com/search?q={dork}" for dork in dorks]
        return "\n".join(google_urls)
    except Exception as e:
        return f"Google Dork Error: {str(e)}"