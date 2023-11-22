
# ItemsInCart = 0
#
# if ItemsInCart != 2:
#     raise Exception("product count in cart is not matching")
    # pass

# assert(ItemsInCart == 0)

# Try, Catch
a=2
try :
    with open('test.txt', 'r') as reader:
        reader.read()

except:
    print("There is failure in try block")
print("_________________________________")

try :
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Cleaning up resoures")

print("_________________________________")

try:
    if a==2:
        print("Value of a is correct")
except:
    print("Value of a is wrong")

finally:
    print("Code is executed successfully")