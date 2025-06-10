def sum_of_digit(n):
    # Base Case
    if n < 10:
        return n
    # Recursive Case
    else:
        last_digit = n % 10
        # Collecting the last digit
        remaining_digit = n // 10
        # Collecting the remaining digit(s)
        return last_digit + sum_of_digit(remaining_digit)


# calling the function
print(sum_of_digit(55))
