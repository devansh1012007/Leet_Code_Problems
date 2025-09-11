'''if i not in my_dict_2.keys() and should_pass == False:
                            return "f1"'''
# without using stacks
class Solution():
    
    def isValid(self, s):
        if len(s)%2 != 0:
            return False
            #return False
        my_dict ={"(" : ")",
        ")" : "(",
        "[" : "]",
        "]" : "[",
        "{" : "}",
        "}" : "{"}
        lst = []
        
        my_dict_2 = {"(" : ")",
        "[" : "]",
        "{" : "}"}

        for i in s:
            if i not in lst:
                lst.append(i)
                if s.count(i) != s.count(my_dict[i]):
                    return False
                    #return False  

        should_pass = False
        index_num_4_check = 0
        round_count = 1
        for i in s :
                index_num_4_check = index_num_4_check + 1
                #print("main for loop", index_num_4_check)
                #print(i,round_count,index_num_4_check)
                if round_count == (len(s)/2)+1:
                    return True
                if should_pass == True:
                    should_pass = False
                    pass
                else:
                    if i not in my_dict_2.keys() and should_pass == False:
                            #print(i)
                            return False
                    
                    round_count += 1
                    #index_num_4_check =+ 1
                    if my_dict[i] != s[-index_num_4_check]:
                        #print("passed from -ve index check")
                        #print(i,round_count,index_num_4_check)
                        if my_dict[i] != s[index_num_4_check]:
                            return False
                            #return False
                        else:
                            #index_num_4_check =+ 1
                            should_pass = True
                            #print("should pass")
                    
                    if s[-index_num_4_check] == s[index_num_4_check]:
                        should_pass = True
                        
    
        return True

case = Solution()
print(case.isValid("()[]}{"))

# -------------------------------------------------------------------------------------------
# using stacks
class Solution:
    def isValid(self, s):
        i=0
        a=[]
        for i in range(len(s)):
            if s[i]=='('or s[i]=='['or s[i]=='{':
                a.append(s[i])
            else:
                if not a:
                    return False
                top=a.pop()
                if s[i]==')'and top!='(':
                    return False
                if s[i]==']'and top!='[':
                    return False
                if s[i]=='}'and top!='{':
                    return False
        return len(a)==0