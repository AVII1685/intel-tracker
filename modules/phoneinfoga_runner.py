import subprocess

def run_phoneinfoga(phone_number):
    try:
        # PhoneInfoga ko CLI se run kar rahe hain
        result = subprocess.run(
            ["python", "PhoneInfoga/phoneinfoga.py", "-n", phone_number],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"PhoneInfoga error: {str(e)}"

# Test ke liye direct run
if __name__ == "__main__":
    phone = input("Enter phone number: ")
    print(run_phoneinfoga(phone))