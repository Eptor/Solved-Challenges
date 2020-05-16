from random import randint

iteration = randint(11,101)

print(f"number of iterations = {iteration}")

for i in range(iteration):
    if i % 3 == 0:
        print(f'{i} = Fizz')

    elif i % 5 == 0:
        print(f'{i} = Buzz')

    elif i % 3 == 0 and i % 5 == 0:
        print(f'{i} == FizzBuzz')

    else:
        print(f'{i} neither Fizz nor Buzz')
