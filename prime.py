import time

inputnum = []
numlis = []
mem = []
prime = []
chk = 0

#input(0と1は除外)
inputnum = int(input())
numlis = list(range(2, inputnum + 1)) 

#計測開始
start = time.perf_counter() 

#main
while numlis:

    #numlis内の最小値をchkとprimeに追加
    chk = numlis[0]
    prime.append(chk)

    #chkの倍数をmemに追加
    for elem in numlis:
        if elem % chk == 0:
            mem.append(elem)
    
    #numlisからmemの要素を削除
    for x in mem:
        numlis.remove(x)
    
    #memをクリア
    mem.clear()

#計測終了
end = time.perf_counter() 

print(prime)

#msで出力
elapsed_ms = (end - start) * 1000
print(f"処理時間: {elapsed_ms:.3f} ms")