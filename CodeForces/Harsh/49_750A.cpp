using namespace std;
int main()
{
    int m, n;
    cin >> m >> n;
    int i=1;
    
    for (i=1; i<=m ;i++) {
         if (i*5 + n > 240) break;
         else {
             n += i*5;
         }
    }
    
    cout << i-1;
}