#Made by Aaron Peter D'cunha
#Challenge 1 from code.golf
#Print the lyrics to the song The 12 Days of Christmas

#My idea is to use lists and accordingly choose the lyrics based on the step
day = ["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth","Ninth","Tenth","Eleventh","Twelfth"] #Idk y i felt my spellings were wrong.

# I never noticed the lyrics of the song.. All I knew was the tune.. and now I see a pattern in the song.

gift =['Two Turtle Doves', 'Three French Hens', 'Four Calling Birds', 'Five Gold Rings', 'Six Geese-a-Laying', 'Seven Swans-a-Swimming', 'Eight Maids-a-Milking', 'Nine Ladies Dancing', 'Ten Lords-a-Leaping', 'Eleven Pipers Piping', 'Twelve Drummers Drumming']

#The Loop
for i in range(12):
  print("On the {} day of Christmas".format(day[i])) #Prints the initial line
  print("My true love sent to me")
  for k in range(i,0,-1):
    print(gift[k-1] + ", " + ("and"*(1//k)) ) #Instead of checking when its the end of the lop, might as well use some simple math to multiply the string with a number to print it the amount of times i need.

  print("A Partridge in a Pear Tree.")
  print()