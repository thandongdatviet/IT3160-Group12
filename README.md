# MAP AI PATHFINDING BETWEEN TWO POINTS

## Mô tả Project
Đây là kết quả bài tập lớn môn Nhập môn Trí tuệ Nhân tạo IT3160, kì 20222, sáng thứ 2.
Cho 2 điểm trên bản đồ, tìm đường đi từ một điểm đến điểm còn lại.
Cung cấp người dùng cái nhìn trực quan về tìm kiếm đường đi trong thực tế.
Sử dụng thuật toán tìm kiếm A* với hàm heuristic Euclid.
Tham khảo: 
- https://vi.wikipedia.org/wiki/Gi%E1%BA%A3i_thu%E1%BA%ADt_t%C3%ACm_ki%E1%BA%BFm_A*
- https://www.geeksforgeeks.org/a-search-algorithm/
> Nếu hàm heuristic **__h__** có tính chất thu nạp được (admissible), nghĩa là nó không bao giờ đánh giá cao hơn chi phí nhỏ nhất thực sư của việc đi tới đích, thì bản thân A* có tính **tối ưu**

## Cách sử dụng
- Để chọn điểm xuất phát, nhấn chuột trái vào bàn đồ
- Để chọn điểm cần đến (đích), nhấn chuột phải vào bản đồ
- Nhấp chuột vào Find Path để tìm đường đi
- Để bật/tắt hiển thị tất cả các đường có thể đi, bấm phím T
- Để bật/tắt hiển thị không gian tìm kiếm của bài toán (tập mở, tập đóng), bấm phím R
- Để thoát khỏi chương trình, bấm phím Q

## Yêu cầu cấu hình
- Cài đặt Python, tham khảo: https://www.python.org/downloads/
- Cài thư viện numpy
- Cài thư viện pygame, hướng dẫn cài đặt xem ở bên dưới

## Cài đặt chương trình
- Clone repository vào thư mục local trên máy
- Kiểm tra trên máy đã có các module cần thiết
- Vào thư mục gốc của chương trình, gõ lệnh trên terminal ` python src/main.py `

## Hướng dẫn cài các thư viện vào Python trên Windows
PIP là hệ thống quản lý gói thư viện đối với các module viết bằng Python.
- Đầu tiên cần cài đặt PIP: https://phoenixnap.com/kb/install-pip-windows
- Sau khi cài đặt PIP thành công, thực hiện lênh trên command prompt
` pip install numpy `
- Tham khảo cách cài đặt numpy: https://techcult.com/how-to-install-numpy/
- Tiếp tục cài thêm thư viện pygame
` pip install pygame `

## Các lỗi có thể xảy ra

## Modified History
