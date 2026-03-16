import cv2
import os

name = input("Enter person name: ")

path = "database"

cap = cv2.VideoCapture(0)

count = 0

print("Capturing images...")

while count < 20:

    ret, frame = cap.read()

    cv2.imshow("Register Face",frame)

    file_path = os.path.join(path,f"{name}_{count}.jpg")

    cv2.imwrite(file_path,frame)

    count += 1

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()

print("Face Registered Successfully")