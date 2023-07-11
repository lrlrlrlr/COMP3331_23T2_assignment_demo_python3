
from dns import resolver,reversename
addr=reversename.from_address("2001:4860:4860::8888")
query = resolver.resolve(addr,"PTR")[0]
print(str(query))