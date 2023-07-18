import dns.resolver

answers = dns.resolver.resolve('www.google.com', 'A')

print(answers.response)