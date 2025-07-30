n=int(input("enter number"))
def format_number():
    number = n
    base = 'o'  # 'o' is for octal format
    formatted = format(number, base)
    print(f"Formatted (Octal) value of {n}:", formatted)

format_number()