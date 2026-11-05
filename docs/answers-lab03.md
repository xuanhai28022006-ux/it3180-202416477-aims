# Lab 03 – Câu hỏi thảo luận

## 1. Merge base là gì?

Merge base là commit tổ tiên chung gần nhất của hai nhánh. Git dùng nó làm điểm xuất phát để so sánh các thay đổi trên hai nhánh khi thực hiện merge và xác định xung đột.

## 2. Vì sao trên `master` và `release/*` nên dùng `revert` thay vì `reset`?

Đây là các nhánh đã chia sẻ và có thể được nhiều người dùng làm nền. `reset` di chuyển con trỏ nhánh và có thể viết lại lịch sử chung; `revert` tạo commit mới đảo ngược thay đổi, giữ nguyên lịch sử để mọi người đồng bộ an toàn. Thực hiện revert qua nhánh riêng và PR.
