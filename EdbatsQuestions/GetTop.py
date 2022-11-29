class Solution(object):

    def top_notes(self, di):

        for key, values in di.items():
            if key == 'notes':
                di["top_note"] = max(di["notes"])
                di.pop("notes", None)
                return di


if __name__ == '__main__':
    p = Solution()
    dt = {"name": "John", "notes": [3, 5, 4]}
    print(p.top_notes(dt))
