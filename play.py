map = """
■■■■■■■■■■■■■■■■■■
□□□□□□□□□□□□□□□□□□
□□□□□□□□□□□□□□□□□□
□□□□□□□□□□□□□□□□□□
□□□□□□□□□□□□□□□□□□
□□□□□□□□□□□□□□□□□□
□□□□□□□□□□□□□□□□□□
□□□□□□□□□□□□□□□□□□
■■■■■■■■■■■■■■■■■■
"""
# (9, 18) also 19th index is new line
# The escape code to move the cursor to (1, 1) and flush immediately
CURSOR_HOME = "\x1B[1;1H"

# maybe there is a library that can listen to the keyboard for keypresses (hint: it definitely exists)
while True:
    # 1. Move the cursor to the top-left corner
    # The 'end=""' and 'flush=True' are essential here.
    print(CURSOR_HOME, end="", flush=True)

    # 2. Print the entire map, which overwrites the previous frame
    print(map, end="", flush=True)