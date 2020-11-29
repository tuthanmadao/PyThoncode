"""
    Viết chương trình tính n!! với n!! = 1.3.5...n nếu n lẻ, n!! = 2.4.6...n nếu n chẵn.
"""
giatri_n = 1
n = int(input("n = "))
if n % 2 == 0:
    print(f"{n} là số chẵn")
    for i in range(2, n + 1, 2):
        giatri_n *= i
else:
    print(f"{n} là số lẻ")
    for i in range(3, n + 1, 2):
        giatri_n *= i
print(f"n!! = {giatri_n}")
