# A = input("Enter amount: ")
p = float(input("Enter principle: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print(f"\n\n\n\nprinciple = {p}\nrate = {r}\ntime = {t}\n\n\n\n")

A = p*(1+r/100)**t

print(f"Amount is = {A}")

print("See compund interest amount?")
ci_c = input("Enter yes or no: ")

if ci_c == "yes":
    print(f"Compund interest is = {A-p}")
else:
    print("Okay")



# Enter principle: 1000
# Enter rate: 5
# Enter time: 2




# principle = 1000.0
# rate = 5.0
# time = 2.0




# Amount is = 1102.5
# See compund interest amount?
# Enter yes or no: yes
# Compund interest is = 102.5