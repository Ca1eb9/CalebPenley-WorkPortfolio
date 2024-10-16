# -*- coding: utf-8 -*-
"""Caleb Penley A7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pYDSSIYZpY8OcXdBe7_7yoWnDSvtwLcp
"""

def test_file_setup(file_name, lst):
  f = open(file_name, "w")
  f.close()

  if len(lst) == 0:
    print("list is empty")
    return
  f = open(file_name, "w")
  for item in lst:
    f.write(item + '\n')
  f.close()


def file_to_list(file_name):
  f = open(file_name, "r")
  file_lines = f.readlines()
  f.close()

  return [line.replace('\n', '') for line in file_lines]


def list_to_file(inputs, new_file_name):
  f = open(new_file_name, "w")
  f.close()

  for i in range(len(inputs)):
    f = open(new_file_name, "w")
    for item in inputs:
      f.write(item + '\n')
    f.close()



#1:
def file_reverse(file_name):
  init_list = file_to_list(file_name)

  outputs = []
  for i in range(len(init_list)):
    outputs += [0]
  for i in range(len(init_list)):
    outputs[len(init_list)-i-1] = init_list[i]

  list_to_file(outputs, "ans1.txt")

#2:
def longest_word(file_name):
  init_list = file_to_list(file_name)

  for i in range(len(init_list)):
    largest = None

    if len(init_list[i]) > len(init_list[i-1]):
      largest = init_list[i]
    else:
      largest = init_list[i-1]

    return largest

#3:
def file_word_replace(file_name, wrong_word, correct_word):
  init_list = file_to_list(file_name)

  new_list = []
  for i in range(len(init_list)):
    new_list += [init_list[i]]
  for i in range(len(new_list)):
    if new_list[i] == wrong_word:
      new_list[i] = correct_word

  list_to_file(new_list, "ans3.txt")



def main():
  ### Test:

  #Setup:
  test_file_setup("testing_file.txt", ["apple", "banana", "carrot", "watermelon"])

  #1:
  file_reverse("testing_file.txt")

  #2:
  ans2 = longest_word("testing_file.txt")
  print(ans2)
  print("\n")

  #3:
  file_word_replace("testing_file.txt", "banana", "oranges")

if __name__ == '__main__':
    main()