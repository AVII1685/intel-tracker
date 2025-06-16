import subprocess
import os

def run_phoneinfoga(phone_number):
    try:
        # If server is Linux (Render), return message
        if os.name != 'nt':
            return "PhoneInfoga cannot be executed in this server environment (Linux)."

        result = subprocess.check_output([
            "modules/phoneinfoga/phoneinfoga.exe", "scan", "-n", phone_number
        ], stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"PhoneInfoga error:\n{e.output}"
    except FileNotFoundError:
        return "PhoneInfoga executable not found. Please make sure phoneinfoga.exe exists."
    except Exception as e:
        return f"Unexpected error: {str(e)}"