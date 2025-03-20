import os
import cv2
import face_recognition
import pickle
import numpy as np

# === CẤU HÌNH THƯ MỤC ===
IMAGE_FOLDER = "dataset_khautr"  # Thư mục chứa ảnh đeo khẩu trang
ENCODED_FOLDER = "encoded_khautr"  # Thư mục lưu đặc điểm khuôn mặt đã trích xuất

# === BƯỚC 1: TRÍCH XUẤT ĐẶC ĐIỂM KHUÔN MẶT ===
def extract_face_encodings():
    if not os.path.exists(ENCODED_FOLDER):
        os.makedirs(ENCODED_FOLDER)

    known_face_encodings = []
    known_face_names = []

    files = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.jpg', '.png', '.jpeg'))]
    if not files:
        print("❌ Không tìm thấy ảnh trong thư mục!")
        return

    for filename in files:
        path = os.path.join(IMAGE_FOLDER, filename)
        print(f"🖼 Đang xử lý ảnh: {filename}...")

        image = face_recognition.load_image_file(path)
        face_encodings = face_recognition.face_encodings(image)

        if face_encodings:
            encoding = face_encodings[0]
            name = os.path.splitext(filename)[0]

            known_face_encodings.append(encoding)
            known_face_names.append(name)

            with open(os.path.join(ENCODED_FOLDER, f"{name}.pkl"), "wb") as f:
                pickle.dump({"name": name, "encoding": encoding}, f)

            print(f"✔ Đã lưu khuôn mặt của '{name}'.")

    print(f"✅ Đã trích xuất {len(known_face_encodings)} khuôn mặt từ '{IMAGE_FOLDER}'.")

# === BƯỚC 2: NHẬN DIỆN KHUÔN MẶT TỪ CAMERA ===
def recognize_faces():
    known_face_encodings = []
    known_face_names = []

    encoded_files = [f for f in os.listdir(ENCODED_FOLDER) if f.endswith(".pkl")]

    if not encoded_files:
        print(f"❌ Không tìm thấy dữ liệu khuôn mặt trong '{ENCODED_FOLDER}'!")
        return

    print(f"📂 Đang tải dữ liệu từ thư mục '{ENCODED_FOLDER}'...")
    for file in encoded_files:
        with open(os.path.join(ENCODED_FOLDER, file), "rb") as f:
            data = pickle.load(f)
            known_face_encodings.append(data["encoding"])
            known_face_names.append(data["name"])

    print(f"✔ Đã tải {len(known_face_encodings)} khuôn mặt.")

    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("❌ Không thể mở camera!")
        return

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("❌ Không thể đọc dữ liệu từ camera!")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video_capture.release()
    cv2.destroyAllWindows()

# === CHẠY CHƯƠNG TRÌNH ===
if __name__ == "__main__":
    print("\n🚀 Bước 1: Trích xuất đặc điểm khuôn mặt...")
    extract_face_encodings()

    print("\n🎥 Bước 2: Nhận diện khuôn mặt từ camera...")
    recognize_faces()
