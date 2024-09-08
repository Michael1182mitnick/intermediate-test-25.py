# Write a function to flatten a nested list into a single list of values.

def flatten(nested_list):
    """
    Function to flatten a nested list into a single list of values.

    :param nested_list: List that may contain nested lists.
    :return: A flat list containing all values from the nested list.
    """
    flat_list = []

    def flatten_helper(lst):
        for item in lst:
            # If the item is a list, recursively flatten it
            if isinstance(item, list):
                flatten_helper(item)
            else:
                # Otherwise, add the item to the flat list
                flat_list.append(item)

    # Start the flattening process
    flatten_helper(nested_list)
    return flat_list


# Example usage
nested_list = [1, [2, [3, 4], 5], 6]
flattened = flatten(nested_list)
print("Flattened list:", flattened)
