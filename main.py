# Phoenix Valent
	# U4L2
		# Reverse a string with stacks

from StackClass import ArrayStack


def reverseDaString():
	possible = True
	original = input("Type out a string, I promise nothing bad will happen to it... ")
	new = ""
	reverseStack = ArrayStack()
	for i in original:
		reverseStack.push(i)
	while possible:
		try:
			new+=(reverseStack.pop())
		except:
			possible = False
	
	return new

def main():
	reversedString = reverseDaString()
	print(f"I lied.\n\n{reversedString}")

if __name__ == "__main__":
	main()