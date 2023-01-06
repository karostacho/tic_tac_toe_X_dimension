from display import annouce_the_winner

board = [["x", "x", "x"], [1, "x", "x"], ["o", "x", "o"]] 
numbers = [1,2,3,4,5,6,7,8,9]



x= sum(board, [])
print(x)

def check_if_draw(board, numbers):
    list_of_boxes = sum(board,[])
    if not any(item in numbers for item in list_of_boxes):
        print("ok")

check_if_draw(board, numbers)