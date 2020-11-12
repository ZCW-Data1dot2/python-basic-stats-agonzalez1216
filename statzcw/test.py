import zcount
import zmean
import zmedian
import zvariance
import zstddev
import zstderr
import zmode
import zcorr
import csv
f0 = open('/Users/alfonso/PycharmProjects/pythonBasicStats/python-basic-stats-agonzalez1216/dataZero.csv', mode='r')
f1 = open('/Users/alfonso/PycharmProjects/pythonBasicStats/python-basic-stats-agonzalez1216/dataOne.csv', mode='r')
f2 = open('/Users/alfonso/PycharmProjects/pythonBasicStats/python-basic-stats-agonzalez1216/dataTwo.csv', mode='r')
f3 = open('/Users/alfonso/PycharmProjects/pythonBasicStats/python-basic-stats-agonzalez1216/dataThree.csv', mode='r')


def create_dictionaries(file_dict):
    ret_x_list = list()
    ret_y_list = list()
    for row in file_dict:
        ret_x_list.append(float(row['x']))
        ret_y_list.append(float(row['y']))
    return ret_x_list, ret_y_list


file0_dict = csv.DictReader(f0)
file1_dict = csv.DictReader(f1)
file2_dict = csv.DictReader(f2)
file3_dict = csv.DictReader(f3)
f0x_values, f0y_values = create_dictionaries(file0_dict)
f0x_count = zcount.count(f0x_values)


# print(f0x_values)
# print(f0x_count)
# print(zmean.mean(f0x_values))
# print(zmedian.median(f0x_values))
# print(zvariance.variance(f0x_values))
# print(zstddev.stddev(f0x_values))
# print(zstderr.stderr(f0x_values))
# print(zmode.mode(f0x_values))
print(zcorr.corr(f0x_values, f0y_values))
