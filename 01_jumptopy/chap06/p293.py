dic= {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G',
      '....':'H','..':'I','.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N',
      '---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U',
      '...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}


def mos(sec):
    result=[]
    for word in sec.split("  "):
        for ch in word.split(" "):
            result.append(dic[ch])
        result.append(" ")
    return ''.join(result)

print(mos('. .. .-  .... .. -.'))