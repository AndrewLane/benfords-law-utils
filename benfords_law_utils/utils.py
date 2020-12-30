def calculate_benford_stats(numerical_data):
    first_digit_index = 0
    first_digits = list(map(
        lambda number: int(str(number)[first_digit_index]), numerical_data))

    total_count = 0
    empirical_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ratios = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, 10):
        count_for_this_digit = first_digits.count(i)
        empirical_counts[i - 1] = count_for_this_digit
        total_count += count_for_this_digit

    if total_count > 0:
        for i in range(1, 10):
            ratios[i - 1] = empirical_counts[i - 1] / total_count

    return empirical_counts, ratios, total_count
