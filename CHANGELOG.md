# Changelog

## [Unreleased]

## [1.1.0] - 2026-11-06

### Added
- Add search by DVD category.
- Add sorting of DVDs by title and cost.

## [1.0.0] - 2026-11-06



### Added

- Hiển thị các DVD trong giỏ hàng và tổng tiền.

- Tìm DVD theo tiêu đề.

- Tính giảm giá và kiểm tra phần trăm giảm giá.

- Thêm sơ đồ use case.

- Thêm thông báo tiếng Việt khi thêm DVD vào giỏ hàng.

- Thêm regression test cho giới hạn giỏ hàng.



### Changed

- Chuyển các module DVD và Cart vào package `aims`.



### Fixed

- Từ chối DVD thứ 21 khi giỏ đã đủ 20 DVD.

- Tính đúng tổng tiền sau giảm giá.

- Báo lỗi khi phần trăm giảm giá nằm ngoài khoảng 0–100.

