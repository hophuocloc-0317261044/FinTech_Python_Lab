# Bài tập 1: Mô phỏng Kế hoạch Tích lũy Hưu trí Tự động
# Nhập dữ liệu hệ thống 

tuoi = 25
tien_gui = 60000000
lai_suat = 0.10
so_du = 0.0
muc_tieu = 1000000000
tang_tien_gui = 0.08
nam = 0

print("=== báo cáo mô phổng kế hoạch mưu trí tự động ===".upper())
header = f"{'Năm':<10} | {'Tuổi':<10} | {'Số tiền gửi mới':<20} | {'Tiền lãi trong năm':<20} | {'Tổng tài sản cuối năm':<20}"
print(header)
print("-" * len(header))

# sử dụng vòng lặp while để tính toán số dư hàng năm

while so_du < muc_tieu:
    nam += 1
    tien_lai_trong_nam = so_du * lai_suat
    tien_gui_moi = so_du * tang_tien_gui
    so_du += tien_gui + tien_lai_trong_nam + tien_gui_moi
    tuoi += 1
    print(f"{nam:<10} | {tuoi:<10} | {tien_gui_moi:<20,.2f} | {tien_lai_trong_nam:<20,.2f} | {so_du:<20,.2f}")
print("-" * len(header))
print(f"Kết Luận: khach hàng sẽ đạt được mục tiêu nghỉ hưu sau {nam} năm(lúc {tuoi} tuổi)") 




