
def la_doi_xung(n):
    ban_dau = n
    dao = 0
    while n > 0:
        so_cuoi = n % 10       
        dao = dao * 10 + so_cuoi
        n = n // 10             
    return dao == ban_dau
    

def tong_doi_xung(A, B):
    tong = 0
    for x in range(A, B + 1):
        if la_doi_xung(x):
            tong += x
    return tong


def liet_ke_doi_xung(A, B):
    ds = []
    for x in range(A, B + 1):
        if la_doi_xung(x):
            ds.append(x)
    return ds


def dem_doi_xung(A, B):
    dem = 0
    for x in range(A, B + 1):
        if la_doi_xung(x):
            dem += 1
    return dem


def doi_xung_lon_nhat(A, B):
    lon_nhat = -1
    for x in range(A, B + 1):
        if la_doi_xung(x) and x > lon_nhat:
            lon_nhat = x
    return lon_nhat


def doi_xung_nho_nhat(A, B):
    nho_nhat = None
    for x in range(A, B + 1):
        if la_doi_xung(x):
            if nho_nhat is None or x < nho_nhat:
                nho_nhat = x
    return nho_nhat

while True:
    print("\n===== MENU =====")
    print("1. Kiểm tra số đối xứng")
    print("2. Tính tổng số đối xứng từ A đến B")
    print("3. Liệt kê số đối xứng từ A đến B")
    print("4. Đếm số đối xứng từ A đến B")
    print("5. Tìm số đối xứng lớn nhất trong đoạn")
    print("6. Tìm số đối xứng nhỏ nhất trong đoạn")
    print("0. Thoát")
    
    chon = int(input("Chọn chức năng: "))

    if chon == 1:
        n = int(input("Nhập số cần kiểm tra: "))
        if la_doi_xung(n):
            print(n, "là số đối xứng.")
        else:
            print(n, "không phải số đối xứng.")

    elif chon == 2:
        A = int(input("Nhập A: "))
        B = int(input("Nhập B: "))
        print("Tổng số đối xứng:", tong_doi_xung(A, B))

    elif chon == 3:
        A = int(input("Nhập A: "))
        B = int(input("Nhập B: "))
        print("Danh sách số đối xứng:", liet_ke_doi_xung(A, B))

    elif chon == 4:
        A = int(input("Nhập A: "))
        B = int(input("Nhập B: "))
        print("Có", dem_doi_xung(A, B), "số đối xứng.")

    elif chon == 5:
        A = int(input("Nhập A: "))
        B = int(input("Nhập B: "))
        print("Số đối xứng lớn nhất:", doi_xung_lon_nhat(A, B))

    elif chon == 6:
        A = int(input("Nhập A: "))
        B = int(input("Nhập B: "))
        print("Số đối xứng nhỏ nhất:", doi_xung_nho_nhat(A, B))

    elif chon == 0:
        print("Chương trình kết thúc.")
        break

    else:
        print("Chức năng không hợp lệ, vui lòng chọn lại!")

