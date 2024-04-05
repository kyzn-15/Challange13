import os

def batas():
    print("-"*35)

def inpt(): 
    while True:
        input_data = int(input("Masukan angka \t:"))
        break
    return input_data

def mean(**data):
    num_list = data["nilai"]
    jumData = sum(num_list)
    bnykData = len(num_list)
    hsil_mean = float(jumData / bnykData)

    list_urut = sorted(num_list)
    n = len(list_urut)
    if n % 2 == 0:
        hasil_median = (list_urut[n//2 - 1] + list_urut[n//2]) / 2
    else:
        hasil_median = list_urut[n//2]
    frekuensi_data = {}
    for j in num_list:
        if j in frekuensi_data:
            frekuensi_data[j] += 1
        else:
            frekuensi_data[j] = 1
    max_freq = max(frekuensi_data.values())
    hasil_modus = [key for key, value in frekuensi_data.items() if value == max_freq]
    return hsil_mean, hasil_median, hasil_modus

num_list = []
while True:
    batas()
    os.system('cls')
    num_list.append(inpt())
    opsi = input("lanjut (y/t):").lower()
    if opsi == "t":
        break
    else:
        continue

batas()
os.system('cls')

hsil_mean, median_result, modus_result = mean(nilai=num_list)
print(f"Mean dari data : {num_list} = {hsil_mean}")
print(f"Median dari data : {num_list} = {median_result}")
print(f"Modus dari data : {num_list} = {modus_result}")
