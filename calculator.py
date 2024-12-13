def add(a, b):
    a, b = a[::-1], b[::-1]  # Reverse for easier addition
    carry, result = 0, []

    for i in range(max(len(a), len(b))):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0

        total = digit_a + digit_b + carry
        result.append(total % 10)
        carry = total // 10

    if carry:
        result.append(carry)

    return ''.join(map(str, result[::-1]))

def parse_expression(expression):
    tokens = expression.split()
    return tokens  # Example: ["12345", "+", "67890"]

def evaluate_expression(expression):
    tokens = parse_expression(expression)
    operator = tokens[1]
    if operator == '+':
        return add(tokens[0], tokens[2])
    # Add cases for subtraction, multiplication, etc.


def repl():
    print("Arbitrary-Precision Calculator. Type 'exit' to quit.")
    while True:
        user_input = input(">> ")
        if user_input.lower() == 'exit':
            break
        try:
            result = evaluate_expression(user_input)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()