#major current problems
#recursives functions are very inefficient, also, there's a lot of functions that does similar tasks

##---------------- shape
def shape(data):
    #data verify
    if not isinstance(data, (list, tuple, Array)):
        return ()
    data_shape = [len(data)]
    if data_shape == [0]:
        return (0,)
    element = data[0]

    #just looking first element shape
    while isinstance(element, (list, tuple, Array)):
        element_size = len(element)
        data_shape.append(element_size)
        if element_size == 0:
            break
        element = element[0]

    #checking if all elements in the same dimension have the same shape
    if not isinstance(data, Array): #Array class will verify shape, then, isn't necessary to verify again
        validate_shape(data, 1, data_shape)
    return tuple(value for value in data_shape)

def validate_shape(current_data, dimension, data_shape):
    for element in current_data:
        if not isinstance(element, (list, tuple, Array)):
            if dimension < len(data_shape): #if the non list/tuple/array value isn't in the last dimension
                raise ValueError("Different array elements size")
            continue
        if (dimension >= len(data_shape)) or (data_shape[dimension] != len(element)):
            #(if there's a list/tuple/array in or above the last dimension) or (shape mismatch)
            raise ValueError("Different array elements size")
        validate_shape(element, dimension + 1, data_shape)

def ndim(data):
    return len(shape(data))

def size(data, axis=None):
    data_shape = shape(data)
    if axis is None:
        result = 1
        for element in data_shape:
            result *= element
        return result
    elif isinstance(axis, (int, float)):
        return data_shape[axis]
    else:
        raise ValueError("Axis needs to be an int, float or None")
    

##----------------- Array
class Array: 
    def __init__(self, data): 
        self.shap = shape(data)
        self.data = data

    def __repr__(self):
        return f"Array({self.data})"
    
    def __str__(self):
        return f"{self.data}"
    
    def __len__(self):
        if not isinstance(self.data, (list, tuple, Array)):
            raise ValueError("Only lists and tuples supports 'len()'")
        return len(self.data)
    
    def __getitem__(self, item):
        #verifying item
        if not isinstance(item, tuple):
            item = (item,)
        array_dim_qty = len(self.shap)
        if len(item) > array_dim_qty:
            raise ValueError("Too many indexes")
        while len(item) < array_dim_qty:
            item += (slice(None),)

        #getting the result
        result = recursive_get(self.data, item)
        
        if isinstance(result, list):
            return Array(result)
        return result

    
    def __setitem__(self, item, new_value):
        #verifying item
        if not isinstance(item, tuple):
            item = (item,)
        array_dim_qty = len(self.shap)
        if len(item) > array_dim_qty:
            raise ValueError("Too many indexes")
        while len(item) < array_dim_qty:
            item += (slice(None),)
        
        #getting the result
        return recursive_set(self.data, item, new_value)
        

    def __iter__(self):
        return iter(self.data)
    
    def __add__(self, other):
        #verifying other
        if not isinstance(other, (int, float, list, tuple, Array)):
            raise ValueError(f"'{other}' can't be added")
        if not isinstance(other, (int, float)):
            if self.shap != shape(other):
                raise ValueError("Arrays must have the same shape")

        #getting the result
        result = recursive_copy(self.data)
        recursive_add(result, other, len(self.shap))
        return result

    def __radd__(self, other):
        #verifying other
        if not isinstance(other, (int, float, list, tuple, Array)):
            raise ValueError("")
        if not isinstance(other, (int, float)):
            if self.shap != shape(other):
                raise ValueError("")

        #getting the result
        result = recursive_copy(self.data)
        recursive_add(result, other, len(self.shap))
        return result

    def __sub__(self, other):
        #verifying other
        if not isinstance(other, (int, float, list, tuple, Array)):
            raise ValueError("")
        if not isinstance(other, (int, float)):
            if self.shap != shape(other):
                raise ValueError("")

        #getting the result
        result = recursive_copy(self.data)
        recursive_sub(result, other, len(self.shap))
        return result

    def __rsub__(self, other):
        #verifying other
        if not isinstance(other, (int, float, list, tuple, Array)):
            raise ValueError("")
        if not isinstance(other, (int, float)):
            if self.shap != shape(other):
                raise ValueError("")

        #getting the result
        result = recursive_copy(self.data)
        recursive_reverse_sub(result, other, len(self.shap))
        return result

    def __mul__(self, other):
        #verifying other
        if not isinstance(other, (int, float, list, tuple, Array)):
            raise ValueError("")
        if not isinstance(other, (int, float)):
            if self.shap != shape(other):
                raise ValueError("")

        #getting the result
        result = recursive_copy(self.data)
        recursive_mul(result, other, len(self.shap))
        return result

    def __rmul__(self, other):
                #verifying other
        if not isinstance(other, (int, float, list, tuple, Array)):
            raise ValueError("")
        if not isinstance(other, (int, float)):
            if self.shap != shape(other):
                raise ValueError("")

        #getting the result
        result = recursive_copy(self.data)
        recursive_mul(result, other, len(self.shap))
        return result

    def __truediv__(self, other):
        #verifying other
        if not isinstance(other, (int, float, list, tuple, Array)):
            raise ValueError("")
        if not isinstance(other, (int, float)):
            if self.shap != shape(other):
                raise ValueError("")

        #getting the result
        result = recursive_copy(self.data)
        recursive_truediv(result, other, len(self.shap))
        return result

    def __rtruediv__(self, other):
        #verifying other
        if not isinstance(other, (int, float, list, tuple, Array)):
            raise ValueError("")
        if not isinstance(other, (int, float)):
            if self.shap != shape(other):
                raise ValueError("")

        #getting the result
        result = recursive_copy(self.data)
        recursive_reverse_truediv(result, other, len(self.shap))
        return result

    def sum(self, axis=None):
        return my_sum(self.data, axis)

    def mean(self, axis=None):
        return my_mean(self.data, axis)
    
    def max(self, axis=None):
        return my_max(self.data, axis)
    
    def min(self, axis=None):
        return my_min(self.data, axis)

    def shape(self): #missing @property
        return self.shap

