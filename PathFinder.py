def find_path(ex_map, vision_matrix, in_coords, out_coords):
    start = (in_coords[0] - vision_matrix[0], in_coords[1] - vision_matrix[1])
    finish = (out_coords[0] - vision_matrix[0], out_coords[1] - vision_matrix[1])
    matrix = path_matrix(ex_map, vision_matrix)
    wave(matrix, start, finish)
    path = reverse(matrix, finish)
    path.reverse()
    return path


def path_matrix(ex_map, vision_matrix):
    matrix = []
    for x in range(0, vision_matrix[2] - vision_matrix[0] + 1):
        matrix.append([])
        for y in range(0, vision_matrix[3] - vision_matrix[1] + 1):
            matrix[x].append(-1)
            if ex_map.TileArray[vision_matrix[0] + x][vision_matrix[1] + y].id == 2:
                matrix[x][y] = 99
    return matrix


def wave(matrix, start, finish):
    counter = 1
    matrix[start[0]][start[1]] = counter
    while matrix[finish[0]][finish[1]] == -1:
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == counter:
                    if x + 1 < len(matrix):
                        if matrix[x + 1][y] == -1:
                            matrix[x + 1][y] = counter + 1
                    if x - 1 >= 0:
                        if matrix[x - 1][y] == -1:
                            matrix[x - 1][y] = counter + 1
                    if y + 1 < len(matrix[x]):
                        if matrix[x][y + 1] == -1:
                            matrix[x][y + 1] = counter + 1
                    if y - 1 >= 0:
                        if matrix[x][y - 1] == -1:
                            matrix[x][y - 1] = counter + 1
        counter += 1
    return matrix


def reverse(matrix, finish):
    path = [finish]
    counter = matrix[finish[0]][finish[1]]
    p_x, p_y = finish
    while counter != 2:
        finish_search = False
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if p_x + 1 < len(matrix):
                    if matrix[p_x + 1][p_y] == counter - 1:
                        path.append((p_x + 1, p_y))
                        p_x += 1
                        finish_search = True
                        break
                if p_x - 1 > 0:
                    if matrix[p_x - 1][p_y] == counter - 1:
                        path.append((p_x - 1, p_y))
                        p_x -= 1
                        finish_search = True
                        break
                if p_y + 1 < len(matrix[x]):
                    if matrix[p_x][p_y + 1] == counter - 1:
                        path.append((p_x, p_y + 1))
                        p_y += 1
                        finish_search = True
                        break
                if p_y - 1 > 0:
                    if matrix[p_x][p_y - 1] == counter - 1:
                        path.append((p_x, p_y - 1))
                        p_y -= 1
                        finish_search = True
                        break
            if finish_search:
                counter -= 1
                break
    return path
