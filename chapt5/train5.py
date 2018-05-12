def float_conv(x):
    """Converts input num to float"""
     try:
         return float(x)
     except ValueError:
         print("Input NUMBER")

num = input("Input number:")
result = float_conv(num)
print(result)

