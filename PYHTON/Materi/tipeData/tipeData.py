# Tipe data di Python

#integer
data_int = 12
print(data_int)
print(f"- bertipe : {type(data_int)}")

# float
data_float = 22/7 #pi
print(data_float)
print(f"- bertipe : {type(data_float)}")

# string
data_string = "Danu Rifai"
print(data_string)
print(f"- bertipe : {type(data_string)}")

# bolean
data_bolean = True
print(data_bolean)
print(f"- bertipe : {type(data_bolean)}")

## tipe data khusus

# bilangan kompleks
data_complex = complex(5,6) # realnya di depan imajinernya dibelakang
print(data_complex)
print(f"- bertipe : {type(data_complex)}")

#tipe data dari bahasa C

from ctypes import c_double 

data_c_double = c_double(10.5)
print(data_c_double)