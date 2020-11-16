import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        allowed_colors = set(['red', 'orange', 'black', 'blue', 'green', 'pink', 'striped', 'yellow', 'test'])
        # Initialize all allowed keys to false
        self.__dict__.update((key, False) for key in allowed_colors)
        # Update the given keys by their given names
        self.__dict__.update((key, value) for key, value in kwargs.items() if key in allowed_colors)

        # Add all balls to the contents list
        self.contents = []
        for color, number in kwargs.items():
            for _ in range(number):
                self.contents.append(color)
        
        self.drawn_balls = []

    def draw(self, number):
        ball = ''
        if number >= len(self.contents):
            self.drawn_balls = self.contents
        else:
            for _ in range(number):
                # Generate random integer
                index = random.randint(0,  len(self.contents) - 1)
                # Remove balls at random from contents list
                ball = self.contents.pop(index)
                self.drawn_balls.append(ball)
        
        return self.drawn_balls

    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    M = 0
    for N in range(num_experiments):
        
        # Create a copy of hat object, so the number of balls doesn´t change each iteration
        new_hat = copy.deepcopy(hat)
        #print(new_hat.contents)

        actual_balls = new_hat.draw(num_balls_drawn)
        #print(actual_balls)

        # If number of balls drawn is greater or equal than all the balls contained in the heat, the probability is 1
        if num_balls_drawn >= len(new_hat.contents):
            M = 1
            N = 1
            break

        actual_balls_dict = {}
        for ball in actual_balls:
            actual_balls_dict[ball] = actual_balls_dict.get(ball, 0) + 1

        #print(actual_balls_dict)
        
        results = []
        for color, number in expected_balls.items():
            # If the expected color is not an actual ball color append true
            if color not in actual_balls_dict.keys():
                results.append(False)
                break
            # Find if number of expected balls is equal or less than actual balls
            elif number <= actual_balls_dict[color]:
                results.append(True)
            else:
                results.append(False)

        # If all elemets of results are true add 1 to M
        result = all(results)
        if result:
            M += 1

    probability = M/N

    return probability

