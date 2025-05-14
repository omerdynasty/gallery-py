# Photo Gallery with Thumbnails (Python)

This project creates a simple photo gallery where images are displayed with thumbnails. It generates thumbnails for each supported image in the directory, stores them in a "thumbs" folder, and creates an HTML gallery. The gallery allows you to click on thumbnails to view the full-size image.

## Features

* Automatically generates thumbnails for images in supported formats (`.jpg`, `.jpeg`, `.png`, `.webp`).
* The gallery is fully responsive and displays images in a clean and simple layout.
* Clicking a thumbnail opens the full-size image in a modal.
* Built with Python and the `PIL` (Pillow) library for image processing.

## Installation

1. **Clone the repository** or download the project files to your local machine.

2. **Install the required libraries**:
   You will need the `Pillow` library for image processing. Install it using `pip`:

   ```bash
   pip install Pillow
   ```

3. **Prepare your photos**:
   Place your photos (with supported extensions like `.jpg`, `.jpeg`, `.png`, `.webp`) in the same directory as the script.

4. **Run the Python script**:
   Run the following Python script:

   ```bash
   python main.py
   ```

   This will create a `gallery.html` file and a `thumbs` folder containing the thumbnails. The gallery will be accessible on `http://localhost:8000/gallery.html`.

## Usage

After running the script, the `gallery.html` file will be automatically created. The Python server will start, and you can access the gallery by opening your browser and navigating to:

```
http://localhost:8000/gallery.html
```

The gallery will display images in thumbnails. When you click on a thumbnail, the full-size image will be shown in a modal.

## Configuration

* **Thumbnail Size**: You can adjust the thumbnail size by modifying the following variables in the script:

  ```python
  THUMB_WIDTH = 300
  THUMB_HEIGHT = 200
  ```

* **Supported Image Formats**: The following image formats are supported by default:

  ```python
  SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")
  ```

  You can modify this list to include other image formats if needed.

## Contributing

Feel free to fork this repository and submit issues or pull requests if you have any suggestions or improvements.

## License

This project is open-source and available under the [GPL v3](LICENSE).
