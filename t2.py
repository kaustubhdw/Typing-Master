from time import *
import random as r


def mistake (partest, usertest):
    error = 0
    for i in range (len (partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except :
            error = error + 1
    return error
def speed_time(time_start, time_end,userinput):
    time_delay = time_end - time_start
    time_R = round(time_delay, 2)
    speed = len(userinput)/ time_R
    return round(speed)



class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(color.BLUE + "                    Choose the Lamguage for Typing Speed Test                  " + color.END)
print(color.PURPLE + "                            a -> For English                  " + color.END)
print(color.PURPLE + "                            b -> For Hindi                  " + color.END)
X = input(color.GREEN + "Enter Your choice : " + color.END)
if X == "a":
    test = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",

            "In the beginning God created the heavens and the earth. The earth was formless and void, and darkness was over the surface of the deep.",

            "Harry Potter and the Philosopher's Stone is a fantasy novel written by British author J.K. Rowling. It follows Harry Potter, a young wizard.",

            "The mitochondria are known as the powerhouse of the cell. They generate the energy that our cells need to function properly.",

            "Albert Einstein was a theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics.",

            "The Great Wall of China is a series of fortifications made of stone, brick, tamped earth, wood, and other materials, built along an east-to-west line.",

            "Shakespeare's plays have been translated into every major living language and are performed more often than those of any other playwright.",

            "The human brain is the most complex organ in the body. It controls our thoughts, emotions, movements, and bodily functions.",

            "The Mona Lisa is a half-length portrait painting by the Italian artist Leonardo da Vinci. It is considered one of the most famous paintings in the world.",

            "The Declaration of Independence, adopted on July 4, 1776, announced that the thirteen American colonies were no longer part of the British Empire.",

            "Mozart was a prolific and influential composer of the classical era. He composed over 600 works, many of which are acknowledged as pinnacles of symphonic, concertante, chamber, operatic, and choral music.",

            "The Taj Mahal is an ivory-white marble mausoleum on the right bank of the river Yamuna in the Indian city of Agra. It was commissioned in 1632 by the Mughal emperor Shah Jahan to house the tomb of his favorite wife, Mumtaz Mahal.",

            "The human body has 206 bones. These bones provide structure, protect organs, anchor muscles, and store calcium.",

            "Vincent van Gogh was a Dutch Post-Impressionist painter who is among the most famous and influential figures in the history of Western art.",

            "The periodic table is a tabular arrangement of the chemical elements, arranged by atomic number, electron configuration, and recurring chemical properties.",

            "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower.",

            "The Amazon Rainforest, often referred to as the "'Lungs of the Earth,'" produces 20% of the world's oxygen and is home to an estimated 10% of the world's species.",

            "Leonardo da Vinci was an Italian polymath of the Renaissance whose areas of interest included invention, painting, sculpting, architecture, science, music, mathematics, engineering, literature, anatomy, geology, astronomy, botany, writing, history, and cartography.",

            "The Hubble Space Telescope is a space telescope that was launched into low Earth orbit in 1990 and remains in operation. It has provided some of the most detailed images of distant galaxies, nebulae, and other celestial phenomena."]
    test1= r.choice (test)
    print()

    print(color.BLUE + "                        ***** Typing Speed Test *****                  " + color.END)
    print()
    print (test1)
    print()
    time_1 = time()
    testinput = input("Enter: ")
    time_2 = time()
    print('Speed : ', speed_time(time_1,time_2, testinput)," w/sec")
    print("Error : ", mistake (test1, testinput))


elif X == "b":
    test = [
        "सूरज ने पहली बार उसको देखा था। वह उसकी मुस्कान पर मोहित हो गया था।",
        "गंगा की धारा सुंदरता का प्रतीक है। उसका पानी शुद्धता का प्रतीक है।",
        "मेरे देश की धरती सोना उगले, उगले हीरे मोती।",
        "बारिश की बूँदें खुशियों का पेड़ बनाती हैं। वह सबको नई उम्मीद देती है।",
        "सच्चा प्यार अनमोल होता है। उसकी कीमत कोई नहीं समझ सकता।",
        "विद्या ही शिक्षा का मूल आधार है। बिना शिक्षा के कोई भी समृद्धि नहीं कर सकता।",
        "मित्रता एक अनमोल खजाना है। अच्छे दोस्त हमारे जीवन को सजीव बनाते हैं।",
        "धूप में चलना सच्चे साहस की पराकाष्ठा है। वह दिखाता है कि हम किसी भी स्थिति को परास्त कर सकते हैं।",
        "सपनों की ऊँचाई को छूने के लिए हमें मेहनत करनी पड़ती है।",
        "आत्मा की शांति के लिए ध्यान और योग अत्यंत महत्वपूर्ण हैं।",
        "समाज में समरसता और एकता की जरूरत है। हमें सभी को साथ लेकर चलना चाहिए।",
        "स्वच्छता एक अच्छे स्वास्थ्य का आधार है। हमें इसे हमेशा महत्व देना चाहिए।",
        "पर्यावरण की रक्षा हमारा कर्तव्य है। हमें प्रकृति को संरक्षित रखना चाहिए।",
        "कर्म करते रहो, फल की चिंता मत करो। फल जो होगा, वह स्वयं होगा।",
        "सभी को न्याय मिलना चाहिए। कोई भी अन्याय सहन नहीं करना चाहिए।",
        "विश्वास और आत्मविश्वास हर कार्य की कुंजी है। बिना विश्वास के कोई भी लक्ष्य साकार नहीं होता।",
        "आत्मा की शुद्धि के लिए अनिवार्य है कि हम अपने कर्मों को नेकी के साथ करें।",
        "समाज की प्रगति के लिए शिक्षा का महत्वपूर्ण योगदान है।",
        "सभी को विज्ञान और प्रौद्योगिकी में रुचि लेनी चाहिए। इससे हमारा जीवन सरल और सुखमय होगा।",
        "सपने वह तारा हैं जो हमें सही रास्ते पर ले जाते हैं। उन्हें पूरा करने के लिए हमें मेहनत करनी पड़ती है।"
    ]
    test1= r.choice (test)
    print()

    print(color.BLUE + "                        ***** Typing Speed Test *****                  " + color.END)
    print()
    print (test1)
    print()
    time_1 = time()
    testinput = input("Enter: ")
    time_2 = time()
    print('Speed : ', speed_time(time_1,time_2, testinput)," w/sec")
    print("Error : ", mistake (test1, testinput))

else:
    print(color.RED + "!Wrong Choice!                 " + color.END)
    print(color.PURPLE + "Please Enter the Correct Choice" + color.END)

from time import *
import random as r
def mistake (partest, usertest):
    error = 0
    for i in range (len (partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except :
            error = error + 1
    return error
def speed_time(time_start, time_end,userinput):
    time_delay = time_end - time_start
    time_R = round(time_delay, 2)
    speed = len(userinput)/ time_R
    return round(speed)



class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(color.BLUE + "                    Choose the Lamguage for Typing Speed Test                  " + color.END)
print(color.PURPLE + "                            a -> For English                  " + color.END)
print(color.PURPLE + "                            b -> For Hindi                  " + color.END)
X = input(color.GREEN + "Enter Your choice : " + color.END)
if X == "a":
    test = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",

            "In the beginning God created the heavens and the earth. The earth was formless and void, and darkness was over the surface of the deep.",

            "Harry Potter and the Philosopher's Stone is a fantasy novel written by British author J.K. Rowling. It follows Harry Potter, a young wizard.",

            "The mitochondria are known as the powerhouse of the cell. They generate the energy that our cells need to function properly.",

            "Albert Einstein was a theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics.",

            "The Great Wall of China is a series of fortifications made of stone, brick, tamped earth, wood, and other materials, built along an east-to-west line.",

            "Shakespeare's plays have been translated into every major living language and are performed more often than those of any other playwright.",

            "The human brain is the most complex organ in the body. It controls our thoughts, emotions, movements, and bodily functions.",

            "The Mona Lisa is a half-length portrait painting by the Italian artist Leonardo da Vinci. It is considered one of the most famous paintings in the world.",

            "The Declaration of Independence, adopted on July 4, 1776, announced that the thirteen American colonies were no longer part of the British Empire.",

            "Mozart was a prolific and influential composer of the classical era. He composed over 600 works, many of which are acknowledged as pinnacles of symphonic, concertante, chamber, operatic, and choral music.",

            "The Taj Mahal is an ivory-white marble mausoleum on the right bank of the river Yamuna in the Indian city of Agra. It was commissioned in 1632 by the Mughal emperor Shah Jahan to house the tomb of his favorite wife, Mumtaz Mahal.",

            "The human body has 206 bones. These bones provide structure, protect organs, anchor muscles, and store calcium.",

            "Vincent van Gogh was a Dutch Post-Impressionist painter who is among the most famous and influential figures in the history of Western art.",

            "The periodic table is a tabular arrangement of the chemical elements, arranged by atomic number, electron configuration, and recurring chemical properties.",

            "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower.",

            "The Amazon Rainforest, often referred to as the "'Lungs of the Earth,'" produces 20% of the world's oxygen and is home to an estimated 10% of the world's species.",

            "Leonardo da Vinci was an Italian polymath of the Renaissance whose areas of interest included invention, painting, sculpting, architecture, science, music, mathematics, engineering, literature, anatomy, geology, astronomy, botany, writing, history, and cartography.",

            "The Hubble Space Telescope is a space telescope that was launched into low Earth orbit in 1990 and remains in operation. It has provided some of the most detailed images of distant galaxies, nebulae, and other celestial phenomena."]
    test1= r.choice (test)
    print()

    print(color.BLUE + "                        ***** Typing Speed Test *****                  " + color.END)
    print()
    print (test1)
    print()
    time_1 = time()
    testinput = input("Enter: ")
    time_2 = time()
    print('Speed : ', speed_time(time_1,time_2, testinput)," w/sec")
    print("Error : ", mistake (test1, testinput))


elif X == "b":
    test = [
        "सूरज ने पहली बार उसको देखा था। वह उसकी मुस्कान पर मोहित हो गया था।",
        "गंगा की धारा सुंदरता का प्रतीक है। उसका पानी शुद्धता का प्रतीक है।",
        "मेरे देश की धरती सोना उगले, उगले हीरे मोती।",
        "बारिश की बूँदें खुशियों का पेड़ बनाती हैं। वह सबको नई उम्मीद देती है।",
        "सच्चा प्यार अनमोल होता है। उसकी कीमत कोई नहीं समझ सकता।",
        "विद्या ही शिक्षा का मूल आधार है। बिना शिक्षा के कोई भी समृद्धि नहीं कर सकता।",
        "मित्रता एक अनमोल खजाना है। अच्छे दोस्त हमारे जीवन को सजीव बनाते हैं।",
        "धूप में चलना सच्चे साहस की पराकाष्ठा है। वह दिखाता है कि हम किसी भी स्थिति को परास्त कर सकते हैं।",
        "सपनों की ऊँचाई को छूने के लिए हमें मेहनत करनी पड़ती है।",
        "आत्मा की शांति के लिए ध्यान और योग अत्यंत महत्वपूर्ण हैं।",
        "समाज में समरसता और एकता की जरूरत है। हमें सभी को साथ लेकर चलना चाहिए।",
        "स्वच्छता एक अच्छे स्वास्थ्य का आधार है। हमें इसे हमेशा महत्व देना चाहिए।",
        "पर्यावरण की रक्षा हमारा कर्तव्य है। हमें प्रकृति को संरक्षित रखना चाहिए।",
        "कर्म करते रहो, फल की चिंता मत करो। फल जो होगा, वह स्वयं होगा।",
        "सभी को न्याय मिलना चाहिए। कोई भी अन्याय सहन नहीं करना चाहिए।",
        "विश्वास और आत्मविश्वास हर कार्य की कुंजी है। बिना विश्वास के कोई भी लक्ष्य साकार नहीं होता।",
        "आत्मा की शुद्धि के लिए अनिवार्य है कि हम अपने कर्मों को नेकी के साथ करें।",
        "समाज की प्रगति के लिए शिक्षा का महत्वपूर्ण योगदान है।",
        "सभी को विज्ञान और प्रौद्योगिकी में रुचि लेनी चाहिए। इससे हमारा जीवन सरल और सुखमय होगा।",
        "सपने वह तारा हैं जो हमें सही रास्ते पर ले जाते हैं। उन्हें पूरा करने के लिए हमें मेहनत करनी पड़ती है।"
    ]
    test1= r.choice (test)
    print()

    print(color.BLUE + "                        ***** Typing Speed Test *****                  " + color.END)
    print()
    print (test1)
    print()
    time_1 = time()
    testinput = input("Enter: ")
    time_2 = time()
    print('Speed : ', speed_time(time_1,time_2, testinput)," w/sec")
    print("Error : ", mistake (test1, testinput))

else:
    print(color.RED + "!Wrong Choice!                 " + color.END)
    print(color.PURPLE + "Please Enter the Correct Choice" + color.END)

from time import *
import random as r
def mistake (partest, usertest):
    error = 0
    for i in range (len (partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except :
            error = error + 1
    return error
def speed_time(time_start, time_end,userinput):
    time_delay = time_end - time_start
    time_R = round(time_delay, 2)
    speed = len(userinput)/ time_R
    return round(speed)



class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print(color.BLUE + "                    Choose the Lamguage for Typing Speed Test                  " + color.END)
print(color.PURPLE + "                            a -> For English                  " + color.END)
print(color.PURPLE + "                            b -> For Hindi                  " + color.END)
X = input(color.GREEN + "Enter Your choice : " + color.END)
if X == "a":
    test = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",

            "In the beginning God created the heavens and the earth. The earth was formless and void, and darkness was over the surface of the deep.",

            "Harry Potter and the Philosopher's Stone is a fantasy novel written by British author J.K. Rowling. It follows Harry Potter, a young wizard.",

            "The mitochondria are known as the powerhouse of the cell. They generate the energy that our cells need to function properly.",

            "Albert Einstein was a theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics.",

            "The Great Wall of China is a series of fortifications made of stone, brick, tamped earth, wood, and other materials, built along an east-to-west line.",

            "Shakespeare's plays have been translated into every major living language and are performed more often than those of any other playwright.",

            "The human brain is the most complex organ in the body. It controls our thoughts, emotions, movements, and bodily functions.",

            "The Mona Lisa is a half-length portrait painting by the Italian artist Leonardo da Vinci. It is considered one of the most famous paintings in the world.",

            "The Declaration of Independence, adopted on July 4, 1776, announced that the thirteen American colonies were no longer part of the British Empire.",

            "Mozart was a prolific and influential composer of the classical era. He composed over 600 works, many of which are acknowledged as pinnacles of symphonic, concertante, chamber, operatic, and choral music.",

            "The Taj Mahal is an ivory-white marble mausoleum on the right bank of the river Yamuna in the Indian city of Agra. It was commissioned in 1632 by the Mughal emperor Shah Jahan to house the tomb of his favorite wife, Mumtaz Mahal.",

            "The human body has 206 bones. These bones provide structure, protect organs, anchor muscles, and store calcium.",

            "Vincent van Gogh was a Dutch Post-Impressionist painter who is among the most famous and influential figures in the history of Western art.",

            "The periodic table is a tabular arrangement of the chemical elements, arranged by atomic number, electron configuration, and recurring chemical properties.",

            "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower.",

            "The Amazon Rainforest, often referred to as the "'Lungs of the Earth,'" produces 20% of the world's oxygen and is home to an estimated 10% of the world's species.",

            "Leonardo da Vinci was an Italian polymath of the Renaissance whose areas of interest included invention, painting, sculpting, architecture, science, music, mathematics, engineering, literature, anatomy, geology, astronomy, botany, writing, history, and cartography.",

            "The Hubble Space Telescope is a space telescope that was launched into low Earth orbit in 1990 and remains in operation. It has provided some of the most detailed images of distant galaxies, nebulae, and other celestial phenomena."]
    test1= r.choice (test)
    print()

    print(color.BLUE + "                        ***** Typing Speed Test *****                  " + color.END)
    print()
    print (test1)
    print()
    time_1 = time()
    testinput = input("Enter: ")
    time_2 = time()
    print('Speed : ', speed_time(time_1,time_2, testinput)," w/sec")
    print("Error : ", mistake (test1, testinput))


elif X == "b":
    test = [
        "सूरज ने पहली बार उसको देखा था। वह उसकी मुस्कान पर मोहित हो गया था।",
        "गंगा की धारा सुंदरता का प्रतीक है। उसका पानी शुद्धता का प्रतीक है।",
        "मेरे देश की धरती सोना उगले, उगले हीरे मोती।",
        "बारिश की बूँदें खुशियों का पेड़ बनाती हैं। वह सबको नई उम्मीद देती है।",
        "सच्चा प्यार अनमोल होता है। उसकी कीमत कोई नहीं समझ सकता।",
        "विद्या ही शिक्षा का मूल आधार है। बिना शिक्षा के कोई भी समृद्धि नहीं कर सकता।",
        "मित्रता एक अनमोल खजाना है। अच्छे दोस्त हमारे जीवन को सजीव बनाते हैं।",
        "धूप में चलना सच्चे साहस की पराकाष्ठा है। वह दिखाता है कि हम किसी भी स्थिति को परास्त कर सकते हैं।",
        "सपनों की ऊँचाई को छूने के लिए हमें मेहनत करनी पड़ती है।",
        "आत्मा की शांति के लिए ध्यान और योग अत्यंत महत्वपूर्ण हैं।",
        "समाज में समरसता और एकता की जरूरत है। हमें सभी को साथ लेकर चलना चाहिए।",
        "स्वच्छता एक अच्छे स्वास्थ्य का आधार है। हमें इसे हमेशा महत्व देना चाहिए।",
        "पर्यावरण की रक्षा हमारा कर्तव्य है। हमें प्रकृति को संरक्षित रखना चाहिए।",
        "कर्म करते रहो, फल की चिंता मत करो। फल जो होगा, वह स्वयं होगा।",
        "सभी को न्याय मिलना चाहिए। कोई भी अन्याय सहन नहीं करना चाहिए।",
        "विश्वास और आत्मविश्वास हर कार्य की कुंजी है। बिना विश्वास के कोई भी लक्ष्य साकार नहीं होता।",
        "आत्मा की शुद्धि के लिए अनिवार्य है कि हम अपने कर्मों को नेकी के साथ करें।",
        "समाज की प्रगति के लिए शिक्षा का महत्वपूर्ण योगदान है।",
        "सभी को विज्ञान और प्रौद्योगिकी में रुचि लेनी चाहिए। इससे हमारा जीवन सरल और सुखमय होगा।",
        "सपने वह तारा हैं जो हमें सही रास्ते पर ले जाते हैं। उन्हें पूरा करने के लिए हमें मेहनत करनी पड़ती है।"
    ]
    test1= r.choice (test)
    print()

    print(color.BLUE + "                        ***** Typing Speed Test *****                  " + color.END)
    print()
    print (test1)
    print()
    time_1 = time()
    testinput = input("Enter: ")
    time_2 = time()
    print('Speed : ', speed_time(time_1,time_2, testinput)," w/sec")
    print("Error : ", mistake (test1, testinput))

else:
    print(color.RED + "!Wrong Choice!                 " + color.END)
    print(color.PURPLE + "Please Enter the Correct Choice" + color.END)
