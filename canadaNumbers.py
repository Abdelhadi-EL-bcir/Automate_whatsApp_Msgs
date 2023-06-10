import pywhatkit
import pyautogui
i = 28
with open('canada.txt', 'r') as file:
    for line in file:
        # Process each line
        pywhatkit.sendwhatmsg(line.strip()
                              , "Every day, discover a selection of the best job offers in the public and private sectors, including permanent (CDI) and fixed-term (CDD) positions, internship (PFE) opportunities with compensation, and pre-employment offers. We also provide Employment Coaching articles to support you in your job search or simply in your career. \noffresexclusives.blogspot.com"
                              , 00
                              , i
                            )
        i = i + 2
        print("message sended to "+line.strip())