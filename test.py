import numpy as np

arr2d = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])


def func(pred: np.ndarray, target: np.ndarray):
    assert pred.shape == target.shape, 'Shape mismatch'
    assert pred.ndim == 1, 'Wrong dimesion'

    return ((((pred - target) ** 2).sum()) / pred.size)

def func2(pred: np.ndarray, target: np.ndarray):
    assert pred.shape == target.shape, 'Shape mismatch'
    assert pred.ndim == 2, 'Wrong dimesion'

    return ((((pred - target) ** 2).sum(axis=1)) / (pred.size / pred.shape[0]))

def func3(pred: np.ndarray, target: np.ndarray):
    assert pred.shape == target.shape, 'Shape mismatch'
    assert pred.ndim == 1, 'Wrong dimesion'

    return (((abs(pred - target)).sum()) / pred.size)

def func4(pred: np.ndarray, target: np.ndarray):
    assert pred.shape == target.shape, 'Shape mismatch'
    assert pred.ndim == 2, 'Wrong dimesion'

    return (((abs(pred - target)).sum(axis=1)) / (pred.size / pred.shape[0]))

def func5(pred: np.ndarray, target: np.ndarray):
    assert pred.shape == target.shape, 'Shape mismatch'
    assert pred.ndim == 1, 'Wrong dimesion'

    return len([i for i in range(len(pred)) if pred[i] == target[i]]) / len(pred)

def func6(pred: np.ndarray, target: np.ndarray):
    assert pred.shape == target.shape, 'Shape mismatch'
    assert pred.ndim == 2, 'Wrong dimesion'

    return np.array([(len([i for i in range(len(pred[row])) if pred[row, i] == target[row, i]]) / len(pred[row])) for row in range(len(pred))])

def func7():
    l = []
    while (ans := input('>> ')) != '0':
        l.append(ans.strip().split(' '))
    l = np.array(l)
    correct_ans = np.array(input('>> ').strip().split(' '))
    scores = np.array([int(i) for i in (input('>> ').strip().split(' '))])
    print(list(np.array([(sum([scores[i] for i in range(len(l[row])) if l[row, i] == correct_ans[i]])) for row in range(len(l))])))


print(func6(np.array([[10, 20, 60, 15, 45], [10, 20, 60, 15, 45], [10, 20, 60, 15, 45]]), np.array([[20, 20, 55, 10, 70], [20, 20, 55, 10, 70], [20, 20, 55, 10, 70]])))
func7()