def tf_transform(count_matrix):
    tf_matrix = []
    for part in count_matrix:
        sum_of_part = sum(part)
        new_part = []
        for el in part:
            new_part.append(round(el / sum_of_part, 3))
        tf_matrix.append(new_part)
    return tf_matrix


if __name__ == '__main__':
    count_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    tf_matrix = tf_transform(count_matrix)
    assert tf_matrix == [[0.143, 0.143, 0.286, 0.143, 0.143,
                          0.143, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.143, 0.0, 0.0, 0.0,
                                                                 0.143, 0.143, 0.143, 0.143, 0.143, 0.143]]
    print(tf_matrix)
