INPUT: int = 440231


def main():
    recipes = [3, 7]
    first = 0
    second = 1
    while len(recipes) < INPUT + 10:
        total = recipes[first] + recipes[second]
        if total > 9:
            recipes.extend([1, total % 10])
        else:
            recipes.append(total)
        first = (first + recipes[first] + 1) % len(recipes)
        second = (second + recipes[second] + 1) % len(recipes)
    print("".join([str(digit) for digit in recipes[INPUT:INPUT+10]]))


if __name__ == "__main__":
    main()
