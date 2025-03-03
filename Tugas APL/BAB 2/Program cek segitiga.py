def main():
    print("Program untuk mengecek jenis segitiga berdasarkan panjang sisinya.")
    
    while True:
        try:
            a = float(input("Masukkan panjang sisi a: "))
            b = float(input("Masukkan panjang sisi b: "))
            c = float(input("Masukkan panjang sisi c: "))
            if a > 0 and b > 0 and c > 0:
                break
            else:
                print("Panjang sisi harus lebih besar dari 0. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Masukkan nomor yang benar.")
    
    # Cek apakah tiga sisi dapat membentuk segitiga
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            jenis_segitiga = "Segitiga Sama Sisi"
        elif a == b or a == c or b == c:
            jenis_segitiga = "Segitiga Sama Kaki"
        else:
            jenis_segitiga = "Segitiga Sembarang"
    else:
        jenis_segitiga = "Bukan Segitiga"
    
    print(f"Jenis segitiga: {jenis_segitiga}")
 
main()

