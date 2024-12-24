import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


JSON_FILE_all_sub_breeds = get_path(filename="all_sub_breeds.json")
JSON_FILE_all_breeds = get_path(filename="all_breeds.json")
JSON_FILE_all_images = get_path(filename="all_images.json")
JSON_FILE_breweries_id = get_path(filename="breweries_id.json")