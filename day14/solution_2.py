# it took ~1 min to get answer

INPUT: str = "440231"


def get_last(recipes, offset=0) -> str:
    return "".join([str(digit) for digit in recipes[-len(INPUT) - offset:-offset]])


def main():
    recipes = [3, 7]
    first = 0
    second = 1
    while get_last(recipes) != INPUT and get_last(recipes, offset=1) != INPUT:
        total = recipes[first] + recipes[second]
        if total > 9:
            recipes.extend([1, total % 10])
        else:
            recipes.append(total)
        first = (first + recipes[first] + 1) % len(recipes)
        second = (second + recipes[second] + 1) % len(recipes)
    print("".join([str(digit) for digit in recipes]).index(INPUT))


if __name__ == "__main__":
    main()