#functions for methods ----------------
def my_min(array, axis=None):
    if axis is not None:
        if len(shape(array)) <= axis:
            if len(shape(array)) == 0:
                return array
            raise ValueError(f"The array doens't have '{axis}' axis ")
            
    #getting the result
    result = recursive_min(array, axis)

    if isinstance(result, list):
        return Array(result)
    return result

def recursive_min(array, axis):
    result = float("inf")
    if isinstance(array[0], (int, float)):
        for element in array:
            if element < result:
                result = element
        return result
    elif isinstance(array[0], (list, tuple, Array)):
        if axis is None:
            for element in array:
                attempt = recursive_min(element, axis)
                if attempt < result:
                    result = attempt
            return result
        elif axis == 0:
            result = array[0]
            for element in array[1:]:
                result = recursive_min_axis0(result, element)
            return result
        return [recursive_min(element, axis - 1) for element in array]
    else:
        raise ValueError("The array contains values that are not numbers")

def recursive_min_axis0(current_min, competitor_min):
    if isinstance(current_min, (int, float)):
        if current_min < competitor_min:
            return current_min
        return competitor_min
    return [recursive_min_axis0(a, b) for a, b in zip(current_min, competitor_min)]

def my_max(array, axis=None):
    if axis is not None:
        if len(shape(array)) <= axis:
            if len(shape(array)) == 0:
                return array
            raise ValueError(f"The array doens't have '{axis}' axis ")
            
    #getting the result
    result = recursive_max(array, axis)

    if isinstance(result, list):
        return Array(result)
    return result

def recursive_max(array, axis):
    result = float("-inf")
    if isinstance(array[0], (int, float)):
        for element in array:
            if element > result:
                result = element
        return result
    elif isinstance(array[0], (list, tuple, Array)):
        if axis is None:
            for element in array:
                attempt = recursive_max(element, axis)
                if attempt > result:
                    result = attempt
            return result
        elif axis == 0:
            result = array[0]
            for element in array[1:]:
                result = recursive_max_axis0(result, element)
            return result
        return [recursive_max(element, axis - 1) for element in array]
    else:
        raise ValueError("The array contains values that are not numbers")

def recursive_max_axis0(current_max, competitor_max):
    if isinstance(current_max, (int, float)):
        if current_max > competitor_max:
            return current_max
        return competitor_max
    return [recursive_max_axis0(a, b) for a, b in zip(current_max, competitor_max)]

def my_mean(array, axis=None):
    return my_sum(array, axis) / size(array, axis)

def my_sum(array, axis=None):
        #verifying
        if axis is not None:
            if len(shape(array)) <= axis:
                if len(shape(array)) == 0:
                    return array
                raise ValueError("")

        #getting the result
        result = recursive_sum(array, axis)

        if isinstance(result, list):
            return Array(result)
        return result

def recursive_sum(array, axis): 
    result = 0
    if isinstance(array[0], (int, float)):
        for element in array:
            result += element
        return result
    elif isinstance(array[0], (list, tuple, Array)):
        if axis is None:
            for element in array:
                result += recursive_sum(element, axis)
            return result
        elif axis == 0:
            result = [0] * len(array[0])
            for element in array:
                for idx in range(len(element)):
                    result[idx] += Array(element[idx])
            return result
        return [recursive_sum(element, axis - 1) for element in array]
    else:
        raise ValueError("The array contains values that are not numbers")

