import json
import os
from PIL import Image

def load_from_filepath(filepath:str) -> dict:
    """
    loads the artwork from the json file and returns a list of dictionaries with the artwork information.
    """
    collection = "none"
    extra_tags = []
    filename = os.path.basename(filepath)
    parts = filename.split(".")[0].split("-")
    print(parts)
    title = parts[0].replace("_"," ")
    year = parts[1]
    medium = parts[2] 
    if "oil" in medium:
        medium = "oil"
    elif "acrylics" in medium:
        medium = "acrylics"
    available = parts[3]
    if len(parts) > 4:
        collection = parts[4].lower()
    if len(parts) > 5:
        extra_tags = [i.lower() for i in parts[5:]]
    return {

        "title": title, 
        "year": year,
        "medium": medium,
        "available": available,
        "collection": collection,
        "extra_tags": extra_tags,
        "file_path": filepath    
    }

def save_artwork(artwork_dict:dict) -> None:
    """
    saves the artwork information in the dictionary to a json file and renames the artwork file.
    """
    title = artwork_dict["title"].replace(" ","_").capitalize()
    year = artwork_dict["year"]
    medium = artwork_dict["medium"]
    available = artwork_dict["available"]
    collection = artwork_dict["collection"]
    extra_tags = "_".join(artwork_dict["extra_tags"])
    new_filename = f"{title}-{year}-{medium}-{available}"
    if collection != "none":
        new_filename += f"-{collection}"
    if extra_tags != "":
        new_filename += f"-{extra_tags}"
    data = preprocess_artwork(artwork_dict["file_path"])
    new_filename += ".jpg"
    with open(f"images/{new_filename}", "wb") as f:
        data.save(f, format="JPEG")
    


def preprocess_artwork(file_path:str)-> bytes: 
    """
    preprocesses the artwork by:
    - getting the maximum between the width and height of the image
    - resizing it to a maximum width or height of 1000px
    - converting it to jpg if it"s not already
    """

    img = Image.open(file_path)
    max_dimension = max(img.size)
    if max_dimension > 1000:
        scale_factor = 1000 / max_dimension
        new_size = (int(img.size[0] * scale_factor), int(img.size[1] * scale_factor))
        img = img.resize(new_size)
    if img.format != "JPEG":
        img = img.convert("RGB")
    return img