"""
Given a string - return the length of the longest substring that has even vowels count
Note: all vowels should have even count.
"""
from collections import Counter

# Method #1: This is the O(n^2) solution ; and has to be improved by SLIDING WINDOW
def longest_substring_even_vowels_count(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_length = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            # This is the sub-string
            substr = s[i:j]
            # Filter vowels from the sub-string
            intr = ''.join(c for c in substr if c in vowels)
            # if there are vowels - count them
            ctr = Counter(intr) if intr else {'a': 0, 'e': 0, 'i': 0, 'u': 0, 'o': 0}
            # Check if vowels have even count
            vals = list(ctr.values())
            if all(v % 2 == 0 for v in vals):
                max_length = max(max_length, len(substr))
    return max_length

string = "leetcodeisgreat"
# Test Case - that will take too long for naive test case
string2 = "tyrwpvlifrgjghlcicyocusukhmjbkfkzsjhkdrtsztchhazhmcircxcauajyzlppedqyzkcqvffyeekjdwqtjegerxbyktzvrxwgfjnrfbwvhiycvoznriroroamkfipazunsabwlseseeiimsmftchpafqkquovuxhhkpvphwnkrtxuiuhbcyqulfqyzgjjwjrlfwwxotcdtqsmfeingsxyzbpvmwulmqfrxbqcziudixceytvvwcohmznmfkoetpgdntrndvjihmxragqosaauthigfjergijsyivozzfrlpndygsmgjzdzadsxarjvyxuecqlszjnqvlyqkadowoljrmkzxvspdummgraiutxxxqgotqnxwjwfotvqglqavmsnmktsxwxcpxhuujuanxueuymzifycytalizwnvrjeoipfoqbiqdxsnclcvoafqwfwcmuwitjgqghkiccwqvloqrxbfjuxwriltxhmrmfpzitkwhitwhvatmknyhzigcuxfsosxetioqfeyewoljymhdwgwvjcdhmkpdfbbztaygvbpwqxtokvidtwfdhmhpomyfhhjorsmgowikpsdgcbazapkmsjgmfyuezaamevrbsmiecoujabrbqebiydncgapuexivgvomkuiiuuhhbszsflntwruqblrnrgwrnvcwixtxycifdebgnbbucqpqldkberbovemywoaxqicizkcjbmbxikxeizmzdvjdnhqrgkkqzmspdeuoqrxswqrajxfglmqkdnlescbjzurknjklikxxqqaqdekxkzkscoipolxmcszbebqpsizhwsxklzulmjotkrqfaeivhsedfynxtbzdrviwdgicusqucczgufqnaslpwzjhgtphnovlrgz"
output = longest_substring_even_vowels_count(string2)
print("The length is:", output)