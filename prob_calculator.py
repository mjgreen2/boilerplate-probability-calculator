#Solution to Probability Calculator
#Created in Visual Studio Code
#By Michael Green

import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **balls):
        self.__dict__.update(balls)
        color_list = list(self.__dict__.keys())
        self.contents = []

        #convert dict (balls) into list (contents). Ex. {red:2} -> [red, red]
        for ball_cntr in range(0, len(color_list), 1) :
            number_ball = self.__dict__.get(color_list[ball_cntr], 0)
            for color_cntr in range(0, number_ball, 1):
                self.contents.append(color_list[ball_cntr])

    '''The `Hat` class should have a `draw` method that accepts an argument 
    indicating the number of balls to draw from the hat. This method should 
    remove balls at random from `contents` and return those balls as a list of strings. 
    The balls should not go back into the hat during the draw, 
    similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.
    '''
    def draw(self, draw_number):
        number_to_draw = draw_number
        if number_to_draw > len(self.contents):
            number_to_draw = len(self.contents)

        ball_list = []
        for draw_cntr in range(0, number_to_draw, 1):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            ball_list.append(ball)

        return ball_list


'''The `experiment` function should return a probability. Perform `N` experiments, 
count how many times `M` we get at least 'expected_balls', 
and estimate the probability as `M/N`.
'''
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):   
    successful_experiments = 0
    for exp_cntr in range(0, num_experiments, 1):
        match = 0
        duplicate = copy.deepcopy(hat)
        raw_results = duplicate.draw(num_balls_drawn)
        #convert rawResults list into dict for comparison
        processed_results = convert_list_to_dict(raw_results)

        #check if color is in hat. If yes, compare values. 
        # Match = number of drawn balls equals/exceeds number expected_balls 
        balls_from_draw_list = list(processed_results.keys())
        for check_cntr in range(0, len(balls_from_draw_list), 1):
            if balls_from_draw_list[check_cntr] in expected_balls:
                if processed_results.get(balls_from_draw_list[check_cntr]) >=   expected_balls.get(balls_from_draw_list[check_cntr]):
                    match += 1
                else:
                    continue
            else:
                continue
        #success if all drawn matches expected in color and number
        if match == len(expected_balls):
            successful_experiments += 1

    return successful_experiments/num_experiments

# Function: list of colors to dict of color:number
# Ex. [red, green, red] -> {green:1, red:2}
def convert_list_to_dict(list):
    conversion = {}
    list.sort()
    value = 0
    list_key = list[0]
    for list_cntr in range(0, len(list), 1):
        item = list[list_cntr]
        if item is list_key :
            value += 1
        else:
            conversion[list_key] = value
            list_key = item
            value = 1

    conversion[list_key] = value
    return conversion