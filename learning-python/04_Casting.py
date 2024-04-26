# casting - merubah satu tipe data ke tipe lain
# tipe data ada : string, interger, float, boolean

# STRING
print("====STRING====")
data_str = "12"
data_int   = int(data_str)     # string harus angka
data_float = float(data_str)   # float harus angka
data_bool  = bool(data_str)    # akan false jika string 0

print("data : ", data_int, "type : ", type(data_int))
print("data : ", data_float, "type : ", type(data_float))
print("data : ", data_bool, "type : ", type(data_bool))


# INTERGER
print("====INTERGER====")
data_int = 12
data_str   = str(data_int)    
data_float = float(data_int)  
data_bool  = bool(data_int)    

print("data : ", data_str, "type : ", type(data_str))
print("data : ", data_float, "type : ", type(data_float))
print("data : ", data_bool, "type : ", type(data_bool)) # false apabila 0


# FLOAT
print("====FLOAT====")
data_float = 0
data_int   = int(data_float)     
data_str   = str(data_float)   
data_bool  = bool(data_float)    # akan false jika float 0

print("data : ", data_int, "type : ", type(data_int))
print("data : ", data_str, "type : ", type(data_str))
print("data : ", data_bool, "type : ", type(data_bool))


# BOOLEAN
print("====BOOLEAN====")
data_bool = True
data_int   = int(data_bool)     
data_str   = str(data_bool)   
data_float  = bool(data_bool) 

print("data : ", data_int, "type : ", type(data_int))
print("data : ", data_str, "type : ", type(data_str))
print("data : ", data_float, "type : ", type(data_float))
