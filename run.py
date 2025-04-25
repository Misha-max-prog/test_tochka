import json


def check_capacity(max_capacity: int, guests: list) -> bool:
    # Реализация алгоритма
    changes = []
    for guest in guests:
        check_in = guest['check-in']
        check_out = guest['check-out']
        changes.append((check_in, 1))
        changes.append((check_out, -1))
    # сортируем по дате, если даты одинаковые сначала выезд потом въезд
    changes.sort(key=lambda x: (x[0], x[1]))
    count_guests = 0
    for date, change in changes:
        count_guests += change
        if count_guests > max_capacity:
            return False
    return True


if __name__ == "__main__":
    # Чтение входных данных
    max_capacity = int(input())
    n = int(input())


    guests = []
    for _ in range(n):
        guest_json = input()
        guest_data = json.loads(guest_json)
        guests.append(guest_data)


    result = check_capacity(max_capacity, guests)
    print(result)
