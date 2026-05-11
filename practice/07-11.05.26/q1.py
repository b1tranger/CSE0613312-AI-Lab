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
