# if word ends with "ing": append "ly", else: append "ing"
print(text + "ly" if (text := input("Enter a string: ")).endswith("ing") and len(text) > 2 else text + "ing" if len(text) > 2 else text)