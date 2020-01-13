#1. reads name.txt into a variable my_name and then
with open('name.txt') as f:
    name_text = f.read()
#2. writes a new file named hello.txt with the contents 
# Hello, my name is <my_name>.
print("Hello, my name is ",	name_text)


with open('hello.txt', 'w') as f:

	 f.write('hello, my name is ')
	 f.write(name_text)
	 f.write('\n')

