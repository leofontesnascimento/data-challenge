import math
import numpy as np


def sort_matrix(m):
    return np.sort(m)


def calculate_median(m):
    sorted = sort_matrix(m)
    print('sorted_matrix: ', sorted)
    medium = math.ceil(sorted.size / 2)
    if sorted.size % 2 != 0:
        return sorted[medium - 1]
    else:
        last_left = sorted[medium - 1]
        first_right = sorted[medium]
        return (last_left + first_right) / 2


def main():
    print('[A] matrix with size 5x1')
    m = np.array([9, 11, 16, 7, 2])
    print('matrix: ', m)
    median = calculate_median(m)
    print('median: ', median)

    print('----------------------------------')

    print('[B] matrix with size 6x1')
    m = np.array([1, 2, 3, 4, 5, 6])
    print('matrix: ', m)
    median = calculate_median(m)
    print('median: ', median)

    print('----------------------------------')

    print('[C] matrix with size 8x1')
    m = np.array([1, 2, 3, 4, 5, 6, 9, 10])
    print('matrix: ', m)
    median = calculate_median(m)
    print('median: ', median)

    print('----------------------------------')

    print('[D] combine two matrix with size 5x1')
    m_1 = np.array([9, 11, 16, 7, 2])
    print('matrix m_1: ', m_1)
    m_2 = np.array([9, 11, 16, 7, 2])
    print('matrix m_2: ', m_2)
    combined = np.concatenate((m_1, m_2))
    print('matrix combined: ', combined)
    median = calculate_median(combined)
    print('median: ', median)

    print('----------------------------------')

    print('[E] combine two matrix with size 5x1 and 8x1')
    m_1 = np.array([9, 11, 16, 7, 2])
    print('matrix m_1: ', m_1)
    m_2 = np.array([1, 2, 3, 4, 5, 6, 9, 10])
    print('matrix m_2: ', m_2)
    combined = np.concatenate((m_1, m_2))
    print('matrix combined: ', combined)
    median = calculate_median(combined)
    print('median: ', median)

if __name__ == "__main__":
    main()
