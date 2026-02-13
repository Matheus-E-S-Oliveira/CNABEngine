import os
from datetime import datetime


def generate_log_filename(original_file: str) -> str:
    base_name = os.path.splitext(os.path.basename(original_file))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("logs", exist_ok=True)
    log_dir = "logs"
    return os.path.join(log_dir, f"{base_name}_{timestamp}.log")