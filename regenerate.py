import time
import os
import json
from art_manager import load_from_filepath

def generate_button(tag):
    return f"""
            <button data-filter="{tag}">{tag.replace('_',' ')}</button>"""
    
def generate_filter_buttons(tags):
    return_string = """
        <div class="filters">
            <button data-filter="all">All</button>"""
    for tag in tags:
        return_string+=generate_button(tag)
    return_string += "</div>"
    return return_string

def generate_artwork_block(image_name,title,year,medium,available,extra_tags = []):
    medium_string = medium.replace('_',' ')
    tag_string = ' '.join([medium,available]+extra_tags)
    return f"""
    <div class="artwork" data-tags="{tag_string}">
        <button class="artwork-button"
                data-title="{title}"
                data-meta="{medium_string} · {year}"
                data-image="images/{image_name}">
        <img src="images/{image_name}" alt="{title}">
        </button>
        <h3>{title}</h3>
        <p>{medium_string} · {year}</p>
    </div>
  """

def generate_gallery(folder):
    all_tags = set()
    json_dumps = []
    return_string = """
    <main class="gallery">"""
    for filename in os.listdir(folder):
            artwork_dict = load_from_filepath(filename)
            json_dumps.append(artwork_dict)

            return_string+=generate_artwork_block(filename,
                                                  artwork_dict['title'],
                                                  artwork_dict['year'],
                                                  artwork_dict['medium'],
                                                  artwork_dict['available'],
                                                  artwork_dict['extra_tags']) 
            all_tags.update([artwork_dict['medium'],
                             artwork_dict['available'],
                             artwork_dict['collection']]+artwork_dict['extra_tags'])
            
    return_string += "</main>"
    print(all_tags)
    with open('artworks.json', 'w', encoding='utf-8') as f:

        json.dump(json_dumps, f, ensure_ascii=False, indent=4)
    return return_string,all_tags

def lightbox():
     return """

<div class="lightbox" aria-hidden="true">
  <div class="lightbox-content" role="dialog" aria-modal="true">
    <button class="lightbox-close" aria-label="Close artwork">×</button>

    <img class="lightbox-image" src="" alt="">
    <h2 class="lightbox-title"></h2>
    <p class="lightbox-meta"></p>
  </div>
</div>
"""

def footer():
     this_year = time.localtime().tm_year
     return f"""
<footer>
  © {this_year} Gael Jay. All artwork protected.
</footer>
</html>
"""

def header():
    return """
<!DOCTYPE html>
<html>
  <head>
    <title>Art Portfolio</title>
    <link rel="stylesheet" href="css/style.css">
    <script src="js/filter.js" defer></script>
    <script src="js/lightbox.js" defer></script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta property="og:title" content="Gael Jay's Portfolio" />
    <meta property="og:image" content="https://gaelart.github.io/preview.jpg" />
    <meta property="og:description" content="Online gallery of traditional artist Gael Jay." />
  </head>
  """

def body():
     gallery,tags = generate_gallery('images')
     return f"""
<body>

    <div class="bigtitle">Gallery</div>
{generate_filter_buttons(tags)}
{gallery}
{lightbox()}

  """

def generate_full_page(filename='index.html'):

    with open(filename, 'w',encoding="utf-8") as f:
        f.write(header() + body() + footer())
    return header() + body() + footer() 

if __name__ == "__main__":
    generate_full_page()