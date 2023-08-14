class Solution(object):

      #speed = distance//time

    def minSpeedOnTime(self, dist, hour):

        def calculateTime(speed):
            time=0
            for i in range(len(dist)-1):
                time +=(dist[i]+speed-1) //speed
            time += dist[-1] /speed
            return time

        left,right = 1,10**7

        while left <=right:
            mid = left + (right -left)//2
            time = calculateTime(mid)

            if time<=hour:
                right = mid-1

            else:
                left = mid+1
        return left if left <= 10 ** 7 else -1
