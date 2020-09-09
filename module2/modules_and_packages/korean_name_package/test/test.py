import korean_name.korean_name as kn

my_bdate = kn.get_birth_date()

print(my_bdate)
print(kn.get_korean_name(*my_bdate))