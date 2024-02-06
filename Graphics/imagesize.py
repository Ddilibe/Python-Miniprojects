import cv2
import numpy as np

def get_sectional_cut(image_path, start_point, end_point, thickness=1):
    """Extracts a sectional cut of a picture.

    Args:
        image_path (str): Path to the image file.
        start_point (tuple): (x, y) coordinates of the starting point of the cut.
        end_point (tuple): (x, y) coordinates of the ending point of the cut.
        thickness (int, optional): Thickness of the cut line. Defaults to 1.

    Returns:
        numpy.ndarray: The extracted sectional cut of the image.
    """

    img = cv2.imread(image_path)

    # Get image dimensions
    height, width, _ = img.shape

    # Ensure start and end points are within image boundaries
    start_point = np.clip(start_point, 0, (width-1, height-1))
    end_point = np.clip(end_point, 0, (width-1, height-1))

    # Create a mask for the cut region
    mask = np.zeros_like(img)
    cv2.line(mask, start_point, end_point, (255, 255, 255), thickness)

    # Apply the mask to the image
    cut_image = cv2.bitwise_and(img, mask)

    return cut_image

# Example usage:
image_path = "path/to/your/image.jpg"
start_point = (100, 50)  # Adjust as needed
end_point = (300, 200)   # Adjust as needed

cut_image = get_sectional_cut(image_path, start_point, end_point)

# Display or save the cut image:
cv2.imshow("Sectional Cut", cut_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To save the cut image:
cv2.imwrite("sectional_cut.jpg", cut_image)

