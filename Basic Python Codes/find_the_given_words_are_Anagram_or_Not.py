word1=str(input("Enter a First Word: "))
word2=str(input("Enter a First Word: "))
word3=word1.lower()
word4=word2.lower()
srt_word1=sorted(word3)
srt_word2=sorted(word4)
if srt_word1==srt_word2:
    print("The Word is Anagram")
else:
    print("The Word is Not Anagram")