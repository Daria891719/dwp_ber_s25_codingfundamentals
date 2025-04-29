# Homework L7: Shopping List

## WHAT YOU'RE BUILDING
"""
Create a program that:

1. Asks users to enter items for their shopping list
2. Keeps asking for items until they type 'done'
3. Shows the complete list at the end

## EXPECTED OUTPUT
```
Enter an item ('done' to finish): milk
Enter an item ('done' to finish): bread
Enter an item ('done' to finish): eggs
Enter an item ('done' to finish): done


Your shopping list:
1. milk
2. bread
3. eggs

Total items: 3

## REQUIREMENTS
### The program must:
1. Use a while loop
2. Store items in a list
3. Be case-insensitive for the word 'done' (DONE, Done, done should all work)
4. Number the items when displaying the final list
5. Show the total number of items at the end


### Input handling:
1. Ignore empty inputs (just ask again)
2. Remove extra spaces before and after items
3. Don't add 'done' to the shopping list

## TESTING YOUR PROGRAM
Test your program with these scenarios:

1. Normal items: milk, bread, eggs
2. Items with spaces: " milk  " (extra spaces)
3. Empty inputs: (just press Enter)
4. Different cases of 'done': DONE, Done, done
5. Single item then done
6. Directly typing 'done' (empty list)

## BONUS CHALLENGES (OPTIONAL)
After completing the basic requirements, try these:

1. Don't allow duplicate items
2. Sort the list alphabetically before displaying
"""
procurement_sheet=[]
while True:
    procurement=input("Write the product you need to buy (when finish, write *done*): ")
    procurement=procurement.lower()
    procurement=procurement.strip()
    if procurement != "done":
        cleaned_procurement = ""
        previous_letter_was_space = False 
        for letter in procurement:
            if letter.isalpha(): 
                cleaned_procurement += letter
                previous_letter_was_space = False 
            elif letter.isspace() and not previous_letter_was_space: #check for space between words
                cleaned_procurement += " "
                previous_letter_was_space = True
            else:
                continue
        if cleaned_procurement and cleaned_procurement not in procurement_sheet:#Finds the unique words
            procurement_sheet.append(cleaned_procurement)
    else:
        break
procurement_sheet_fin = sorted(procurement_sheet)
iter_obj=iter(procurement_sheet_fin)
print("You need to buy:")
i=1
while True:
     try: 
        good=next (iter_obj)
        print (i," ",good)
        i+=1
     except StopIteration:
        break
print ("The total quantity of goods is: ", len (procurement_sheet_fin))
"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
Write a function which takes a list of strings and returns each line prepended by the correct number.
The numbering starts at 1. The format is n: string. Notice the colon and space in between.
Examples: (Input --> Output)
[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]"""
def numeration(fancy_text):
    fancy_text_fin=[]
    for i in range(len(fancy_text)):
        text=str(i+1)+": "+ fancy_text[i]
        fancy_text_fin.append(text)
    return fancy_text_fin
fancy_text=[]
print ("You need to write a fancy word. Write end when end")
while True:
    fancy_word=input("Write a fancy word: ")
    fancy_word=fancy_word.lower().strip()
    cleaned_text = ""
    if fancy_word == "end":
        break  
    else:        
        for letter in fancy_word:
            if letter.isalpha(): 
                cleaned_text += letter
            else:
                continue
        if cleaned_text not in fancy_text:#Finds the unique words
            fancy_text.append(cleaned_text)
print("Well done! You list of words is", end=" ")
fancy_text_fin=numeration(fancy_text)
print (fancy_text_fin)