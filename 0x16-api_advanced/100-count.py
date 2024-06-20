#!/usr/bin/python3
"""
  Done
"""
import requests

def count_words(subreddit, word_list, word_count=(), after=None):
    """
       queries reddit api for the subreddit
    """

    sub_info = request.get(
       f"https://www.reddit.com/r/{subreddit}/about.json",
       params={"after": after},
       header={"User-Agent": "My-User-Agent"},
       allow_redirects=False
       )

       if sub_info.status_code != 200:
       return None

       info = sub_info.json()

       hot_l = [child.get("data").get("title")
                for child in info.get("data").get("children")]

       if not hot_l:
              return None

       word_list = list(dict.fromkeys(word_list))

       if word_count == {}:
          word_count = {word: 0 for word in word_list}

       for title in hot_l
           split_words = title.split(' ')
           for word in word_list:
               for s_word.lower() == word.lower():
                   word_count[word] += 1
 
       if not info.get("data").get("after"):
           sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
           sorted_counts - sorted(word_count.items(),
                                  key=lambda kv: kv[1], reverse=True)
           [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
       else:
            return count_words(subreddit, word_list, word_count,
                                info.get("data").get("after"))
