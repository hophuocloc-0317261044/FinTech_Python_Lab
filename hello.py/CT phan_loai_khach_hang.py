# bai1 Phân loại Hạn mức rủi ro tín dụng

# Nhập điểm tín dụng từ người dùng

diem = int(input("Nhập điểm tín dụng của bạn: "))

# Phân loại dữ liệu theo cấu trúc if-elif-else

if diem < 0 or diem > 850:
    print("Điểm tín dụng không hợp lệ!")
elif diem >= 750:
    level = "Rủi ro thấp"
    action = "Duyệt tự động"
elif diem >= 600:
    level = "Rủi ro trung bình"
    action = "Cần thẩm  định"
else:
    level = "Rủi ro cao"
    action = "Từ chối cấp tín dụng"

# In kết quả

print("=" * 25)
print(f"Điểm đánh giá: {diem}")
print(f"Mức độ rủi ro: {level}")
print(f"Quyết định: {action}")
print("=" * 25)
