"""
--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an order for more. 
They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier:
find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. 
The elves also need a little extra paper for each present: the area of the smallest side.

For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
"""

def area_needed(text):
    dimensions_list = []
    total_wrapping_paper = 0
    with open(text, 'r') as file:
        dimensions = file.readlines()
        for item in dimensions:
            item = item.strip().split(sep='x')
            dimensions_list.append(item)

    def area_calc(length, width, height):

        area1 = (2*length*width)
        area2 = (2*width*height)
        area3 = (2*height*length)
        total_area = area1 + area2 + area3
        smallest_area = min(length*width, width*height, height*length)

        return total_area + smallest_area
    
    for item in dimensions_list:
        paper_for_item = area_calc(int(item[0]),int(item[1]),int(item[2]))
        total_wrapping_paper += paper_for_item
    return total_wrapping_paper


print(area_needed("2015\day-2-input1.txt"))