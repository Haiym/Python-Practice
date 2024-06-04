def distance(time):
    # Convert time to meters
    meters = time * 340.29
    # Convert meters to kilometers
    distance = meters / 1000
    return distance
time = 5  # time elapsed in seconds

distance_to_lightning = distance(time)
print(f'The distance to the lightning strike is {distance_to_lightning:.2f} kilometers.')