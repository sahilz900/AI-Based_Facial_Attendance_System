from deepface import DeepFace
import cv2
import pandas as pd
import datetime
import os
import pickle

with open("models/face_encodings.pickle", "rb") as f:
    data = pickle.load(f)

known_encodings = data["encodings"]
known_names = data["names"]

cap = cv2.VideoCapture(0)

attendance_file = "attendance.xlsx"
if not os.path.exists(attendance_file):
    df = pd.DataFrame(columns=["Name", "Date", "Time"])
    df.to_excel(attendance_file, index=False)

df = pd.read_excel(attendance_file)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Could not read frame.")
        break

    try:
        result = DeepFace.find(frame, db_path="images/", enforce_detection=False)
        if len(result) > 0:
            
            name = os.path.basename(result[0]['identity'][0]).split("_")[0]
            today = datetime.datetime.now().strftime("%Y-%m-%d")

            if not ((df["Name"] == name) & (df["Date"] == today)).any():
                print(f"✅ Marking attendance for: {name}")

                now = datetime.datetime.now()
                new_entry = {"Name": name, "Date": today, "Time": now.strftime("%H:%M:%S")}
                df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
                df.to_excel(attendance_file, index=False)
            else:
                print(f"⏳ {name} is already marked present today.")
    except:
        pass

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

