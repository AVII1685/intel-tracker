import subprocess

def run_phoneinfoga(phone_number):
    try:
        # PhoneInfoga binary path
        cmd = [
            './modules/phoneinfoga/phoneinfoga.exe',
            'scan',
            '-n', phone_number,
            '--json'
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"

    except Exception as e:
        return f"Exception occurred: {str(e)}"