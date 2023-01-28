# Your code here!!
def sing():
    lyric = ""
    for x in range(0,12):
        if x==4:
            lyric += "whisper words of wisdom, "
        elif x == 10:
             lyric += "there will be an answer, "
        elif x == 11:
            lyric+= "let it be"
        else:
             lyric += "let it be, "
        

    return lyric

print(sing())