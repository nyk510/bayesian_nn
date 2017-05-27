# coding: utf-8
__author__ = "nyk510"
"""
人工データ・セットを作成するスクリプト
"""

import numpy as np


def func1(x):
    """
    人工データの正しい関数例その1
    
    :param np.array x: 
    :return: 
    :rtype: np.array
    """
    return x + np.sin(5 * x) - .8


def make_data(size, function_id=1, seed=1):
    """
    人工データの作成
    
    :param int size: 
    :param int function_id: 
    :param int seed: 
    :return: データと正しい関数の集合
    :rtype: tuple of (np.array, np.array, function)
    """
    np.random.seed(seed)
    x = np.sort(np.random.uniform(-1.1, 1.1, size=200)).astype(np.float32)
    x = x[(x < 0.) | (x > .5)]
    f = None
    if function_id == 1:
        f = func1
    else:
        # 別の関数で試したい場合は適当にここで指定する
        raise ValueError

    y = f(x) + np.random.normal(loc=.1, scale=.1, size=x.shape).astype(np.float32)
    y += np.where(np.random.randint(0, 2, x.shape) > 0, np.random.randint(-1, 2, size=x.shape), 0.).astype(np.float32)
    return x, y, f