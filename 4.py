import math

def solution(a, b, c):
    D = b**2 - 4*a*c

    if D < 0:
        return None
    elif D == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return tuple(sorted((x1, x2)))

# Foydalanuvchidan o'zgaruvchilarni kiritish
user_input = input("Solution formatida kiritish: ")

try:
    # Kiritilgan matnni to'g'ri formatga aylantirish
    user_input = user_input.replace("solution(", "").replace(")", "")
    params = user_input.split(", ")
    
    # Parametrlarni ajratish
    a = float(params[0].split("=")[1])
    b = float(params[1].split("=")[1])
    c = float(params[2].split("=")[1])
    
    # Natijani chiqarish
    result = solution(a, b, c)
    print("Natija:", result)
except Exception as e:
    print("Xato:", e)

