from typing import List


class Solution:
    def count_matches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0

        if ruleKey == 'type':
            for i in range(len(items)):
                if items[i][0] == ruleValue:
                    count += 1
            return count
        elif ruleKey == 'color':
            for i in range(len(items)):
                if items[i][1] == ruleValue:
                    count += 1
            return count
        elif ruleKey == 'name':
            for i in range(len(items)):
                if items[i][2] == ruleValue:
                    count += 1
            return count

    def count_matches2(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_dictionary = {'type': 0, 'color': 1, 'name': 2}
        rule = rule_dictionary[ruleKey]

        count = 0
        for item in items:
            if item[rule] == ruleValue:
                count += 1
        return count



s = Solution()
print(s.count_matches([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
                      "color", "silver"))
print(s.count_matches([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
                      "type", "phone"))
print(s.count_matches2([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
                      "color", "silver"))
print(s.count_matches2([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
                      "type", "phone"))
