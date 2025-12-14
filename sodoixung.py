n = int(input("Moi nhap mot so bat ki: "))
__list__ = []

def doi_xung (n):
    gia_tri = n
    rev = 0
    while gia_tri > 0:
        rev = rev * 10 + gia_tri % 10
        gia_tri//=10
    return rev == n

while True:
    menu = input(f"""
                        MENU
1. Kiem tra so nao la so doi xung voi {n}
2. Kiem tra so co doi xung khong
3. In tong cac so doi xung trong doan gia tri tu A den B
4. Out
    Chon: """)

    if menu == "1":
        while True:
            rever = 0
            x = int(input("Moi nhap so can kiem tra: "))
            while x > 0:
                rever = rever * 10 + x%10
                x//=10
            print(f"So bi dao nguoc lai thanh {rever}")
            if rever == n:
                print(f"So {rever} la so doi xung voi gia tri nhap vo")
            else:
                print(f"So {rever} khong phai so doi xung voi so {n}")

            lua_chon = input("""
            Ban muon tiep tuc kiem tra khong ?
            1. Co
            2. Khong
            """)
            if lua_chon == "1":
                continue
            if lua_chon == "2":
                break

    if menu == "2":
        y = int(input("Vui long nhap mot so bat ky: "))
        rev = 0
        k = y
        while k > 0:
            rev = rev * 10 + k%10
            k//=10
        if rev == y:
            print(f"{y} la so doi xung")
        else:
            print(f"{y} khong phai la so doi xung")

    if menu == "3":
        a = int(input("Vui long nhap gia tri a: "))
        b = int(input("Vui long nhap gia tri b: "))
        __sum__ = 0
        for i in range(a, b+1):
            if doi_xung(i):
                __sum__+=i
                __list__.append(i)
        print(f"Danh sach cac so doi xung: {__list__}")
        print(f"Tong cua cac so doi xung bang: {__sum__}")
        back= input("""
            Moi chon:
            1. Quit 
            2. Back
            chon: """)
        if back == "1":
            break 
        while True:
            if back == "2":
                break

    if menu == "4":
        break
    if menu not in ("1","2","3","4"):
        print(f"{menu} khong nam trong danh sach")

