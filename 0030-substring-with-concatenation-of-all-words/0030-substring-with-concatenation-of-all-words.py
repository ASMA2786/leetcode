
class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words

        word_count = {}

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        res = []

        for i in range(word_len):
            left = i
            seen = {}
            count = 0

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]

                if word in word_count:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == total_words:
                        res.append(left)

                else:
                    seen = {}
                    count = 0
                    left = j + word_len

        return res
