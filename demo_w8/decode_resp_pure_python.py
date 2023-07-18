# DNS response message
dns_response = b'\x11X\x81\x80\x00\x01\x00\x01\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01\xc0\x0c\x00\x01\x00\x01\x00\x00\x00o\x00\x04\xac\xd9\xa7D'

# Extract the header fields
header_id = int.from_bytes(dns_response[0:2], byteorder='big')
header_flags = int.from_bytes(dns_response[2:4], byteorder='big')
header_questions = int.from_bytes(dns_response[4:6], byteorder='big')
header_answer_rrs = int.from_bytes(dns_response[6:8], byteorder='big')
header_authority_rrs = int.from_bytes(dns_response[8:10], byteorder='big')
header_additional_rrs = int.from_bytes(dns_response[10:12], byteorder='big')

# Decode flags:
response_code = header_flags & 0b00001111
is_authoritative = bool(header_flags & 0b00010000)
is_truncated = bool(header_flags & 0b00100000)
is_recursion_desired = bool(header_flags & 0b10000000)
is_recursion_available = bool(header_flags & 0b01000000)

# Decode the questions section
question_offset = 12
question_name = ''
while True:
    label_length = dns_response[question_offset]
    if label_length == 0:
        break
    question_name += dns_response[question_offset+1:question_offset+1+label_length].decode('utf-8') + '.'
    question_offset += label_length + 1
question_name = question_name[:-1]  # Remove the trailing '.'

question_type = dns_response[question_offset+1:question_offset+3]
question_class = dns_response[question_offset+3:question_offset+5]

# Decode the answer section
answer_offset = question_offset + 5
answer_name = question_name
answer_type = dns_response[answer_offset+1:answer_offset+3]
answer_class = dns_response[answer_offset+3:answer_offset+5]
answer_ttl = int.from_bytes(dns_response[answer_offset+5:answer_offset+9], byteorder='big')
answer_data_length = int.from_bytes(dns_response[answer_offset+9:answer_offset+11], byteorder='big')
answer_data = '.'.join(str(byte) for byte in dns_response[answer_offset+12:answer_offset+11+answer_data_length])

# Print the decoded information
print("Query: ", question_name)
print("Type: ", question_type)
print("Class: ", question_class)
print("Answer: ", answer_data)
