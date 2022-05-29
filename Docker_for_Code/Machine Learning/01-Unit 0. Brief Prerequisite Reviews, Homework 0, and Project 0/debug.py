"""
In this problem, you are given a buggy piece of code and are asked to debug it.

The goal of this exercise is for you to set up a working debugging system for yourselves. (See the next page for an example.) Feel free to use other debuggers as you wish. But note that any extra print statement in submitted code will be graded as incorrect in the online code graders.

The function get_sum_metrics takes two arguments: a prediction and a list of metrics to apply to the prediction (say, for instance, the accuracy or the precision). Note that each metric is a function, not a number. The function should compute each of the metrics for the prediction and sum them. It should also add to this sum three default metrics, in this case, adding 0, 1 or 2 to the prediction.
"""

def get_sum_metrics(predictions, metrics=[]):
    for i in range(3):
        metrics.append(lambda x: x + i)

    sum_metrics = 0
    for metric in metrics:
        sum_metrics += metric(predictions)

    return sum_metrics


print(get_sum_metrics(1, [0,1,2]))