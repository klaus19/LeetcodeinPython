class Solution(object):

    def alphabet(ns):
        ns = sorted(ns)
        a, b, ab = ns[0], ns[1], ns[0] * ns[1]
        ns.remove(a)
        ns.remove(b)
        ns.remove(ab)
        c, bc = ns[0], b * ns[0]
        ns.remove(c)
        ns.remove(bc)
        return ns[0]

if __name__ == "__main__":
    t = [2, 3, 4, 1, 12, 6, 2, 4]
    print(Solution().alphabet(t))