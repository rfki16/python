# tipe data interger
data_interger = 1
print("data : ", data_interger)
print("- tipe : ", type(data_interger))

# tipe data float
data_float = 1.5
print("data : ", data_float)
print("- tipe : ", type(data_float))

# tipe data string
data_string = "agus"
print("data : ", data_string)
print("- tipe : ", type(data_string))

# tipe data boolean
data_boolean = True
print("data : ", data_boolean)
print("- tipe : ", type(data_boolean))

## tipe data khusus

# tipe data complex
data_complex = complex(5,7)
print("data : ", data_complex)
print("- tipe : ", type(data_complex))

# tipe data bahasa C
from ctypes import c_double

data_c_double = c_double(17.25)
print("data : ", data_c_double)
print("- tipe : ", type(data_c_double))
