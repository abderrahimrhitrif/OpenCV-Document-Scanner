# OpenCV Document Scanner

## Overview

The OpenCV Document Scanner is a Python project that uses OpenCV to scan documents from images. It detects the contours of a document in an image, applies a perspective transformation to get a top-down view, and processes the scanned document for enhanced readability. The final scanned image is saved with a timestamp.

## Files

### 1. `scanner.py`
This script performs the following steps:
- **Image Loading and Resizing**: Loads an image from the file `document.jpg` and resizes it to a standard size.
- **Preprocessing**: Converts the image to grayscale and applies Gaussian blur to reduce noise.
- **Edge Detection**: Detects edges in the blurred image using the Canny edge detection algorithm.
- **Contour Detection**: Finds contours in the edge-detected image and identifies the document by approximating the contour with four points.
- **Perspective Transform**: Applies a perspective transformation to the detected document to obtain a top-down view.
- **Post-Processing**: Enhances the visibility of the document by making the text stand out more.
- **Saving the Scanned Document**: Saves the processed document with a timestamp in the `./Scanned` directory.

### 2. `utils.py`
Contains utility functions used by `scanner.py`:
- **`order_points(pts)`**: Reorders a list of four points in a consistent order (top-left, top-right, bottom-right, bottom-left).
- **`four_points_transform(image, pts)`**: Applies a perspective transformation to the image based on the four provided points.

## Setup

### Requirements
- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)

### Installation
To run this project, you need to install the required libraries:

```bash
pip install opencv-python-headless numpy
```

## Usage

1. Place the image you want to scan in the same directory as `scanner.py` and name it `document.jpg`.
2. Run the `scanner.py` script:

   ```bash
   python scanner.py
   ```

3. The processed and scanned document will be displayed and saved in the `./Scanned` directory with a filename like `scanned_YYYYMMDD_HHMMSS.jpg`.

## Customization

- **Enhancing Text Visibility**: Uncomment the line in `scanner.py` that adjusts the contrast to make the document text darker and more defined:

  ```python
  # warped_gray = cv2.convertScaleAbs(warped_gray, alpha=1.5, beta=-100)
  ```

## License

This project is open-source and available under the MIT License. Feel free to modify and use it as needed.
