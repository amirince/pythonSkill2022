#User class can store a user's personal information such as name, age, medication,....
class user:
def __init__(self, username):
    self.username = username

#This function will generate corpus_list_titles, corpus_list, corpus_dict
def Generate_Corpus():
  ################################################################################
  #                                     Corpi                                    #
  ################################################################################
    '''
      yesList1 = ["I", "do", "with", "difficulty","yes","hard", "By", "myself","own"]
      yesList2 = ["yes","I","do","me","myself","alone", "by", "myself", "without", "can"]
      yesList3 = ["yes","do","with", "help","and","helps", "my", "somebody", "someone", "son", "daughter"]
      noList4 = ["no","somebody","does", "for", "me", "my","son","daughter","friend", "husband"]
      noList5 = ["never", "hard", "for", "me", "no", "did"]
      noList6 = ["next","other", "no", "easy", "don't", "do", "not","never", "myself", "without"]
    '''
    corpus_list_titles = ["yesList1", "yesList2", "yesList3", "noList4", "noList5", "noList6"]
    
    corpus_list = [["I", "do", "with", "difficulty","yes","hard", "By", "myself","own"],
                 ["yes","I","do","me","myself","alone", "by", "myself", "without", "can"],
                 ["yes","do","with", "help","and","helps", "my", "somebody", "someone", "son", "daughter"], 
                 ["no","somebody","does", "for", "me", "my","son","daughter","friend", "husband"],
                 ["never", "hard", "for", "me", "no", "did"],
                 ["next","other", "no", "easy", "don't", "do", "not","never", "myself", "without"]]\
                 
    corpus_dict = {
        "yesList1":0,
        "yesList2":0,
        "yesList3":0,
        "noList4":0,
        "noList5":0,
        "noList6":0
    }

return corpus_list_titles, corpus_list, corpus_dict

#Semantic Search Function takes a querystring as a parameter and returns the most appropriate corpus entry
def Semantic_Search(corpus_list_titles, corpus_list, corpus_dict, query_string):
    ################################################################################
    #                                  Parse Query                                 #
    ################################################################################
    result_category_list = []
      
    query_list = query_string.split(" ")
    #print(query_list)
      
    for word in query_list:
        for c_index in range(len(corpus_list)):
            if word in corpus_list[c_index]:
            corpus_dict[corpus_list_titles[c_index]] += 1
      #print(corpus_dict)
    
      ################################################################################
      #                             Identify Max Value(s)                            #
      ################################################################################
    
    max_value = max(corpus_dict.values()) #maximum value in corpus_dict
    
    #Creating a list of the entries that have the max value
    for entry in corpus_list_titles:
        if corpus_dict[entry] == max_value:
            result_category_list.append(entry)
    
    if len(result_category_list) > 1:
        print("Ask clarifying questions.")
    else:
        return result_category_list[0], max_value
      
    
    #if there is more than one entry with max_value:
        #generate new corpus_list titles, corpus_list, corpus dict with entries of max value
        #ask the user an appropriate follow-up question
        #call the Semantic_Search function with new corpus_list_titles, corpus_list, corpus_dict, query_string
    
    #return category, score
user1 = user("Tom")
corpus_list_titles, corpus_list, corpus_dict = Generate_Corpus()
query_string = "I can do it by myself"
result = Semantic_Search(corpus_list_titles, corpus_list, corpus_dict, query_string)
print(result)

#Danielle McIntosh 
#danielle.mcintosh@bison.howard.edu


