# bài4 Tính Lãi suất Tiết kiệm
# nhập dữ liệu đầu vào bằng inpt và định dạng dữ liệu 
so_tien_goc = float(input("Nhập số tiền gốc: VND"))
lai_suat = float(input("Nhập lãi suất hàng năm (ví dụ: 0.05 cho 5%): "))
thoi_gian = int(input("Nhập số năm gửi: "))

# Tính lãi suất

Tong_tien = so_tien_goc * (1 + lai_suat * thoi_gian)

# In kết quả 

print(f"Tổng số tiền sau {thoi_gian} năm là: {Tong_tien:.2f} VND")

