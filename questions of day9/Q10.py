#Write a Python script to merge two Python dictionaries.
d1={1:10,2:20}
d2={3:'unique',4:'shrestha'}
d3={**d1,**d2}
print(d3)
