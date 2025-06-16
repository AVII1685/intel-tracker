def generate_google_dorks(phone_number):
    dorks = [
        f'site:naukri.com "{phone_number}"',
        f'site:linkedin.com/in "{phone_number}"',
        f'site:workindia.in "{phone_number}"',
        f'filetype:pdf "{phone_number}"',
        f'"{phone_number}" site:facebook.com',
        f'"{phone_number}" site:instagram.com',
        f'"{phone_number}" site:justdial.com',
        f'"{phone_number}" site:github.com',
    ]
    return dorks