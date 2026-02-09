def hitung_nilai(tugas, uts, uas):
    nilai = (tugas*0.3) + (uts*0.3) + (uas*0.4)
    print("nilai:", nilai)
    if nilai >= 85:
        print("Grade: A")
    elif nilai >= 70:
        print("Grade: B")
    elif nilai >= 55:
        print("Grade: C")
    elif nilai >= 40:
        print("Grade: D")
    elif nilai < 40:
        print("Grade: E")
hitung_nilai(80, 75, 90)