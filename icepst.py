def winkel2time(drehzahl, kurbelwinkel):
  t_inj = kurbelwinkel/(drehzahl*360/(6*10**7))
  print('----------------------------------------')
  print('t_inj: ' + str("{:.1f}".format(t_inj)) + ' µs')
  print('----------------------------------------')
  
  
def kmh2mph(kmh):
  print(kmh/1,609)
