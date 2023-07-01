#include <iostream>
#include <string>
using namespace std;
 
int main() {
    int n;
    cin >> n;
    
    int count = 0;
    string shape;
    for (int i=0; i < n; i++)  {
        cin >> shape;
      
        if (shape.compare("Tetrahedron") == 0) count += 4;
        else if (shape.compare("Cube") == 0) count += 6;
        else if (shape.compare("Octahedron") == 0) count += 8;
        else if (shape.compare("Dodecahedron") == 0) count += 12;
        else if (shape.compare("Icosahedron") == 0) count += 20;
    
    }
    
    cout << count;
    
    
    return 0;
}