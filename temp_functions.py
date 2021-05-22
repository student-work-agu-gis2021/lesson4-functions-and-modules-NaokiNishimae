def fahr_to_celsius(temp_fahrenheit):
 


  converted_temp=(temp_fahrenheit-32)/1.8
  return converted_temp


  def temp_classifier(temp_celsius):
  """
  accepts a tempreture value in Celsius that will be reclassified into integer numbers 0,1,2,3 based on following criteria
  parameter:temp_celsius
  return:Classiffied number(0,1,2,3)

  """


  if temp_celsius<-2:
    return 0
  elif temp_celsius<2:
    return 1
  elif temp_celsius<15:
    return 2
  elif temp_celsius>=15:
    return 3