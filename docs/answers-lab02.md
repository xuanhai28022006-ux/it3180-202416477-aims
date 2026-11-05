# Lab 02 – Câu hỏi thảo luận

## 1. Vì sao cần đồng bộ `master` trước khi gửi PR?

Đồng bộ nhánh với `master` giúp phát hiện xung đột sớm, kiểm tra tính năng cùng các thay đổi mới nhất và giảm rủi ro PR chỉ chạy được trên một nhánh cũ.

## 2. Khi nào không nên rebase?

Không nên rebase commit đã push và được người khác dùng làm nền, vì rebase tạo commit SHA mới và viết lại lịch sử mà họ đang dựa vào. Rebase phù hợp với nhánh riêng chưa chia sẻ; với lịch sử chung, ưu tiên merge hoặc dùng PR.

## 3. `feature/*` khác `topic/*` thế nào?

`feature/*` thường chứa một tính năng người dùng có thể nhận thấy, như in nội dung giỏ hàng hoặc tìm DVD. `topic/*` gom một công việc theo chủ đề/phạm vi, như thêm PR template hoặc tài liệu use case. Cả hai đều làm trên nhánh riêng và đưa về `master` qua PR.
