/*
一个孩子在一栋高楼的第N层玩球。这层楼的高度h是已知的。
他把球从窗口扔了出去。球反弹（例如）到其高度的三分之二（反弹0.66）。
他母亲从离地1.5米的窗户向外看。
妈妈会看到球在她窗前经过多少次（包括什么时候落下和弹跳）？
有效实验必须满足三个条件：
以米为单位的浮点参数“h”必须大于0
浮动参数“bounce”必须大于0且小于1
浮动参数“window”必须小于h。
如果满足上述三个条件，则返回正整数，否则返回-1。
注：
只有篮板球的高度比窗口参数严格时，才能看到球。
*/
#include <iostream>
using namespace std;
class Bouncingball
{
public:
    static int bouncingBall(double h, double bounce, double window);
};
int Bouncingball::bouncingBall(double h, double bounce, double window)
{
    int count = 0;
    if (h <= 0 || bounce >= 1 || bounce <= 0 || window >= h)
    {
        return -1;
    }
    if (h >= window)
        count += 1;
    while (true)
    {
        h *= bounce;
        if (h > window)
            count += 2;
        else
            break;
    }
    return count;
}

int main()
{
    Bouncingball ball;
    cout << ball.bouncingBall(30, 0.66, 1.5);
    return 0;
}
