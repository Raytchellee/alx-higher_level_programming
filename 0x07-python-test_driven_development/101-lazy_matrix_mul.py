#!/usr/bin/python3
"""Multiplies matrix using Numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplies two matrices

    Args:
        m_a: matrix a
        m_b: matrix b
    """

    return (np.matmul(m_a, m_b))