#functions for dunder methods ---------------
def recursive_reverse_truediv(array, value, dim): 
    if isinstance(value, (int, float)):
        for idx, element in enumerate(array):
            if isinstance(element, (int, float)):
                array[idx] = value / array[idx]
            else:
                recursive_reverse_truediv(element, value, dim - 1)
    elif isinstance(value, (list, tuple, Array)):
        for idx in range(len(array)):
            if dim == 1:
                array[idx] = value[idx] / array[idx]
            else:
                recursive_reverse_truediv(array[idx], value[idx], dim - 1)
    else:
        raise ValueError(f"'{value}' can't be divided")

def recursive_truediv(array, value, dim):
    if isinstance(value, (int, float)):
        for idx, element in enumerate(array):
            if isinstance(element, (int, float)):
                array[idx] /= value
            else:
                recursive_truediv(element, value, dim - 1)
    elif isinstance(value, (list, tuple, Array)):
        for idx in range(len(array)):
            if dim == 1:
                array[idx] /= value[idx]
            else:
                recursive_truediv(array[idx], value[idx], dim - 1)
    else:
        raise ValueError(f"'{value}' can't be divided")
    
def recursive_mul(array, value, dim):
    if isinstance(value, (int, float)):
        for idx, element in enumerate(array):
            if isinstance(element, (int, float)):
                array[idx] *= value
            else:
                recursive_mul(element, value, dim - 1)
    elif isinstance(value, (list, tuple, Array)):
        for idx in range(len(array)):
            if dim == 1:
                array[idx] *= value[idx]
            else:
                recursive_mul(array[idx], value[idx], dim - 1)
    else:
        raise ValueError(f"'{value}' can't be multiplied")

def recursive_reverse_sub(array, value, dim): 
    if isinstance(value, (int, float)):
        for idx, element in enumerate(array):
            if isinstance(element, (int, float)):
                array[idx] = value - array[idx]
            else:
                recursive_reverse_sub(element, value, dim - 1)
    elif isinstance(value, (list, tuple, Array)):
        for idx in range(len(array)):
            if dim == 1:
                array[idx] = value[idx] - array[idx]
            else:
                recursive_reverse_sub(array[idx], value[idx], dim - 1)
    else:
        raise ValueError(f"'{value}' can't be subtracted")

def recursive_sub(array, value, dim):
    if isinstance(value, (int, float)):
        for idx, element in enumerate(array):
            if isinstance(element, (int, float)):
                array[idx] -= value
            else:
                recursive_sub(element, value, dim - 1)
    elif isinstance(value, (list, tuple, Array)):
        for idx in range(len(array)):
            if dim == 1:
                array[idx] -= value[idx]
            else:
                recursive_sub(array[idx], value[idx], dim - 1)
    else:
        raise ValueError(f"'{value}' can't be subtracted")

def recursive_add(array, value, dim):
    if isinstance(value, (int, float)):
        for idx, element in enumerate(array):
            if isinstance(element, (int, float)):
                array[idx] += value
            else:
                recursive_add(element, value, dim - 1)
    elif isinstance(value, (list, tuple, Array)):
        for idx in range(len(array)):
            if dim == 1:
                array[idx] += value[idx]
            else:
                recursive_add(array[idx], value[idx], dim - 1)
    else:
        raise ValueError(f"'{value}' can't be added")

def recursive_copy(array):
    if isinstance(array, (int,float)):
        return array
    return [recursive_copy(element) for element in array]

def recursive_set(array, indexes, value):
    current_index = indexes[0]
    remaining_indexes = indexes[1:]

    if isinstance(current_index, int):
        if len(indexes) == 1:
            array[current_index] = value
            return array 
        recursive_set(array[current_index], remaining_indexes, value)
        return array
    elif isinstance(current_index, slice):
        if len(indexes) == 1:
            array[current_index] = [value] * len(array[current_index])
            return array
        for element in array[current_index]:
            recursive_set(element, remaining_indexes, value)
        return array
    elif isinstance(current_index, list):
        if len(indexes) == 1:
            for idx in current_index:
                array[idx] = value
            return array
        for idx in current_index:
            recursive_set(array[idx], remaining_indexes, value)
        return array
    raise ValueError("Invalid index")

def recursive_get(array, indexes):
    if len(indexes) == 0:
        return array
    current_index = indexes[0]
    remaining_indexes = indexes[1:]

    if isinstance(current_index, int):
        return recursive_get(array[current_index], remaining_indexes)
    elif isinstance(current_index, slice):
        return [recursive_get(element, remaining_indexes) for element in array[current_index]]
    elif isinstance(current_index, list):
        return [recursive_get(array[idx], remaining_indexes) for idx in current_index]
    raise ValueError("Invalid index")
