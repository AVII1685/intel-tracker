import subprocess

def run_phoneinfoga(phone_number):
    try:
        # Run phoneinfoga as a subprocess
        result = subprocess.run(
            ["./modules/phoneinfoga/phoneinfoga.exe", "scan", "-n", phone_number],
            capture_output=True, text=True
        )
        return result.stdout if result.stdout else "No output from PhoneInfoga."
    except Exception as e:
        return f"Error running PhoneInfoga: {str(e)}"