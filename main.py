import os
from PIL import Image, ExifTags
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8000
GALLERY_HTML = "gallery.html"
THUMB_FOLDER = "thumbs"
SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")
THUMB_WIDTH = 300
THUMB_HEIGHT = 200

# === Get photo names ===
photos = [f for f in os.listdir() if f.lower().endswith(SUPPORTED_EXTENSIONS)]

# === Create thumbs folder ===
os.makedirs(THUMB_FOLDER, exist_ok=True)

# === Create thumbnails and compress ===
for photo in photos:
    thumb_path = os.path.join(THUMB_FOLDER, photo)
    if not os.path.exists(thumb_path):
        try:
            # Open the original image
            img = Image.open(photo)

            # Check EXIF data and adjust orientation
            if hasattr(img, '_getexif'):  # Check if EXIF data exists
                exif = img._getexif()
                if exif is not None:
                    for tag, value in exif.items():
                        if tag == 274:  # Orientation EXIF tag
                            if value == 3:
                                img = img.rotate(180, expand=True)
                            elif value == 6:
                                img = img.rotate(270, expand=True)
                            elif value == 8:
                                img = img.rotate(90, expand=True)

            # Resize the image to create thumbnail
            img.thumbnail((THUMB_WIDTH, THUMB_HEIGHT))

            # Save the thumbnail
            img.save(thumb_path, "JPEG", quality=85)
            print(f"[+] Thumbnail created: {photo}")
        except Exception as e:
            print(f"[!] Error ({photo}): {e}")

# === Create the gallery HTML file ===
html_code = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Photo Gallery</title>
  <style>
    body {
      font-family: sans-serif;
      background: #111;
      color: white;
      text-align: center;
    }
    h1 {
      margin: 20px;
    }
    .gallery {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 10px;
      padding: 20px;
    }
    .gallery img {
      width: 200px;
      height: 150px;
      object-fit: cover;
      border-radius: 10px;
      cursor: pointer;
      transition: 0.3s;
    }
    .gallery img:hover {
      transform: scale(1.05);
    }
    #modal {
      display: none;
      position: fixed;
      z-index: 10;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0,0,0,0.8);
      justify-content: center;
      align-items: center;
    }
    #modal img {
      max-width: 90vw;
      max-height: 90vh;
      border-radius: 10px;
    }
  </style>
</head>
<body>
  <h1>🖼️ My Gallery</h1>
  <div class="gallery" id="gallery"></div>

  <div id="modal" onclick="this.style.display='none'">
    <img id="modal-img" src="" />
  </div>

  <script>
    const images = """ + str(photos) + """;  // Photos are added automatically

    const gallery = document.getElementById("gallery");
    const modal = document.getElementById("modal");
    const modalImg = document.getElementById("modal-img");

    images.forEach(src => {
      const thumbSrc = "thumbs/" + src;  // Thumbnails are in 'thumbs' folder
      const img = document.createElement("img");
      img.src = thumbSrc;
      img.alt = src;
      img.onclick = () => {
        modal.style.display = "flex";
        modalImg.src = src;  // Show the original photo when clicked
      };
      gallery.appendChild(img);
    });
  </script>
</body>
</html>
"""

# === Save the HTML file ===
with open(GALLERY_HTML, "w", encoding="utf-8") as f:
    f.write(html_code)

print(f"\n[✔] {GALLERY_HTML} file created → total {len(photos)} photos")

# === Start the HTTP server ===
server_address = ("", PORT)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print(f"[🚀] Server started → http://localhost:{PORT}/gallery.html")
httpd.serve_forever()
