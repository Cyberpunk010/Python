import textwrap

def wrap(string, max_width):
    
    # Use textwrap.wrap() to wrap the string
    wrapped_text = textwrap.wrap(string,width=max_width)
    
    # Join the wrapped lines with newline characters
    return '\n'.join(wrapped_text)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)