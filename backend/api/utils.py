import os
import uuid
from backend.settings import MEDIA_ROOT

def verify_video_file_extension_is_ok(video_file) -> bool:
    file_extension = os.path.splitext(video_file.name)[1].lower()
    if file_extension in ['.mp4', '.avi', '.mov', '.mkv', '.webm']:
        return True
    
    return False


def create_dir_to_files(name: str) -> None:
    upload_dir = os.path.join(MEDIA_ROOT, name)
    os.makedirs(upload_dir, exist_ok=True)
    return upload_dir

def save_video_file(video_file) -> None:
    
    try:
        upload_dir = create_dir_to_files("videos")

        file_extension = os.path.splitext(video_file.name)[1]
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        file_path = os.path.join(upload_dir, unique_filename)

        with open(file_path, 'wb+') as destination:
            for chunk in video_file.chunks():
                destination.write(chunk)  
        return unique_filename

    except Exception:
        return False