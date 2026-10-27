# 1 Dữ liệu cơ bản
tien_goc = 20
ty_gia_usd_vnd = [-0.03, 0, 0.03]
ty_gia_lai_suat = [-0.02, -0.01, 0.01, 0.02]

# 2 In tiêu đề
print("=============== ma trận mô phỏng rủi ro =================".upper())
bang= f"{'lãi suất \ tỷ giá' :<5}| {'-3.0%':^10} | {'0%':^10} | {'3.0%':>6}"
print("Vốn danh mục ban đầu: 20 tỷ")
print(bang)
print("-" * len(bang))

# 3 Vòng lặp
for i in ty_gia_lai_suat:
    print(f"Lãi suất {i * 100:+.0f}% |", end=" ")
    for j in ty_gia_usd_vnd:
        tien_sau = tien_goc * (1 + 1.5 * i - 2 * j)
        print(f"{tien_sau:11.2f}" ,end=" ")
    print()