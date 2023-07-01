#include<iostream>
#include<string>
using namespace std;
 
int main() {
    int len;
    string games;
    
    cin >> len;
    cin >> games;
    
    int winCount = 0;
    
    for(char i: games) {
        if (i == 'D') winCount++;
        else winCount--;
    }
    
    if (winCount == 0) cout << "Friendship";
    else if (winCount > 0) cout << "Danik";
    else cout << "Anton";
      
}