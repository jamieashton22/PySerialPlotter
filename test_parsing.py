# test_string = 'Distance: 123.09 cm'
# test_string = '123.09 cm'   

# test_string_strip = test_string.rstrip()

# # print(test_string)
# # print(test_string_strip)

# test_string_split = test_string.split()
# print(test_string_split)
# print(test_string_split[1])
# value = float(test_string_split[1])
# print(value + 4)


# import re
# s = "Sound Level: -11.7 db or 15.2 or 8 db"
# result = re.findall(r"[-+]?\d*\.\d+|\d+", s)
# print (result)

import re
test_string = 'The Distance IS 123.09 cm'
data = re.findall(r"\d*\.\d+|\d+", test_string)
print(data[0])