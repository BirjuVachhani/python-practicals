pattern = 'X-DSPAM-Confidence'
file_name = input('Enter the file name to read from(with extension):')
confidences = list()
with open(file_name) as f:
    for line in f:
        line_parts = line.strip().split(':')
        if line_parts[0] == pattern:
            confidences.append(float(line_parts[1]))

print('Average spam confidence: {}'.format(sum(confidences)/len(confidences)))
