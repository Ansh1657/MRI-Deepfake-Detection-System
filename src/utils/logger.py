import os
import datetime

def log_user_data(original_image, processed_image, task_name):
    """Saves uploaded and generated images locally for audit/logging purposes."""
    log_dir = os.path.join("user_uploads", datetime.datetime.now().strftime("%Y-%m-%d"))
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%H%M%S")
    
    if original_image:
        original_image.save(os.path.join(log_dir, f"{timestamp}_{task_name}_original.png"))
    if processed_image:
        processed_image.save(os.path.join(log_dir, f"{timestamp}_{task_name}_processed.png"))
