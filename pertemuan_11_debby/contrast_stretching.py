import cv2
import numpy as np

def contrast_stretching(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the minimum and maximum pixel values
    min_val = np.min(gray)
    max_val = np.max(gray)

    # Perform contrast stretching
    stretched = cv2.convertScaleAbs(gray, alpha=(255.0 / (max_val - min_val)), beta=(-min_val * (255.0 / (max_val - min_val))))

    return stretched

# Load the image
image = cv2.imread('51.jpeg')

# Apply contrast stretching
stretched_image = contrast_stretching(image)

# Display the original and stretched images
cv2.imshow('Original Image', image)
cv2.imshow('Contrast Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()