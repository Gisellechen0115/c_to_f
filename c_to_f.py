c = input('請輸入攝氏溫度:')
c = float(c)
f = c * 9/5 + 32
print('華氏溫度:', f)


celsius = int(input())

def conv(celsius):
    f =9/5*celsius +32
    return f    
fahrenheit = conv(celsius)
print(fahrenheit)
