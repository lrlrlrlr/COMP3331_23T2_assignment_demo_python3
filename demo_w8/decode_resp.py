import dns.message
import dns.rdataclass
import dns.rdatatype

# DNS response message
dns_response = b'\x11X\x81\x80\x00\x01\x00\x01\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01\xc0\x0c\x00\x01\x00\x01\x00\x00\x00o\x00\x04\xac\xd9\xa7D'

# Decode the DNS response
response = dns.message.from_wire(dns_response)

# Decode the questions section
question = response.question[0]
query = str(question.name)
qtype = dns.rdatatype.to_text(question.rdtype)
qclass = dns.rdataclass.to_text(question.rdclass)

# Decode the answer section
answer = response.answer[0]
name = str(answer.name)
atype = dns.rdatatype.to_text(answer.rdtype)
aclass = dns.rdataclass.to_text(answer.rdclass)
ttl = answer.ttl
data = str(answer[0])

# Print the decoded information
print("Query: ", query)
print("Type: ", qtype)
print("Class: ", qclass)
print("Answer: ", data)