from typing import List
from day1_input_parser import parse_input

frequency = {}

def main():
    left_list, right_list = parse_input("day1_input.txt")
    calc_frequency(right_list)
    
    print(calc_similarity_score(left_list))

def calc_similarity_score(list: List[int]) -> int:
    sum = 0
    for v in list:
        sum += v * frequency.get(v, 0)
        
    return sum
        
def calc_frequency(list: List[int]) -> None:
    for v in list:
        num = frequency.get(v, 0)
        frequency[v] = num + 1

if __name__ == "__main__":
    main()        