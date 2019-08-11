#include <vector>
#include <iostream>
using namespace std;
unsigned int countBits(unsigned long long n);
int main()
{
    cout << countBits(0) << endl;
    return 0;
}
unsigned int countBits(unsigned long long n)
{
    if (n == 0)
        return 0;
    unsigned int count = 0;
    cout << "start n:" << n << endl;
    vector<unsigned int> T;
    do
    {
        T.push_back(n % 2);
        n /= 2;
    } while (n / 2 != 0);
    T.push_back(1);
    for (auto p = T.begin(); p != T.end(); ++p)
    {
        if (*p == 1)
        {
            count++;
        }
    }
    return count;
}