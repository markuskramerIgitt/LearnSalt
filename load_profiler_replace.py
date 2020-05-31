import re

data = """helloy you2
helloy you2
helloy you2
helloy you2
helloy you2
"""
result = re.sub("you2", "you3", data)
print(result)
