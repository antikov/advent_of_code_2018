def main():
    transforms = {}
    with open("input.txt", "r") as fin:
        lines = fin.readlines()
        initial_state = lines[0].split(":")[1].strip()
        for line in lines[2:]:
            state, result = list(map(str.strip, line.split("=>")))
            transforms[state] = result
    
    offset = 0
    for _ in range(20):
    
        while not initial_state.startswith("....."):
            initial_state = "." + initial_state
            offset += 1
        while not initial_state.endswith('.....'):
            initial_state = initial_state + "."

        current_state = ""
        current_state += transforms['..' + initial_state[:3]]
        current_state += transforms['.' + initial_state[:4]]

        for index in range(2, len(initial_state) - 2):
            state = initial_state[index-2:index+3]
            current_state += transforms[state]
        current_state += transforms[initial_state[-4:] + '.']
        current_state += transforms[initial_state[-3:] + '..']
        initial_state = current_state
    
    _sum = 0
    _count = 0
    for index, value in enumerate(initial_state):
        if value == "#":
            _sum += index
            _count += 1
    print(_sum - _count * offset)
    

if __name__ == "__main__":
    main()