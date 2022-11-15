def main(num):
    print(f"{num} AND {num+1} = {num&(num+1)}")
    print(f"{num} OR {num+1} = {num|(num+1)}")
    print(f"{num} XOR {num+1} = {num^(num+1)}")
    print(f"NOT {num} = {~num}")
    print("")


for i in range(100):
    main(i)
