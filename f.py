file1 = open('input.txt', 'r')
file2 = open('output.txt', 'w')

lines = file1.readlines()

for i, line in enumerate(lines):
    if i % 2 != 0:
        file2.write(line)
        print(line.strip())  # Strip to remove extra newline

file1.close()
file2.close()

file2 = open('output.txt', 'r')
f = file2.read()

print("\nContents of output.txt:")
print(f)

file2.close()
