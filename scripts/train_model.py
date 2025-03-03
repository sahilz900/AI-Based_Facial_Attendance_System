from deepface import DeepFace
import os
import pickle

if not os.path.exists("models"):
    os.makedirs("models")

known_encodings = []
known_names = []

for filename in os.listdir("images"):
    if filename.endswith(".jpg"):
        name = filename.split("_")[0]  
        img_path = f"images/{filename}"

        try:
            embedding = DeepFace.represent(img_path, model_name="VGG-Face", enforce_detection=False)
            if embedding:
                known_encodings.append(embedding[0]["embedding"])
                known_names.append(name)
        except:
            print(f"⚠️ Skipping {filename}, face not detected!")

if known_encodings:
    data = {"encodings": known_encodings, "names": known_names}
    with open("models/face_encodings.pickle", "wb") as f:
        pickle.dump(data, f)
    print("✅ Model trained successfully!")
else:
    print("❌ No valid images found. Training failed.")
