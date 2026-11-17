class Solution:
    def isValid(self, s: str) -> bool:
        open_to_closed = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        open_para = []
        closed_para = []

        for para in s:
            if para in open_to_closed.keys():
                open_para.append(para)
            if para in open_to_closed.values():
                closed_para.append(para)
            if len(closed_para) > len(open_para):
                return False
        
        if len(open_para) != len(closed_para):
            return False
        
        for i in range(len(open_para)):
            curr_o_para = open_para.pop()
            print(curr_o_para)
            curr_c_para = closed_para[i]
            print(curr_c_para)
            if open_to_closed.get(curr_o_para) == curr_c_para:
                print(open_to_closed.get(curr_o_para))
                continue
            else:
                return False
        return True
        
            
    




        