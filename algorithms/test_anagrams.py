from anagrams import group_anagrams
def test_anagrams():
    groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert groups == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert group_anagrams([]) == []
test_anagrams()
