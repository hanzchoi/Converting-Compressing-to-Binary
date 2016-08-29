import sys


dummy_data_one = "356526070063981,2,08/23/2016 12:04:42,startup"
dummy_data_two = "356526070063981,3,08/23/2016 12:04:42,ignition,0,X,0.00000,0.00000,0,0,0,0,0.00,1,39.89"
dummy_data_three = "356526070063981,4,08/23/2016 12:07:52,gps_pos_time_based_ign_on,160752.0,A,28.10930,-81.62534,0.0,0.0,1,8,1.10,39.89"
dummy_data_four = "356526070061464,11,08/23/2016 07:40:09,gps_pos_distance_based,114010.0,A,40.81248,-73.12586,38.0,267.8,1,7,0.80,1,66.37"
dummy_data_five = "356526070061464,5,08/23/2016 07:32:29,gps_pos_angle_based,113229.0,A,40.82377,-73.02209,36.2,257.2,1,7,1.00,1,57.59"


#print(' '.join(format(ord(x), 'b') for x in dummy_data_one))
#print(' '.join(format(ord(x), 'b') for x in dummy_data_two))
#print(' '.join(format(ord(x), 'b') for x in dummy_data_three))
#print(' '.join(format(ord(x), 'b') for x in dummy_data_four))
#print(' '.join(format(ord(x), 'b') for x in dummy_data_five))

"""
def string_conversion_to_binary(data):
    print(sys.getsizeof(' '.join(format(ord(x), 'b') for x in data)))
    return ' '.join(format(ord(x), 'b') for x in data)

print(sys.getsizeof(dummy_data_one))
print()
print(string_conversion_to_binary(dummy_data_one))
"""

def string_conversion_to_binary(data):
    #print(sys.getsizeof(' '.join(ord(x) for x in data)))
    print()
    return ' '.join(ord(x) for x in data)


print(sys.getsizeof(dummy_data_one))
print(string_conversion_to_binary(sys.getsizeof(dummy_data_one)))

