# pip install opencv - python

# to read image
import cv2

# Configurable parameters
source = "MyImage.jpeg"
destination = "newMyImage.jpeg"
# percent by which the image is resized
scale_percent = 70

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
cv2.waitKey(0)




# calculate the 50 percent of original dimension
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# create tuple
dsize = (new_width, new_height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination, output)
