#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Facebook Data Breach.")



#Introduces breach

print("Would you like to learn about the Facebook Data Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, or (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Locations, phone numbers, full names, email addresses, and other details were lifted in a Facebook breach that affected 533 million people in 106 different countries. The hacker exploited a feature that allowed users to use phone numbers to find each other.")
  
  elif topic.lower() == "b":
    print("Facebook informed it’s users they have no plan to notify the over half a billion victims of their data being leaked. They said it was an issue users themselves could not fix. Sites like HaveIBeenPwnd, created by Troy Hunt, could be used to help individuals determine if their data was leaked.")
  
  elif topic.lower() == "c":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no' \n")


  

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, or (c) my advice, or (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("This data breach relates to integrity because Facebook lost the people’s trust that their data would not be tampered with when this hack occurred.")
  
  elif topic.lower() == "b":
    print("I disagree with the organization's response because I believe that users should have been informed in an organized manner that their data was leaked. This is important because this data could be used in scams like phishing scams. This awareness would have helped people be more conscious with their activities instead of falling victim because of Facebook;s mistake.")
  
  elif topic.lower() == "c":
     print("I would convince victims to take action by informing them of how their data could create vulnerabilities through hackers’ use of social engineering. A simple link or request from a trusted friend could cause them to lose access to their bank accounts and emails. Hackers get access into one account and pretend to be that person to trick the victim’s friends to fall for their hack too. Then they repeat this method over and over again. The data stolen from this Facebook hack could be used by a malicious person to make a list of their potential victims.\n\n My advice would be to change all your current passwords, monitor your bank accounts, not click links without running them through a phishing checker, and not send any code sent to you to anyone! Also, always trust your gut instinct!")


  elif topic.lower() == "d":
     break


  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

  
#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")