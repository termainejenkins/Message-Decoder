#message decoding app in python.

def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
 
    word_map = {int(line.split()[0]): line.split()[1] for line in lines}
    message = []
    line_end = 1
 
    while line_end in word_map:
        message.append(word_map[line_end])
        line_end = line_end * (line_end + 1) // 2
 
    return ' '.join(message)

print (decode('code.txt'))
# The decode function reads the contents of a file specified by the message_file parameter. 
# It extracts the last word from each line, which corresponds to the words associated with pyramid numbers. 
# Finally, it joins these words into a string to form the decoded message. 
# The example usage demonstrates how to apply the function to a specific file ('your_message_file.txt') and print the resulting decoded message.