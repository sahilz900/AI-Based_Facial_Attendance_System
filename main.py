import os

def main():
    while True:
        print("\n🎯 Face Recognition Attendance System")
        print("1. Capture Faces")
        print("2. Train Model")
        print("3. Recognize Faces & Mark Attendance")
        print("4. Export Attendance to Excel")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            os.system("python scripts/capture_faces.py")
        elif choice == "2":
            os.system("python scripts/train_model.py")
        elif choice == "3":
            os.system("python scripts/recognize_faces.py")
        elif choice == "4":
            os.system("python scripts/export_attendance.py")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
