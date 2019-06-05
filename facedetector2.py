import cv2
# imagePath = sys.argv[1]
# cascPath = sys.argv[2]
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread("/home/satyam/Desktop/python/images/news.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)
print(("Found {0} faces!").format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 3)

# img = cv2.resize(image,(int(image.shape[1]/3),int(image.shape[0]/3)))
cv2.imshow("Faces found", image)
cv2.waitKey(0)
