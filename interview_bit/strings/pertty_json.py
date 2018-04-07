__author__ = 'customfurnish'

class Solution:

    def append_string(self, a, tab_count):
        temp = ""
        for x in range(tab_count):
            temp += "\t"
        return temp+a

    def prettyJSON(self, A):
        n = len(A)
        if n < 2:
            return [A]
        tab_count = 0
        open_braces = ["{", "["]

        closed_braces = ["}",  "]"]
        result = []
        temp = ""
        x = 0
        while(x < n):
            if A[x] == "\n":
                continue
            if A[x] in open_braces:
                if len(temp) > 0:
                    result.append(self.append_string(temp, tab_count))
                result.append(self.append_string(A[x], tab_count))
                temp = ""
                tab_count += 1

            elif A[x] in closed_braces:

                if len(temp) > 0:
                    result.append(self.append_string(temp, tab_count))
                tab_count -= 1
                if x+1 < n and A[x+1] == ",":
                    result.append(self.append_string(A[x]+ ",", tab_count))
                    x += 1
                else:
                    result.append(self.append_string(A[x], tab_count))
                temp = ""

            elif A[x] == ",":
                temp +=A[x]
                result.append(self.append_string(temp, tab_count))
                temp = ""
            else:
                temp += A[x]
            x += 1
        return result
    def preetyJson2(self, A):
        ret = []
        n = len(A)
        if n == 0:
            return ret
        tab_count = 0
        open_braces = ["{", "["]

        closed_braces = ["}",  "]"]
        temp = "\t"*tab_count
        for i in range(n):
            if A[i] != ' ':
                temp += A[i]
            if A[i] in open_braces:
                if len(temp) > 2 and temp[-2] != '\t':
                    ret.append(temp[:-1])
                temp = "\t"*tab_count+temp[-1]
                ret.append(temp)
                tab_count += 1
                temp = "\t"*tab_count
            elif A[i] in closed_braces:
                tab_count -= 1
                if len(temp) > 2 and temp[-2] != '\t':
                    ret.append(temp[:-1])
                temp = "\t"*tab_count+temp[-1]
            elif A[i] == ',':
                ret.append(temp)
                temp = "\t"*tab_count
        if len(temp) > 0 and temp[-1] != '\t':
            ret.append(temp)
        return ret

S = '{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}"'












print Solution().prettyJSON(S)
print Solution().preetyJson2(S)

# {
#     "attributes":
#     [
#         {
#             "nm":"ACCOUNT",
#             "lv":
#             [
#                 {
#                     "v":
#                     {
#                         "Id":null,
#                         "State":null
#                     },
#                     "vt":"java.util.Map",
#                     "cn":1
#                 }
#             ],
#             "vt":"java.util.Map",
#             "status":"SUCCESS",
#             "lmd":13585
#         },
#         {
#             "nm":"PROFILE",
#             "lv":
#             [
#                 {
#                     "v":
#                     {
#                         "Party":null,
#                         "Ads":null
#                     },
#                     "vt":"java.util.Map",
#                     "cn":2
#                 }
#             ],
#             "vt":"java.util.Map",
#             "status":"SUCCESS",
#             "lmd":41962
#         }
#     ]
# }



# myanser

# {
#     "attributes":
#     [
#         {
#             "nm":"ACCOUNT",
#             "lv":
#             [
#                 {
#                     "v":
#                     {
#                         "Id":null,
#                         "State":null},
#                     }
#                     ,
#                     "vt":"java.util.Map",
#                     "cn":1
#                 }
#             ]
#             ,
#             "vt":"java.util.Map",
#             "status":"SUCCESS",
#             "lmd":13585
#         }
#         ,
#         {
#             "nm":"PROFILE",
#             "lv":
#             [
#                 {
#                     "v":
#                     {
#                         "Party":null,
#                         "Ads":null
#                     }
#                     ,
#                     "vt":"java.util.Map",
#                     "cn":2
#                 }
#             ]
#             ,
#             "vt":"java.util.Map",
#             "status":"SUCCESS",
#             "lmd":41962
#         }
#     ]
# }
