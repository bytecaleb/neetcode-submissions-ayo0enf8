class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        result = init
        x = init

        if iterations == 0:
            return result
        else:
            for i in range(iterations):

                derivative = 2 * x
                result = x - learning_rate * derivative
                x = result

        return round(result,5)
        
    