import cv2

def change_aspect_ratio(image_path, new_width, new_height):
  """Changes the aspect ratio of an image while maintaining its content.

  Args:
    image_path (str): Path to the image file.
    new_width (int): Desired width of the resized image.
    new_height (int): Desired height of the resized image.

  Returns:
    numpy.ndarray: The resized image with the new aspect ratio.
  """

  img = cv2.imread(image_path)

  # Get original image dimensions
  original_height, original_width, _ = img.shape

  # Calculate scaling factors for both width and height
  width_scale = new_width / original_width
  height_scale = new_height / original_height

  # Determine the appropriate scaling factor to maintain content
  scaling_factor = min(width_scale, height_scale)

  # Calculate new dimensions based on the chosen scaling factor
  new_dimensions = (int(original_width * scaling_factor),
                     int(original_height * scaling_factor))

  # Resize the image while preserving aspect ratio
  resized_img = cv2.resize(img, new_dimensions, interpolation=cv2.INTER_AREA)

  return resized_img

# Example usage:
image_path = "path/to/your/image.jpg"
new_width = 640  # Adjust as needed
new_height = 480  # Adjust as needed

resized_img = change_aspect_ratio(image_path, new_width, new_height)

# Display or save the resized image:
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To save the resized image:
cv2.imwrite("resized_image.jpg", resized_img)

