"""
You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") 
and why your map looks mostly blank ("you sure ask a lot of questions") 
and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, 
they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. 
Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

demo_input1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

def main(input_text):
    parsed_values = []
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    lines = input_text.split(sep='\n')
    for line in lines:
        all_line_nums = []
        for value in line:
            if value in numbers:
                all_line_nums.append(value)
            else:
                pass
        parsed_values.append(all_line_nums)

    # each line requires two nums for coordinates
    # so if only one num, duplicate it for requirement
    for num_list in parsed_values:
        if len(num_list) == 1:
            num_list.append(num_list[0])
        else:
            pass
    
    # parsed_values before combining to ints
    # print(parsed_values)

    # now to convert first+last nums into single int
    for index in range(len(parsed_values)):
        parsed_values[index] = int(parsed_values[index][0] + parsed_values[index][-1])
    
    # parsed_values after combining to ints
    # print(parsed_values)

    return sum(parsed_values)

print(main(demo_input1)) # returns 142 as expected

with open("2023\day-1-input.txt",'r') as file:
    input_text = file.read()
    print(main(input_text=input_text))
