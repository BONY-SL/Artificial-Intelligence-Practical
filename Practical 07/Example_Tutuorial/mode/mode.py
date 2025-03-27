from scipy import stats

speed = [99, 86, 87, 88, 111, 108, 87, 94, 7, 8, 77, 85, 86]

x = stats.mode(speed)

print(x)

