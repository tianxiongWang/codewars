#include <iostream>
#include <vector>
using namespace std;
class Kata
{
public:
    std::vector<int> sortArray(std::vector<int> array)
    {
        if (array.empty())
            return array;
        for (auto i = array.begin(); i != array.end() - 1; ++i)
        {
            for (auto j = i + 1; j != array.end(); ++j)
            {
                if (*i % 2 == 0)
                    break;
                if (*j % 2 == 0)
                    continue;
                else
                {
                    if (*i > *j)
                    {
                        int temp = *j;
                        *j = *i;
                        *i = temp;
                    }
                }
            }
        }
        return array;
    }
};
int main()
{
    Kata kata;
    vector<int> T;
    T = kata.sortArray({5, 3, 2, 8, 1, 4});
    for (auto i = T.begin(); i != T.end(); ++i)
        cout << *i;
    return 0;
}