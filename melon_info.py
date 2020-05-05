# """Print out all the melons in our inventory."""

from melons import melon_data

def print_melon(melon_data):
    """Print each melon with corresponding attribute information."""

for melon, data in melon_data.items():
    print(melon)
    for key in data:
        print(key + ':', data[key])

# #  Used this source for guidance: 
# #      https://www.learnbyexample.org/python-nested-dictionary/



