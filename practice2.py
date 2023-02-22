def doneit():
    while True:
        value=int(input("Enter Your Position : "))
        if value in done:
            print("This Place is already full...please select another one.")
            continue
        else:
            done.append(value)
            break
    return value
done=[0]
print(doneit())
