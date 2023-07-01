#include<iostream>
#include<string>
#include<set>
using namespace std;
int main() {
    int size;
    
    int num;
    cin >> size;
    int array [size];
    int a;
    
    cin >> a;
    for(int i=0; i<a; i++) {
        cin >> num;
        array[num-1] = 1;
    }
    
    cin >> a;   
    for(int i=0; i<a; i++) {
        cin >> num;
        array[num-1] = 1;
    }
    
    int count = 0;
    for (int i=0; i<size; i++) {
        if (array[i] == 1) count++;
    }
    
    if (count == size) cout << "I become the guy.";
    else cout << "Oh, my keyboard!";
    return 0;
}