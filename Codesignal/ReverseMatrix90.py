class Solution(object):

    def rotateImage(self,image):

        image.reverse()
        for i in range(len(image)):
            for j in range(i):
                image[i][j], image[j][i] = image[j][i], image[i][j]
        return image

if __name__ == '__main__':

    arr = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().rotateImage(arr))