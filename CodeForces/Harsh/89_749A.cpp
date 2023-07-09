#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
 
int main() {
    
   
   int size;
   cin >> size;
   if (size % 2 == 0) {
       cout << (size/2) << endl;
       for (int i=0 ;i < size/2; i++) cout << 2 << " ";
       cout << endl;
   }
   else {
       cout << (size/2) << endl;
       for (int i=0 ;i < size/2 - 1; i++) cout << 2 << " ";
       cout << 3 << endl;
   }
 
    
    return 0;
}