#include <iostream>
 
using namespace std;
 
int mini(int a, int b) {
    return a < b ? a : b;
}
 
int main() {
    int t;
    cin >> t;
    int parr[t], marr[t], pearr[t];
    int pcount = 0, mcount = 0, pecount = 0;
    int num;
    for (int i=0; i<t; i++) {
        cin >> num;
        switch (num) {
            case 1: parr[pcount++] = i+1; break;
            case 2: marr[mcount++] = i+1; break;
            case 3: pearr[pecount++] = i+1; break;
        }
    }
    
    int min = mini (pcount, mini(mcount, pecount));
    cout << min << endl;
    for (int i=0; i< min; i++) {
        cout << parr[i] << " " << marr[i] << " " << pearr[i] << endl;
    }
    
   
}