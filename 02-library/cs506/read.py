def read_csv(csv_file_path):
    matrix = []
    # raise NotImplementedError()
    with open(csv_file_path, 'r') as f:
        for line in f:
            # Convert line to arr and replace '?' with nan
            lineArr = line.split(',')
            for i in range(len(lineArr)):
                try:
                    lineArr[i] = int(lineArr[i])
                except:
                    lineArr[i] = eval(lineArr[i])
            matrix.append(lineArr)

    return matrix
