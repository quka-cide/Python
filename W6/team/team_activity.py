with open("team/hr_system.txt") as hr_system:

    for line in hr_system:
        parts = line.strip().split(" ")

        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])

        paycheck = salary / 24

        if job_title == 'Engineer':
            paycheck += 1000

        print(f"{name} (ID: {id_number}), {job_title} - ${paycheck:.2f}")