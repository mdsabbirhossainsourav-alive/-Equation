import math
a,b,c= map(int, input().split())
if a == 0:
    if b == 0:
        print(-1 if c == 0 else 0)
    else:
        print(1)
        print(f"{-c/b:.10f}")
else:
    d = b*b - 4*a*c
    if d < 0:
        print(0)
    elif d == 0:
        print(1)
        print(f"{-b/(2*a):.10f}")
    else:
        x1 = (-b - math.sqrt(d)) / (2*a)
        x2 = (-b + math.sqrt(d)) / (2*a)
        x1, x2 = sorted([x1, x2])
        print(2)
        print(f"{x1:.10f}")
        print(f"{x2:.10f}")
