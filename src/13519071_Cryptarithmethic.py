# PROGRAM CRYPTARITHMETHICSOLVER
# DIBUAT OLEH : FARHAN NUR HIDAYAT DENIRA

from time import time

# PERMUTASI
def permutation(lst):
    # basis
    if len(lst) == 0:
        perm = []
    elif len(lst) == 1:
        perm = [lst]
    # rekurens
    else:
        perm = []
        # cari permutasi lst
        for i in range(len(lst)):
            tail = lst[:i] + lst[i + 1:]
            # permutasi dgn first elmt lst[i]
            for per in permutation(tail):
                perm.append([lst[i]] + per)
    return perm


# PERMUTASI DENGAN RANGE
def permrange(lst, r):
    take = len(lst) - r
    # cari faktorial
    fak = 1
    for i in range(1, take + 1):
        fak = fak * i
    # permutasi
    perm = permutation(lst)
    l = []
    for i in range(0, len(perm), fak):
        perm[i] = perm[i][:-take]
        l.append(perm[i])
    return l


# READ FROM FILE
def read():
    global Op
    import os
    c = os.path.dirname(os.path.realpath(__file__))
    par = os.path.split(c)[0]
    while True:
        try:
            filename = input("Masukkan nama soal : ")
            tes = os.path.join(par, 'test', filename)
            file1 = open(tes, 'r')
            Op = file1.readlines()
            break
        except:
            print("File tidak ditemukan, coba lagi...")

    if len(Op) < 4: # asumsi garis pembatas selalu ada
        print("Soal setidaknya memiliki 2 operan,garis pembatas, dan 1 jawaban, silahkan perbaiki.")
        return False

    # hapus \n
    for i in range(len(Op)):
        Op[i] = Op[i].strip()
        if Op[i] == '':
            print("Soal tidak boleh memiliki baris kosong, silahkan perbaiki.")
            return False
    # hapus elemen ----- di array
    Op.pop(len(Op) - 2)
    Op[len(Op) - 2] = Op[len(Op) - 2].replace('+', '')
    return True

# PRINT PERSAMAAN
def print_persamaan(ophuruf, opangka):
    jarak = len(max(ophuruf, key=len))

    # print operan
    for i in range(len(ophuruf) - 1):
        # print spasi
        print(" " * 2 * (jarak - len(ophuruf[i])), end='')
        # print per huruf
        for j in ophuruf[i]:
            print(j, end=' ')
        print('     ', end=' ')

        # print spasi
        print(" " * 2 * (jarak - len(ophuruf[i])), end='')
        # print per angka
        for j in opangka[i]:
            print(j, end=' ')
        print()

    # print garis pembatas
    print("+ " + "- " * (jarak - 1), end='      ')
    print("+ " + "- " * (jarak - 1))

    # print jawaban
    # print spasi
    print(" " * 2 * (jarak - len(ophuruf[-1])), end='')
    # print per huruf
    for j in ophuruf[-1]:
        print(j, end=' ')
    print('     ', end=' ')

    # print spasi
    print(" " * 2 * (jarak - len(ophuruf[-1])), end='')
    # print per angka
    for j in opangka[-1]:
        print(j, end=' ')
    print()


# string jadi arr of int, misal 'ab' jadi [1,2]
def string_to_arrnum(op, huruf_unik, solusi):
    arr = [-1 for i in range(len(op))]
    for i in range(len(huruf_unik)):
        for j in range(len(op)):
            if op[j] == huruf_unik[i]:
                arr[j] = solusi[i]
    return arr


# ubah array nomor jadi angka, misal [1,2] jadi 12
def arrnum_to_num(arr):
    if arr == []:
        return 0
    num = 0
    for i in range(len(arr)):
        pangkat = (len(arr) - (i + 1))
        num += arr[i] * (10 ** pangkat)
    return num


def main():
    awal1 = time()
    if not read():
        return
    print("Mencari solusi, silahkan tunggu...\n")
    # membuat array unik berisi huruf-huruf dari semua operator dan jawaban
    huruf = []
    for string in Op:
        for letter in string:
            if not letter in huruf:
                huruf.append(letter)

    # membuat permutasi angka 0-9 dengan range panjang array huruf

    perm = permrange([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(huruf))

    # Menginisialisasi jumlahtes dan waktu awal
    jumlahtes = 0
    awal2 = time()

    # mengecek satu-persatu list permutasi
    for lst in list(perm):
        valid = True
        jumlahtes += 1
        sum = 0
        numOp = []
        # ubah jadi array int
        for string in Op:
            arrnum = string_to_arrnum(string, huruf, lst)
            numOp.append(arrnum)
            # huruf pertama operator tidak boleh bernilai 0
            if arrnum[0] != 0:
                num = arrnum_to_num(arrnum)
                sum += num
            else:
                valid = False
                break

        if valid:
            # mengecek num dari jawaban
            arrj = string_to_arrnum(Op[-1], huruf, lst)
            numj = arrnum_to_num(arrj)

            # mengecek apakah sesuai soal
            if sum == 2 * numj:
                print_persamaan(Op, numOp)
                print()
                akhir = time()
                print("\nJumlah tes :", jumlahtes)
                print("Waktu :", (akhir - awal2), "detik")
                print()
                print("Waktu Total:", (akhir - awal1), "detik")
                print()

    print("Finished")
    input("Press anything to quit...")

main()
