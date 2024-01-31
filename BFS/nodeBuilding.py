import openpyxl
import time
import matplotlib.pyplot as plt
import numpy as np

def read_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    rows = list(sheet.iter_rows(values_only=True))
    return rows

def final_plot_grid(data, path):
    rows, cols = np.shape(data)

    fig, ax = plt.subplots()
    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    ax.grid(True)

    for i in range(rows):
        for j in range(cols):
            if data[i][j] == 1:
                ax.plot(j, i, marker='o', color='b', markersize=8)
            elif data[i][j] == 'start':
                ax.plot(j, i, marker = 'o', color = 'y', markersize = 10)
            elif data[i][j] == 'goal':
                ax.plot(j, i, marker = 'o', color = 'g', markersize = 10)
            else:
                ax.plot(j, i, marker='o', color='black', markersize=8)
    
    if path:
        if isinstance(path, list):
            for paths in path:
                current = paths
                ax.plot(current[1], current[0], marker = 'o', color = 'orange', markersize = 4)
        else:
            current = path
            ax.plot(current[1], current[0], color='white', marker='o', markersize=4)

    #plt.pause(1)
    plt.show(block=True)
    #plt.close()

def plot_grid(data, path, input_cell = []):
    rows, cols = np.shape(data)

    fig, ax = plt.subplots()
    ax.set_xticks(range(cols))
    ax.set_yticks(range(rows))
    ax.grid(True)

    for i in range(rows):
        for j in range(cols):
            if data[i][j] == 1:
                ax.plot(j, i, marker='o', color='b', markersize=8)
            elif data[i][j] == 'start':
                ax.plot(j, i, marker = 'o', color = 'y', markersize = 10)
            elif data[i][j] == 'goal':
                ax.plot(j, i, marker = 'o', color = 'g', markersize = 10)
            else:
                ax.plot(j, i, marker='o', color='black', markersize=8)
    
    if input_cell:
        ax.plot(input_cell[1], input_cell[0], marker='o', markersize=10, color='white', label='Input Cell')

    if path:
        if isinstance(path, list):
            for paths in path:
                current = paths
                ax.plot(current[1], current[0], marker = 'o', color = 'white', markersize = 4)
        else:
            current = path
            ax.plot(current[1], current[0], color='white', marker='o', markersize=4)

    plt.pause(1)
    #plt.legend()
    plt.show(block=False)
    #time.sleep(1.5)
    plt.close()

# Example usage
# file_path = './map16x22.xlsx'
# excel_data = read_excel(file_path)
# bfs_path = [(0, 1), [(0, 1), (0, 2)]]

# input_cell = (5, 10)

# for path in bfs_path:
#     print(path)
#     plot_grid(excel_data, input_cell, path)


