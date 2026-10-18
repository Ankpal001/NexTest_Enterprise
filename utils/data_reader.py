import json
from pathlib import Path

#C:\Users\Ankit\Desktop\NexTest_Enterprise\test_data\login_data.json
PROJECT_ROOT = Path(__file__).resolve().parent.parent
def read_json(file_name):
    file_path = PROJECT_ROOT/"test_data"/ file_name
    with file_path.open("r", encoding="utf-8") as file:
         return json.load(file)
