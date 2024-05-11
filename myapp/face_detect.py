def detect_face(img):
    import cv2

    cascPath = r"D:\my_main_project\final\GlowStyle\GlowStyle\myapp\haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    image = img
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30)
    )

    print("Found {0} faces !".format(len(faces)))

    sub_face = None  # Initialize sub_face to None

    for(x,y,w,h) in faces:
        cv2.rectangle(image, (x,y),(x+w,y+h),(255,255,255),0)
        sub_face = image[y:y+h, x:x+w]
        # Do something with sub_face here if needed

    del cv2
    return sub_face
