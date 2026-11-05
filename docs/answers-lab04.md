# Lab 04 – Câu hỏi thảo luận

## 1. Vì sao không merge release/* ngược vào master? So sánh với GitFlow.

Trong Release Flow của bài thực hành, nhánh release là baseline của phiên bản đã phát hành. Sau khi tạo release, master tiếp tục nhận tính năng mới nên không merge release ngược vào master. Nếu có hotfix, ta đưa phần sửa cần thiết sang master bằng cherry-pick để tránh kéo các thay đổi chỉ dành cho phiên bản cũ.

Trong GitFlow truyền thống, nhánh release thường được merge lại vào develop và main sau khi phát hành. Quy trình của bài thực hành đơn giản hơn và giữ các nhánh release độc lập để bảo trì nhiều phiên bản.

## 2. Vì sao phát hành 1.0.0 thay vì 0.4.0?

Theo Semantic Versioning, phiên bản 1.0.0 đánh dấu lần phát hành ổn định đầu tiên. Các phiên bản 0.1.0 đến 0.3.0 trong các lab trước là giai đoạn phát triển chưa ổn định. Dùng 0.4.0 sẽ tiếp tục biểu thị trạng thái chưa ổn định, còn 1.0.0 thể hiện baseline đã sẵn sàng phát hành.
