#include <iostream>
using namespace std;
int main()
{
    int a,b;
    
    cin >> a >> b;
    
    int max = a > b ? a:b;
    int min = a < b ? a:b;
    
    cout << min << " " << (max-min)/2;
    
    
}