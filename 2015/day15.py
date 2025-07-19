import re

def build_map():
    M = []
    with open("_input/day15.txt") as f:
        for line in f.read().splitlines():
            m = re.match(r"(.+): capacity (.+), durability (.+), flavor (.+), texture (.+), calories (.+)", line)
            M.append((
                int(m[2]),  # capacity
                int(m[3]),  # durability
                int(m[4]),  # flavor
                int(m[5]),  # texture
                int(m[6])   # calories
            ))
    return M

def calc(R, M):
    def sub_calc(v):
        return max(0, sum(r * M[i][v] for i, r in enumerate(R)))
    return (sub_calc(0) * sub_calc(1) * sub_calc(2) * sub_calc(3), sub_calc(4))  # Return both score and calories

def find_combinations(target_sum, num_parts):
    results = []
    def generate_recursive(remaining_sum, remaining_parts, current_combination):
        if remaining_parts == 1:
            if remaining_sum >= 0:
                results.append(current_combination + [remaining_sum])
            return
        for i in range(remaining_sum + 1):
            generate_recursive(remaining_sum - i, remaining_parts - 1, current_combination + [i])
    
    generate_recursive(target_sum, num_parts, [])
    
    return results

def run_part(ingredients, combinations, calorie_check):
    part_1 = 0
    part_2 = 0
    for combination in combinations:
        score, calories = calc(combination, ingredients)
        part_1 = max(part_1, score)
        if calories == calorie_check:
            part_2 = max(part_2, score)
    return part_1, part_2

ingredient_map = build_map()
ingredient_combinations = find_combinations(100, len(ingredient_map))

part_1, part_2 = run_part(ingredient_map, ingredient_combinations, 500)

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")