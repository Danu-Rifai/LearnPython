#casting

#casting integer
print("===INTEGER===")
data_int = 9;

data_str = str(data_int)
data_float = float(data_int)
data_bool = bool(data_int)
print(f"data = {data_str} bertipe : {type(data_str)}")
print(f"data = {data_float} bertipe : {type(data_float)}")
print(f"data = {data_bool} bertipe : {type(data_bool)}")

print("===FLOAT===")
data_float = 3.14

data_str = str(data_float)
data_int = int(data_float)
data_bool = bool(data_float)
print(f"data = {data_str} bertipe : {type(data_str)}")
print(f"data = {data_int} bertipe : {type(data_int)}") #pembulatan kebawah
print(f"data = {data_bool} bertipe : {type(data_bool)}")

print("===BOLEAN===")
data_bool = True

data_str = str(data_bool)
data_int = int(data_bool)
data_float = float(data_bool)
print(f"data = {data_str} bertipe : {type(data_str)}")
print(f"data = {data_int} bertipe : {type(data_int)}") 
print(f"data = {data_float} bertipe : {type(data_float)}")

print("===STRING===")

data_str = "7"
# jika string berisi angka maka bisa dicasting ke int ataupun float
# jika string terisi maka akan mengembalikan nilai true jika tidak maka false

data_bool = bool(data_str)
print(f"data = {data_bool} bertipe : {type(data_bool)}")
data_int = int(data_str) 
print(f"data = {data_int} bertipe : {type(data_int)}") 
data_float = float(data_str)
print(f"data = {data_float} bertipe : {type(data_float)}")