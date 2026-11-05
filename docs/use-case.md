\# Use Case Diagram — AIMS-mini



Sơ đồ các thao tác chính của khách hàng trong AIMS-mini.



```mermaid

flowchart LR

&#x20;   Customer((Khách hàng))



&#x20;   subgraph AIMS\["AIMS-mini"]

&#x20;       Search(\[Tìm DVD theo tiêu đề])

&#x20;       Add(\[Thêm DVD vào giỏ])

&#x20;       Remove(\[Xóa DVD khỏi giỏ])

&#x20;       View(\[Xem nội dung giỏ])

&#x20;       Total(\[Tính tổng tiền])

&#x20;   end



&#x20;   Customer --- Search

&#x20;   Customer --- Add

&#x20;   Customer --- Remove

&#x20;   Customer --- View

&#x20;   View -.->|bao gồm| Total

```

