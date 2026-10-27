# Bai3 Trích xuất Dữ liệu Giao dịch Tài chính

# Dùng split để cắt chuỗi

ma_giao_dich = input("Nhập mã giao dịch (ví dụ: GD-1000000-VND): ")
part = ma_giao_dich.split("-")
ma_GD = part[0]
tien = int(part[1])
don_vi = part[2]

# dung if-else

if tien >= 5000000:
    print("Giao dịch cần xác thực OTP!")
else:
    print("Giao dịch thành công")

