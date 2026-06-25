import platform
from datetime import datetime

print("========== Dockerized Python Application ==========")
print(f"Python Version : {platform.python_version()}")
print(f"Current Date   : {datetime.now().strftime('%d-%m-%Y')}")
print(f"Current Time   : {datetime.now().strftime('%H:%M:%S')}")