def number_to_words(num):
    if num == 0:
        return "Zero"

    def helper(num):
        below_20 = [
            "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
            "Eighteen", "Nineteen"
        ]
        tens = [
            "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        if num < 20:
            return below_20[num]
        if num < 100:
            return tens[num // 10 - 2] + (" " + below_20[num % 10] if num % 10 > 0 else "")
        if num < 1000:
            return below_20[num // 100] + " Hundred" + (" " + helper(num % 100) if num % 100 > 0 else "")
        for i, word in enumerate(["Thousand", "Million", "Billion"], 1):
            if num < 1000 ** (i + 1):
                return helper(num // (1000 ** i)) + " " + word + (" " + helper(num % (1000 ** i)) if num % (1000 ** i) > 0 else "")

    return helper(num)

# Example usage
num = 12345
words = number_to_words(num)
print(f"The number {num} in words is: {words}")
