def rectangle_area(a, b):
    return a * b

demention1 = 6
demention2 = 8
print(rectangle_area(6, 8))
print(rectangle_area(demention1, demention2))

def paining_cost(wall_length, wall_height, cost_per_meter2, difficulty_level):
    paining_area = wall_height * wall_length
    total_cost = paining_area * cost_per_meter2
    if difficulty_level > 3:
        total_cost = total_cost + difficulty_level * paining_area * 1.75
    return total_cost

print(paining_cost(6.3, 2.5, 30, 4))