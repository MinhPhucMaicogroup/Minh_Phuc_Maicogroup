#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
int main()
{
    int test_case;
    cin >> test_case;
    for(int count=1; count<= test_case; count++)
    {
        long long friends;
        long long small=6, medium=8, large=10;
        long long small_time=15, medium_time=20, large_time=25;
        cin >> friends;
        long long time = 0;
        long long remain = friends%6;
        long long divided = friends/6;
        if(friends <= 6)
        {
            time = 15;
        }
        else if(remain == 0)
        {
            time = divided*15;
        }
        else if(remain <=2)
        {
            time = divided*15 + 5;
        }
        else if(remain <= 4)
        {
            time = divided*15 + 10;
        }
        else
        {
            time = (divided+1) * 15;
        }
        cout << time << endl;
    }
}