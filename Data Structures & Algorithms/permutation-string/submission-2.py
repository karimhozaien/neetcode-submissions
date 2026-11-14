class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}
        def map_maker(table,mapp):
            for letter in range(len(table)):
                if table[letter] not in mapp.keys():
                    mapp[table[letter]] = 1
                else:
                    print(2)
                    mapp[table[letter]] += 1
        
        map_maker(s1,map1)
        print(map1.keys())
        
        for letter in range(len(s2)):
            if s2[letter] in s1:
                position = len(s1) + letter
                if position <= len(s2):
                    word = s2[letter:position]
                    map2 = {}
                    map_maker(word,map2)
                    print(map2)
                    if map1 == map2:
                        return True
        return False

        