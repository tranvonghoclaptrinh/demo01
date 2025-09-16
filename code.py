import math

def tinh_chu_vi(r):
    return 2 * math.pi * r

def tinh_dien_tich(r):
    return math.pi * r ** 2

if __name__ == "__main__":
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    chu_vi = tinh_chu_vi(ban_kinh)
    dien_tich = tinh_dien_tich(ban_kinh)
    print(f"Chu vi hình tròn: {chu_vi:.2f}")
    print(f"Diện tích hình tròn: {dien_tich:.2f}")