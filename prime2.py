import time

inputnum = int(input())
sieve = [1] * (inputnum + 1)
sieve[0] = sieve[1] = 0
count = 0

#計測開始
start = time.perf_counter() 

#2から2毎に(inputnum)まで
for i in range(3, int(inputnum**0.5) + 1, 2):
    #チェック前かどうか
    if sieve[i] == 1:
        #iの2乗から2*i毎に最終まで
        for j in range(i * i, inputnum + 1, 2 * i):
            sieve[j] = 0

#計測終了
end = time.perf_counter() 

print("2")
count += 1

#偶数を除いたsieveが1の場所を出力(数字が同じだから)
for i in range(3, inputnum + 1, 2):
    if sieve[i] == 1:
        print(i)
        count += 1

# 個数出力
print(f"素数の個数: {count}")

#msで出力
elapsed_ms = (end - start) * 1000
print(f"処理時間: {elapsed_ms:.3f} ms")
