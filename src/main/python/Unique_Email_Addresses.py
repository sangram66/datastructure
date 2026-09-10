#https://leetcode.com/problems/unique-email-addresses/
'''
class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            local_name,domain_name = email.split("@")
            #print ("local_name :"+local_name)
            #print ("domain_name :"+domain_name)
            local_name ="".join(local_name.split('+')[0].split('.'))
            #print ("local_name :"+local_name)
            email = local_name +'@' + domain_name
            #print ("email :"+email)
            email_set.add(email)
        return len(email_set)
'''
class Solution:
    def numUniqueEmails(self, emails) :
        mailset = set()
        for item in emails:
            if item.find("+") != -1: 
                print ("inside if "+item[:item.find("+")].replace('.','') + '   ' +item[item.find("@"):] )
                item = item[:item.find("+")].replace('.','') + item[item.find("@"):]
            else:
                item = item[:item.find("@")].replace('.','') + item[item.find("@"):]
                print ("inside else "+item)
            mailset.add(item)
        return len(mailset)
#emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emails=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
sol=Solution()
print (sol.numUniqueEmails(emails) )