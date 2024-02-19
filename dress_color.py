from collections import Counter
import numpy as np

# Data provided
data = [
    "GREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "BLUE", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN",
    "ARSH", "BROWN", "GREEN", "BROWN", "BLUE", "BLUE", "BLEW", "PINK", "PINK", "ORANGE", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "WHITE", "BLUE", "BLUE", "BLUEGREEN", "YELLOW", "GREEN", "BROWN", "BLUE", "PINK", "RED", "YELLOW", "ORANGE", "RED", "ORANGE", "RED", "BLUE", "BLUE", "WHITE", "BLUE", "BLUE", "WHITE", "WHITE",
    "BLUE", "BLUE", "GREEN", "WHITE", "BLUE", "BROWN", "PINK", "YELLOW", "ORANGE", "CREAM", "ORANGE", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "GREEN",
    "GREEN", "WHITE", "GREEN", "BROWN", "BLUE", "BLUE", "BLACK", "WHITE", "ORANGE", "RED", "RED", "RED", "WHITE", "BLUE", "WHITE", "BLUE", "BLUE", "BLUE", "WHITE"
]

# Count the occurrences of each color
color_counts = Counter(data)

# 1. Mean Color
mean_color = np.mean(list(color_counts.values()))

# 2. Most Worn Color
most_worn_color = color_counts.most_common(1)[0][0]

# 3. Median Color
sorted_colors = sorted(color_counts.keys())
median_index = len(sorted_colors) // 2
median_color = sorted_colors[median_index]

# 4. Variance of Colors
variance_colors = np.var(list(color_counts.values()))

# 5. Probability of Choosing Red
probability_red = color_counts.get("RED", 0) / len(data)

# Output results
print("Mean Color:", mean_color)
print("Most Worn Color:", most_worn_color)
print("Median Color:", median_color)
print("Variance of Colors:", variance_colors)
print("Probability of Choosing Red:", probability_red)
