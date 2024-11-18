def point_in_circle(a, b, R, x, y):
    return (x - a) ** 2 + (y - b) ** 2 < R ** 2
a = float(input("Введите координату x центра окружности (a): "))
b = float(input("Введите координату y центра окружности (b): "))
R = float(input("Введите радиус окружности (R): "))
p1, p2 = map(float, input("Введите координаты точки P(p1, p2): ").split(','))
f1, f2 = map(float, input("Введите координаты точки F(f1, f2): ").split(','))
l1, l2 = map(float, input("Введите координаты точки L(l1, l2): ").split(','))
points = [(p1, p2), (f1, f2), (l1, l2)]
inside_count = 0
for point in points:
    x, y = point
    if point_in_circle(a, b, R, x, y):
        inside_count += 1
print(f"Количество точек внутри окружности: {inside_count}")