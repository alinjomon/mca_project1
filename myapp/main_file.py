from . import face_detect
from . import kMeansImgPy
import cv2
from . import allotSkinTone

imgpath = input("Image file name : ")
image = cv2.imread(imgpath)

# Detect face and extract
face_extracted = face_detect.detect_face(image)
# Pass extracted face to kMeans and get Max color list
colorsList = kMeansImgPy.kMeansImage(face_extracted)

print("Main File : ")
print("Red Component : "+str(colorsList[0]))
print("Green Component : "+str(colorsList[1]))
print("Blue Component : "+str(colorsList[2]))

# Allot the actual skinTone to a certain shade
allotedSkinToneVal = allotSkinTone.allotSkin(colorsList)
print("alloted skin tone : ")
print(allotedSkinToneVal)

tones = [
    "tone1",
    "tone2",
    "tone3",
    "tone4",
    "tone5",
]
colors = [
    [59, 34, 25],  # tone1
    [161, 110, 75],  # tone2
    [212, 170, 120],  # tone3
    [230, 188, 152],  # tone4
    [255, 231, 209]  # tone5
]
mindex=colors.index(allotedSkinToneVal)
print(tones[mindex])
