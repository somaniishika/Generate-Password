import string
import random
total=string.ascii_letters + string.digits
length=12
password="".join(random.sample(total,length))
print(password)
