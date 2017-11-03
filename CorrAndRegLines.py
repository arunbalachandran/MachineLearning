def est_std_dev(x):
    if len(x) <= 1:
        return 0.0
    mean = sum(x) / len(x)
    dev_sum = 0.0
    for i in x:
        dev_sum += abs(i - mean)**2
    dev_sum /= (len(x) - 1)
    dev_sum = (dev_sum)**0.5
    return dev_sum

def pearson_corr_coeff(x, y):
    if len(x) <= 1 or len(y) <= 1:
        return 0 
    std_dev_x = est_std_dev(x)
    std_dev_y = est_std_dev(y)
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    summation = 0.0
    for i in range(len(x)):
        summation += (x[i] - mean_x)*(y[i] - mean_y)
    summation = summation/(std_dev_x * std_dev_y * (len(x) - 1)) 
    return summation
