# Source: https://youtu.be/3Q_oYDQ2whs
# Company: Google
# Question: 2 persons calender is given, and their working hours.
# Search thru 2 persons calender and find available hours for 2 person to have a meeting.

# Details: 1 persons ending time can be accepted such as if it ends in [10:00,11.30], meeting can start at 11.30. It is military time. Calendar is sorted.

inputPerson1 = [[["10:00","11:30"],["12:30","13:00"],["14:00","15:30"],["15:30","16:45"]],["10:00","18:00"]]
inputPerson2 = [[["9:15","10:15"],["12:15","13:30"],["14:20","16:30"],["16:45","17:15"]],["9:00","17:30"]]

#Answer:

def ReturnAvailableMeeting(inputPerson1,inputPerson2):
    calendarPerson1 = inputPerson1[0]
    calendarPerson2 = inputPerson2[0]

    shiftHourPerson1 = inputPerson1[-1]
    shiftHourPerson2 = inputPerson2[-1]

    def FindEmptySpace(calendar,shift):
        emptySpaces=[]

        if calendar[0][0] != shift[0]:
            emptySpaces.append([float(shift[0].replace(":",".")),float(calendar[0][0].replace(":","."))])

        for index,time in enumerate(calendar):
            if (index == len(calendar)-1) :
                emptySpaces.append([float(calendar[index][-1].replace(":",".")),float(shift[-1].replace(":","."))])
            else:
                emptySpaces.append([float(calendar[index][-1].replace(":",".")),float(calendar[index+1][0].replace(":","."))])

            if calendar[index][-1] == shift[-1]:
                emptySpaces.pop()      

        return emptySpaces
    
    person1Empty = FindEmptySpace(calendarPerson1,shiftHourPerson1)
    person2Empty = FindEmptySpace(calendarPerson2,shiftHourPerson2)

    def ArrangeMeeting(p1, p2):
        available = []

        for x in p1:
            start1, end1 = x
            for y in p2:
                start2, end2 = y
                if (start1 <= start2 and end1 > start2) or (start1 < end2 and end1 >= end2) or (start1 >= start2 and end1 <= end2):
                    overlap_start = max(start1, start2)
                    overlap_end = min(end1, end2)
                    available.append([overlap_start, overlap_end])

        formatted = []

        for t in available:
            starttime = str(t[0]).replace(".",":")
            endtime = str(t[-1]).replace(".",":")

            if len(starttime) == 4:
                starttime = starttime+"0"
            if len(endtime) == 4:
                endtime = endtime+"0"
            formatted.append([starttime,endtime])

        return formatted
    
    return ArrangeMeeting(person1Empty,person2Empty)

result = ReturnAvailableMeeting(inputPerson1,inputPerson2)
print(result)