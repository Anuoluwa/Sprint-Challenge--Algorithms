'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    subword = "th"
    if len(word) == 0 or (len(word) < len(subword)):
        return 0
    if word[0: len(subword)] == subword:
        return 1 + count_th(word[len(subword) - 1:])
    return count_th(word[len(subword) - 1:])

x = count_th("Think thank the throttle Thespian ")
print(x)