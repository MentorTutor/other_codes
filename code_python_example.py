var1 = 111
print("var1 === ", var1)
print("id(var1) === ", id(var1))
var1 = var1 + 2
print("var1 === ", var1)
print("id(var1) ===", id(var1))
print("id(111) === ", id(111))
print("-" * 30)
var2 = "hello"
print("var2 === ", var2)
print("id(var2) === ", id(var2))
var2 = var2 + " world :)"
print("var2 === ", var2)
print("id(var2) ===", id(var2))
print("id('hello') === ", id("hello"))
print("-" * 30)
var3 = [1, 2, 3, 4]
print("var3 === ", var3)
print("id(var3) === ", id(var3))
print("id([1, 2, 3, 4]) === ", id([1, 2, 3, 4]))
var3.append(5)
# var3 = var3.append(5) # None
print("var3 === ", var3)
print("id(var3) ===", id(var3))
print("id([1, 2, 3, 4]) === ", id([1, 2, 3, 4]))
