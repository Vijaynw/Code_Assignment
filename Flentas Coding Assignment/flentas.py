f = open("final.log", "r")
lines = f.readlines()
add = 0
data = []
for line in lines:
    new = line.split(',')
    data.append(new)

def get_sec(time_str):
    h, m, s = time_str.split(':')

    return int(h) * 3600 + int(m) * 60 + int(s)

print("Choose any one: ")
print("1. Find the distinct From Numbers for a day.")
print("2. Find the distinct From Numbers who used the Free Plan. (Call Duration less than 1 min)")
print("3. Find the total call duration with respect to From Number")
print("4. Find the total income for a day")
print("5. Exit")

while(True):
    no = int(input())
    if no == 1:
        # 1. Find the distinct From Numbers for a day.
        output = set()
        for i in range(1, len(data)):
            output.add(data[i][0])
        print("1. Distinct From Numbers for a day \n")

        for dist_numbers in output:
            print(dist_numbers)


    elif no == 2:
        # 2. Find the distinct From Numbers who used the Free Plan. (Call Duration less than 1 min)
        output = set()
        for i in range(1, len(data)):
            if get_sec(data[i][2]) < 60:
                output.add(data[i][0])
        print("2. Distinct From Numbers who used the Free Plan. \n")
        for free_user in output:
            print(free_user)
    elif no == 3:
        # 3. Find the total call duration with respect to From Number
        output = dict()
        for i in range(1, len(data)):
            if data[i][0] in output:
                val = output[data[i][0]]
                output[data[i][0]] = val + get_sec(data[i][2])
            else:
                output[data[i][0]] = get_sec(data[i][2])

        print("From Numbers , Total Call Duration")
        for From_phones, duration in output.items():                #USE OF DICT
            print(From_phones, "    ", duration)

    elif no == 4:
        total_income = 0

        for i in range(1, len(data)):
            if get_sec(data[i][2]) > 60:
                extra_sec = get_sec(data[i][2]) - 60
                cost = (30 * extra_sec) / 60
                total_income = total_income + cost

        print("Total Income : ", total_income / 100, "rupees")
    elif no == 5:
        break
    else:
        print("Enter Correct number")
    print("Choose any one: ")
    print("1. Find the distinct From Numbers for a day.")
    print("2. Find the distinct From Numbers who used the Free Plan. (Call Duration less than 1 min)")
    print("3. Find the total call duration with respect to From Number")
    print("4. Find the total income for a day")
    print("5. Exit")
