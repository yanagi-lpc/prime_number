#include <iostream>
#include <vector>
using namespace std;

int main(){
    int inputnum;
    cin >> inputnum;

    auto start = chrono::steady_clock::now();

    vector<int> sieve(inputnum + 1, 1);
    sieve[0] = sieve[1] = 0;
    int count = 0;
    
    for (int i = 3; i <= sqrt(inputnum); i += 2){
        if (sieve[i] == 1){
            for (int j = i * i; j <= inputnum; j += 2 * i){
                sieve[j] =0;
            }
        }
    }

    auto end = chrono::steady_clock::now();
    auto time = end - start;

    cout << 2 << " ";
    count++;

    for (int i = 3; i <= inputnum; i += 2){
        if (sieve[i] == 1){
            cout << i << " ";
            count++;
        }
    } 
    cout << endl;


    auto msec = chrono::duration_cast<chrono::milliseconds>(time).count();
    cout << "処理時間: " << msec << "ms" << endl;

    cout << "素数の個数: " << count << endl;

}