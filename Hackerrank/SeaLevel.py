class Solution(object):

    def seaLevel(self,steps,path):

        sea_level =0
        count =0

        for step in path:
            if step == "D":
                sea_level-=1
            elif step == "U":
                sea_level+=1

            if step == "U" and sea_level == 0:
                count+=1
        return count

if __name__ == "__main__":
    path = []