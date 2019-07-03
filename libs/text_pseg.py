import jieba.posseg as pseg
class Text:
  def text_part_speech(self,text):
    words = pseg.cut(text)
    li=[]
    for word, flag in words:
      print('%s %s' % (word, flag))
      li.append( flag)
    print(li)
    return li
  def text_part_pseg(self,text):
    """
    获取文本的词性标注 以文本方式标注
    """
    new= self.text_part_speech(text)
    return ','.join(new)
