import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle


def add_two_numbers_together(a: int, b: int) -> int:
    """Add two numbers together
    Args:
        a (int): first number
        b (int): second number
    Returns:
        int: sum of a and b
    """

    return a + b


df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))

X = df[['A', 'B', 'C']]
y = df['D']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open(f"{pd.to_datetime('today').normalize()}test_model.pkl", 'wb'))
