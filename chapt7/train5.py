fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
result = fox.replace(" .",".")
print(result)
result_2 = result[0:-2]
print(result_2)