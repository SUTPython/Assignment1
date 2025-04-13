n = int(input())
ls = [int(i) for i in input().split()]

valid_way = 0

def search(ls,last_card,is_first) : 
     global valid_way
 
     if len(ls) == 0 : 
         return

     if not is_first : 
         for card_number in range(len(ls)) : 
             if ls[card_number] == last_card : 
                 valid_way += 1
             elif ls[card_number] > last_card :
                 temp_ls = ls.copy()
                 temp_ls.pop(card_number) 
                 search(temp_ls,ls[card_number],False)
     else :
         for card_number in range(len(ls)) :
             temp_ls = ls.copy()
             temp_ls.pop(card_number)
             search(temp_ls,ls[card_number],False)

search(ls,None,True)

print(valid_way)