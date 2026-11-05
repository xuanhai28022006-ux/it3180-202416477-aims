# Lab 01 – Câu hỏi thảo luận

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì với `--local`?

Trên Windows, cấu hình Git toàn cục thường nằm trong `~/.gitconfig` (tương ứng `%USERPROFILE%/.gitconfig`). Nó áp dụng cho mọi repository của người dùng. Cấu hình `--local` được lưu trong `.git/config` của repository hiện tại và chỉ áp dụng ở đó. Khi một khóa có cả hai giá trị, cấu hình local của repository được ưu tiên.

## 2. Vì sao dùng `git mv` khi chuyển module vào package `aims`?

`git mv` vừa chuyển/đổi tên tệp vừa cập nhật staging area, giúp thể hiện thao tác refactor rõ ràng trong commit. Git vẫn lưu lịch sử bằng commit; khi xem log, Git nhận diện tệp được đổi tên dựa trên nội dung tương đồng.

## 3. `release/lab01` có phải baseline không? Vì sao không commit thẳng lên `master`, kể cả khi làm một mình?

`release/lab01` là baseline nộp bài: một trạng thái đã chốt để tham chiếu và tái tạo. Không commit trực tiếp lên `master` giúp mọi thay đổi có PR, lịch sử review và kiểm soát quy trình nhất quán; làm một mình vẫn có thể tự review PR.
