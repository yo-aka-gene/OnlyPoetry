import os
import random

import numpy as np


def random_state(seed: int) -> None:
    """
    Set the random seed for Python, OS hash environment, and NumPy.

    This function ensures reproducibility by fixing the seeds across multiple
    random number generators commonly used in data science workflows.

    Parameters
    ----------
    seed : int
        The seed value to be used for the random number generators.
    """
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    np.random.seed(seed)
