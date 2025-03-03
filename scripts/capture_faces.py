import cv2
import os

name = input("Enter the person's name: ")

person_folder = os.path.join("images", name)
os.makedirs(person_folder, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0
while count < 50:
    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Could not read frame from camera.")
        break

    image_path = os.path.join(person_folder, f"{name}_{count}.jpg")
    cv2.imwrite(image_path, frame)
    count += 1

    cv2.imshow("Capturing Faces", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"✅ 50 images captured and stored in '{person_folder}' successfully!")
