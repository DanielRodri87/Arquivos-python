// import math

// a, b, c = map(int, input().split())
// p = (a + b + c) / 2.0
// area = math.sqrt(p * (p - a) * (p - b) * (p - c))
// print(f"{area:.3f} m2")

// Em C++:

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    
    int a, b, c;
    double p, area;

    cin >> a >> b >> c;

    p = (a + b + c) / 2.0;
    area = sqrt(p * (p - a) * (p - b) * (p - c));

    cout << fixed;
    cout.precision(3);
    cout << area << " m2" << endl;

    return 0;
}