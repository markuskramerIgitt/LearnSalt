import re

data = "The rain in Australia"
result = re.sub("\s", "~~~", data)
print(result)
