#include <iostream>
using namespace std;
 
 
int main() {
    int testCases;
    cin >> testCases;
    
    for(int i=0; i< testCases ; i++) {
        int score;
        cin >> score;
        
        if (score <= 1399) cout << "Division 4" << endl;
        else if (score > 1399 && score <= 1599) cout << "Division 3" << endl;
        else if (score > 1599 && score <= 1899) cout << "Division 2" << endl;
        else cout << "Division 1" << endl;
        
    }
    return 0;
}