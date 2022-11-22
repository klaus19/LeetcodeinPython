class Solution(object):
    def Family(self):
       dict= {
            "Darth Vader": "father",
            "Leia": "sister",
            "Han": "brother in law",
            "R2D2": "droid"
        }

    for key,value in dict.items():
        print(key,"Luke, I am your"+value)

