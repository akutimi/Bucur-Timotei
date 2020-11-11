from cmmdc import calcul


if __name__=="__main__":
  assert calcul(10,0)==0
  assert calcul(10,5)==5
  assert calcul(5,7)==1
  assert calcul(12,18)==6
  assert calcul(39,26)==13
