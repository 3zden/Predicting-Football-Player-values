  '''first problem:  
       
while scraping data from fbref website is inserting data in the dataframe
players rows have different lengths (some players didnt play any match, some just sign the contrat (no data availliable = small length)), which causes issues when you tryna insert the data into a DataFrame.
 
as a solution, i searched for a informations that exist in all rows and make theme as a references
  
since theres no names with length > 4 mots  
jai traiter chaque cas manuellement pour eviter a augmenter la complexité du code
''' 
 
'''second problem 
while scraping i found that there is when you search for some teams it didnt show the right page which causes an issue while searching for data
i use exception to handle this error'''

''' THIRD PROBLEM 
IS WHEN YOU SEARCH FOR A TEAM, SOMETIMES THERS MORE THAN ONE TEAM/PLAYER WITH THE SAME NAME, THE DRIVER GET CLICK IN THE FIRST SEARCH RESULT, WHICH MOST OF THE TIME
NOT WHAT WE SEARCH, 
SO I ADD A TRY AND EXCEPT BLOCK THAT HANDLE THIS ISSUE BY SELECTING TEAM CATEGORY WHEN THIS PROBLEM OCCURS'''

''' i fucking hate web scraping, i dont know why i do  this to myself, i should just use the api, but i like to suffer'''
