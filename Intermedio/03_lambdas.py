# Lambdas

# Las lambdas son funciones sin nombre

sum_two_values = lambda first_value, second_value: first_value + second_value  # una lambda la guardo en una variable
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))


# Lambda dentro de función

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))
