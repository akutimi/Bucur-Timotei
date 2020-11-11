from cmmdc import calculeaza


if __name__=="__main__":
  assert calculeaza(10,0)==0
  assert calculeaza(10,5)==5
  assert calculeaza(5,7)==1
  assert calculeaza(12,18)==6
  assert calculeaza(39,26)==13
