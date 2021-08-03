import random

from statistics import median


def calculate_locations(houses: list[int]) -> float:
    if len(houses) % 2 == 1:
        return quickselect(houses, len(houses) // 2)
    else:
        return 0.5 * (quickselect(houses, len(houses) / 2 - 1) +
                      quickselect(houses, len(houses) / 2))


def quickselect(houses: list[int], k: int) -> int:
    if len(houses) == 1:
        return houses[0]

    pivot: int = random.choice(houses)
    
    lower_distances: list[int] = []
    equal_distances: list[int] = []
    greater_distances: list[int] = []

    for house in houses:
        if house < pivot:
            lower_distances.append(house)
        elif house == pivot:
            equal_distances.append(house)
        elif house > pivot:
            greater_distances.append(house)

    if len(lower_distances) > k:
        return quickselect(lower_distances, k)
    elif len(lower_distances) + len(equal_distances) > k:
        return equal_distances[0]
    else:
        return quickselect(greater_distances, k - len(lower_distances) - len(equal_distances))


def test():
    houses = [random.randrange(1000) for _ in range(100)]
    assert calculate_locations(houses) == median(houses)


if __name__ == "__main__":
    test()
