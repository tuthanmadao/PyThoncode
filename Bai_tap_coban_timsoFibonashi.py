"""
    Viết chương trình tính số Fibonashi thứ n.
"""
n = int(input("n = "))
fibonashi = 1
fn = 1
fn1 = 1
if n <= 2:
    fibonashi = 1
else:
    for i in range(3, n+1, 1):
        fibonashi = fn + fn
        fn, fn1 = fn1, fibonashi

print(fibonashi)