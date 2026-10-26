# OpenCV Document Scanner

## Overview
A computer vision utility built with Python and OpenCV to automatically detect document boundaries, apply perspective transformations, and enhance text readability from scanned images.

## Architecture & Pipeline
1. **Image Preprocessing**: Grayscale conversion, Gaussian blurring, and Canny edge detection.
2. **Contour Detection**: Identifies external contours and approximates polygonal curves to locate 4-corner document boundaries (`cv2.findContours`, `cv2.approxPolyDP`).
3. **Perspective Transform**: Applies a 4-point perspective warp (`utils.py`) to obtain a top-down view of the document.
4. **Text Enhancement**: Thresholding and binarization to darken and clean document text.

## Data
- **Input**: Raw document images (`document.jpg`).

## Method & Algorithms
- **Edge Detection**: Canny edge detector combined with contour sorting by area.
- **Geometric Transformation**: Homography / 4-point perspective warping to rectify angled document photographs.

## Verified Results & Metrics
- Successfully detects rectangular document edges and produces cleaned, top-down perspective-corrected document scans.

## Limitations & Caveats
- Requires reasonably well-lit input images with clear contrast against background surfaces.

## Run Instructions
```bash
python scanner.py
```

## CV Bullet Points
- Developed an automated document scanner in Python using OpenCV, implementing Canny edge detection, contour approximation, and 4-point perspective transformation.
- Enhanced document readability through image thresholding and binarization pipelines.

## Claims to Avoid
- Do not claim production-grade OCR or deep learning document parsing.
