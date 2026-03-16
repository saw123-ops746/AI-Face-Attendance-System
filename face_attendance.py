import cv2
from deepface import DeepFace
import pandas as pd
from datetime import datetime
import os
import time

# =========================
# SETTINGS
# =========================

database_path = "database"
attendance_file = "attendance.xlsx"
camera_time = 30   # seconds camera chalega


# =========================
# CREATE EXCEL FILE
# =========================

if not os.path.exists(attendance_file):
    df = pd.DataFrame(columns=["Name","Date","Time"])
    df.to_excel(attendance_file, index=False)


# =========================
# START CAMERA
# =========================

cap = cv2.VideoCapture(0)

start_time = time.time()

print("Camera Started...")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        break

    try:

        result = DeepFace.find(
            img_path=frame,
            db_path=database_path,
            enforce_detection=False
        )

        if len(result) > 0 and len(result[0]) > 0:

            identity = result[0]['identity'][0]

            name = identity.split("\\")[-1].split(".")[0]

            now = datetime.now()

            date = now.strftime("%d-%m-%Y")
            current_time = now.strftime("%H:%M:%S")

            df = pd.read_excel(attendance_file)

            new_row = {
                "Name": name,
                "Date": date,
                "Time": current_time
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

            df.to_excel(attendance_file, index=False)

            cv2.putText(frame,
                        f"Recognized: {name}",
                        (30,50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0,255,0),
                        2)

        else:

            cv2.putText(frame,
                        "Unknown",
                        (30,50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0,0,255),
                        2)

    except:
        cv2.putText(frame,
                    "Scanning...",
                    (30,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255,255,0),
                    2)

    cv2.imshow("AI Face Attendance", frame)

    # ESC press to exit
    if cv2.waitKey(1) == 27:
        break

    # Auto close after time
    if time.time() - start_time > camera_time:
        print("Camera auto closed")
        break


cap.release()
cv2.destroyAllWindows()

print("Attendance Saved in Excel")
import cv2
from deepface import DeepFace
import pandas as pd
from datetime import datetime
import os

database_path = "database"
attendance_file = "attendance.xlsx"

if not os.path.exists(attendance_file):
    df = pd.DataFrame(columns=["Name","Date","Time"])
    df.to_excel(attendance_file,index=False)

cap = cv2.VideoCapture(0)

print("Camera Started...")

while True:

    ret, frame = cap.read()

    try:

        result = DeepFace.find(
            img_path = frame,
            db_path = database_path,
            model_name="ArcFace",
            enforce_detection=False
        )

        if len(result) > 0 and len(result[0]) > 0:

            identity = result[0]['identity'][0]

            name = os.path.basename(identity).split(".")[0]

            now = datetime.now()

            date = now.strftime("%d-%m-%Y")
            time = now.strftime("%H:%M:%S")

            df = pd.read_excel(attendance_file)

            new_row = {
                "Name":name,
                "Date":date,
                "Time":time
            }

            df = pd.concat([df,pd.DataFrame([new_row])],ignore_index=True)

            df.to_excel(attendance_file,index=False)

            cv2.putText(frame,name,(50,50),
                        cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

    except:
        pass

    cv2.imshow("AI Attendance System",frame)

    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()