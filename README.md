# 📌 Nhận Diện Khuôn Mặt Khi Đeo Khẩu Trang

## 🚀 Giới thiệu
📢 Hệ thống nhận diện khuôn mặt kết hợp kiểm tra đeo khẩu trang là một ứng dụng hữu ích trong nhiều lĩnh vực như giám sát an ninh, kiểm soát ra vào, chấm công tự động và hỗ trợ y tế. Chương trình sử dụng công nghệ Deep Learning và Computer Vision để thực hiện hai nhiệm vụ chính:

- Nhận diện khuôn mặt bằng thư viện face_recognition.

- Phát hiện khẩu trang bằng mô hình YOLO hoặc các phương pháp xử lý hình ảnh khác.
## 🎯 Tính năng
- 🔍 **Phát hiện khuôn mặt** trong hình ảnh hoặc video.
- 🆔 **Nhận dạng và so khớp khuôn mặt** với dữ liệu đã lưu trữ.
- ⚡ **Hỗ trợ chạy trên GPU** để tăng tốc độ xử lý.
- 🔗 **Tích hợp dễ dàng** với các ứng dụng nhận diện khuôn mặt khác.

## 🔧 Cài đặt
### 📌 Yêu cầu hệ thống
- 🐍 **Python** >= 3.8
- 🎮 **CUDA** (nếu chạy trên GPU)
- 📸 **OpenCV**
- 🧠 **InsightFace**

## 🏗 Mô Hình
🖥️ Sử dụng mô hình **RetinaFace** kết hợp với **ResNet-50** để nhận diện khuôn mặt và kiểm tra việc đeo khẩu trang.

## 📥 Cài đặt môi trường
🛠️ Chạy lệnh sau để cài đặt thư viện cần thiết:
```sh
pip install -r requirements.txt
```

## 🚀 Cách sử dụng
### 📸 1. Trích xuất đặc điểm khuôn mặt
🖼️ Chạy lệnh sau để trích xuất đặc điểm khuôn mặt từ dataset:
```sh
python extract_faces.py
```

### 🎥 2. Nhận diện khuôn mặt từ camera
📹 Chạy lệnh sau để nhận diện khuôn mặt từ camera:
```sh
python recognize_faces.py
```
🛑 Nhấn `Q` để thoát chương trình.

## 📂 Cấu trúc thư mục
📁 **Cấu trúc thư mục dự án:**
```
📂 FaceMaskRecognition
 ├── 📁 dataset_khautr        # Thư mục chứa ảnh khuôn mặt
 ├── 📁 encoded_khautr        # Lưu dữ liệu đặc điểm khuôn mặt
 ├── 📜 extract_faces.py      # Mã nguồn trích xuất khuôn mặt
 ├── 📜 recognize_faces.py    # Mã nguồn nhận diện khuôn mặt
 ├── 📜 requirements.txt      # Các thư viện cần thiết
```

## 📌 Ghi chú
- 🏠 **Dữ liệu mẫu**: Có thể thay đổi dataset để phù hợp với yêu cầu.
- 🎭 **Nhận diện với khẩu trang**: Hệ thống hỗ trợ nhận diện ngay cả khi đeo khẩu trang.
- 🚀 **Tăng tốc GPU**: Khuyến nghị sử dụng GPU để cải thiện tốc độ xử lý.


✨ Kết luận
---Hệ thống nhận diện khuôn mặt và kiểm tra đeo khẩu trang đã được triển khai thành công, giúp tăng cường an ninh và hỗ trợ giám sát y tế. Trong tương lai, hệ thống có thể được tối ưu và mở rộng để ứng dụng trong nhiều lĩnh vực khác nhau.
