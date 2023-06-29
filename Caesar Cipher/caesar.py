# NOTE: It will convert all characters to lowercase!
def encrypt(s: str, num: int) -> str:
    return "".join([chr(ord(i) + (num if ord(i)+num <= 122 else num-26)) if i.isalpha() else i for i in s.lower()])

def decrypt(s: str, num: int) -> str:
    return "".join([chr(ord(i) - (num if ord(i)-num >= 97 else num-26)) if i.isalpha() else i for i in s.lower()])

if __name__ == "__main__":
    try:
        cmd = input(
"""Format: <encrypt/decrypt> <num> <cipher text>
Example: encrypt 5 Hello World!
Enter command: """
)
        type_ = cmd.split(" ")[0]
        num = int(cmd.split(" ")[1])
        text = " ".join(cmd.split(" ")[2:])
        if type_ == "encrypt":
            print(encrypt(text, num))
        elif type_ == "decrypt":
            print(decrypt(text, num))
        else:
            raise ValueError("First argument should be either `encrypt` or `decrypt`")
    except Exception as err:
        print(
f"""An Error Occured
Make sure that you have followed the format given.
Error: {err}
"""
)
    