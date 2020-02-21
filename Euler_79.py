numbers = {}

with open('ProblemFiles/Problem_79.txt') as f:
    for line in f:
        code = []
        for n in line.strip():
            code.append(int(n))
        for i, c in enumerate(code):
            if not c in numbers:
                numbers[c] = set()
            numbers[c].update(code[:i])


numbers = [(k, v) for k, v in numbers.items()]
numbers.sort(key= (lambda x : len(x[1])))
print(int(''.join([str(i[0]) for i in numbers])))