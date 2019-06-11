def num_classrooms_nlogn(time_intervals):
    starts_and_ends = []
    for start, end in time_intervals:
        starts_and_ends.append((start, "start"))
        starts_and_ends.append((end, "end"))

    starts_and_ends = sorted(starts_and_ends, key = lambda x: x[0])
    max_count = 0
    current = 0
    for time, typ in starts_and_ends:
        if typ == "start":
            current += 1
        elif typ == "end":
            current -= 1

        if current > max_count:
            max_count = current

    return max_count


######################################################
#               nlogn solution above                 #
#             Original solution below                #
######################################################

def num_classrooms_needed(time_intervals):
    classrooms = get_classrooms(time_intervals)
    return len(classrooms)

def get_classrooms(time_intervals):
    classrooms = []
    seen = {}
    while time_intervals:
        classroom = fill_classroom(time_intervals)
        classrooms.append(classroom)

        remaining_intervals = []
        for time in time_intervals:
            if time not in classroom:
                remaining_intervals.append(time)

        time_intervals = remaining_intervals

    return classrooms


def fill_classroom(time_intervals):
    classroom = []
    time_intervals = sorted(time_intervals, key= lambda x: x[1])
    while time_intervals:
        current = time_intervals.pop(0)
        classroom.append(current)

        time_intervals = [x for x in time_intervals if not overlaps(current, x)]

    return classroom


def overlaps(interval1, interval2):
    if interval1[0] <= interval2[1] and interval2[0] <= interval1[1]:
        return True
    return False
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

if __name__ == "__main__":
    time_intervals = [(30, 75), (0, 50), (60, 150)]
    print(num_classrooms_needed(time_intervals))
    print(num_classrooms_nlogn(time_intervals))