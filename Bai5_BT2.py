# Bài tập 2: Tự động hóa Định giá Trái phiếu Doanh nghiệp

print("=== chương trình tự động định giá trái phiếu doanh nghiệp ===".upper())

# Nhập dữ liệu nguồn 
F = 1000000
c = 0.09
C = F * c
tong_pv_coupon = 0.0
N = 10
y = 0.085

# Dùng vong lập for để tiếp tục tính


for t in range(1,N + 1):
    pv_c = C / ((1 + y) ** t )       # Tính giá trị hiện tại của từng khoản tiền lãi    
    tong_pv_coupon += pv_c            
    pv_f = F / ((1 + y)** N)         # Tính PV mệnh giá gốc
    gia_trai_phieu = tong_pv_coupon + pv_f                  # Tính giá trái phiếu
    
# Dùng cấu trúc rẽ nhánh để phân loại từng gia cổ phiếu

if gia_trai_phieu > F:
    P0 = "Giá trái phiếu được bán cao hơn mệnh giá - Premium"
elif gia_trai_phieu == F:
    P0 = "Giá trái phiếu được bán đúng mệnh giá - Par"
else:
    P0 = "Giá trái phiếu được bán thấp hơn mẹnh giá - Discount"

# Trảv kết quả

print("=== Kết quả dự kiến ===".upper())
print(f"Tiền lãi mỗi năm: {C:,.0f} VND")
print(f"Tổng PV tiền lãi mỗi năm: {pv_c:,.2f} VND")
print(f"PV tiền gốc: {pv_f:,.2f} VND")
print(f"Giá trái PHiếu P0: {tong_pv_coupon:,.2f} VND")
print(f"Kết Luận: {P0}")

