def find_item(list, item):
  
  if len(list) == 0:
    return False
  
  
  list.sort()

    middle = len(list)//2
  if list[middle] == item:
    return True

   
  if item < list[middle]:
    return find_item(list[:middle], item)
  else:
    return find_item(list[middle+1:], item)

  return False


list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False
