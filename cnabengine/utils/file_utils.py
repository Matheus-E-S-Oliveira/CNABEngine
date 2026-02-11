import os
from datetime import datetime

def generate_log_filename(original_file: str) -> str:
    base_name = os.path.splitext(os.path.basename(original_file))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"logs/{base_name}_{timestamp}.log"