import my_temp_conversions

# Pruebas para C_to_F
celsius = 75
fahrenheit = my_temp_conversions.C_to_F(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")

# Pruebas para F_to_C
fahrenheit = 98
celsius = my_temp_conversions.F_to_C(fahrenheit)
print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius")

# Pruebas para K_to_C
kelvin = 234
celsius = my_temp_conversions.K_to_C(kelvin)
print(f"{kelvin} grados Kelvin son {celsius} grados Celsius")

# Pruebas para C_to_K
celsius = 543
kelvin = my_temp_conversions.C_to_K(celsius)
print(f"{celsius} grados Celsius son {kelvin} grados Kelvin")

# Pruebas para F_to_K
fahrenheit = 78
kelvin = my_temp_conversions.F_to_K(fahrenheit)
print(f"{fahrenheit} grados Fahrenheit son {kelvin} grados Kelvin")

# Pruebas para K_to_F
kelvin = 231
fahrenheit = my_temp_conversions.K_to_F(kelvin)
print(f"{kelvin} grados Kelvin son {fahrenheit} grados Fahrenheit")
