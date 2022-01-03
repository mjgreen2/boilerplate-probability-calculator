#Solution to Probability Calculator
#Created in Visual Studio Code
#By Michael Green

import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls):
        self.__dict__.update(balls)
        colorList = list(self.__dict__.keys())
        self.contents = []

        #convert dict (balls) into list (contents). Ex. {red:2} -> [red, red]
        for ballCntr in range(0, len(colorList), 1) :
            numberBall = self.__dict__.get(colorList[ballCntr], 0)
            for colorCntr in range(0, numberBall, 1):
                self.contents.append(colorList[ballCntr])

    '''The `Hat` class should have a `draw` method that accepts an argument 
    indicating the number of balls to draw from the hat. This method should 
    remove balls at random from `contents` and return those balls as a list of strings. 
    The balls should not go back into the hat during the draw, 
    similar to an urn experiment without replacement. If the number of balls to draw 
    exceeds the available quantity, return all the balls.'''
    def draw(self, drawNumber):
        numberToDraw = drawNumber
        if numberToDraw > len(self.contents):
            numberToDraw = len(self.contents)

        ballList = []
        for drawCntr in range(0, numberToDraw, 1):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            ballList.append(ball)

        return ballList

'''The `experiment` function should return a probability. Perform `N` experiments, 
count how many times `M` we get at least 'expected_balls', 
and estimate the probability as `M/N`.'''
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):   
    successful_experiments = 0
    for expCntr in range(0, num_experiments, 1):
        match = 0
        duplicate = copy.deepcopy(hat)
        rawResults = duplicate.draw(num_balls_drawn)
        #convert rawResults list into dict for comparison
        processedResults = list_to_dict(rawResults)

        #check if color is in hat. If yes, compare values. 
        # Match = number of drawn balls equals/exceeds number expected_balls 
        expBallsList = list(processedResults.keys())
        for checkCntr in range(0, len(expBallsList), 1):
            if expBallsList[checkCntr] in expected_balls:
                if processedResults.get(expBallsList[checkCntr]) >= expected_balls.get(expBallsList[checkCntr]):
                    match += 1
                else:
                    continue
            else:
                continue
        #success if all drawn matches expected in color and number
        if match == len(expected_balls):
            successful_experiments += 1

    return successful_experiments/num_experiments

'''Function: list of colors to dict of color:number
Ex. [red, green, red] -> {green:1, red:2}'''
def list_to_dict(list):
    conversion = {}
    list.sort()
    value = 0
    listKey = list[0]
    for lstCntr in range(0, len(list), 1):
        item = list[lstCntr]
        if item is listKey :
            value += 1
        else:
            conversion[listKey] = value
            listKey = item
            value = 1

    conversion[listKey] = value
    return conversion