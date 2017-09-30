import os
import glob
from bs4 import BeautifulSoup
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import operator
from nltk.stem import PorterStemmer

ps = PorterStemmer()

Computing_unigrams = ["health", "computational", "human", "computer", "interaction", "informatics", "cyber", "security",
                      "game", "design",
                      "web", "development", "search", "machine", "learning", "technology", "digital", "graphic", "game",
                      "language", "software", "coding", "programming", "cryptography", "data", "science", "mining",
                      "computing", "artificial", "intelligence", "database"]

x = set(Computing_unigrams)
print("len of computing dict is: ", len(x))
print (x)

Computing_unigrams_Dict = dict((term, 0) for term in Computing_unigrams)
# print (Computing_unigrams_Dict)

Computing_bigrams = ["data science", "health information", "health informatics", "bioinformatics", "machine learning",
                     "natural language", "language processing", "information management", "information retrieval",
                     "human computer", "computer interaction", "information security",
                     "information privacy", "information technology", "information policy", "web development",
                     "cyber security", "computational social",
                     "computational science", "game design", "game development"]
Computing_bigrams_Dict = dict((term, 0) for term in Computing_bigrams)

Library_unigrams = ["library", "archive", "privacy", "information", "privacy", "policy", "security", "digital",
                    "curation", "collections", "cataloging", "society", "media", "management", "art", "law",
                    "records", "public", "librarianship", "resources", "digitization", "preservation", "knowledge",
                    "services", "administration", "communities", "communication", "organization", "collections",
                    "culture", "behavior", "museums"]



y = set(Library_unigrams)
print("len of library dict is: ", len(y))
print (y)

Library_unigrams_dict = dict((t1, 0) for t1 in Library_unigrams)

Library_bigrams = ["collection management", "information services", "information organization", "digital curation",
                   "digital preservation", "digital information", "Information Quality", "Digital Cultures",
                   "Information Age", "Digital World",
                   ""]  # ############# Fill this after consulting library professors

All_tags = []
All_text = ""
Compute_score = []
Library_score = []
for file in glob.glob("HTML_pages/*.html"):
    # print (file)
    file1 = open(file, 'r', encoding="ISO-8859-1")
    soup1 = BeautifulSoup(file1, "html.parser")
    All_tags = []
    for tag in soup1.find_all():
        All_tags.append(tag.name)
    # print (set(All_tags))

    text1 = soup1.find_all("td")
    for i in text1:
        All_text = All_text + (
        i.text.strip()) + " "  # #### In version2, we will calculate normalized values of count of these classes
        # because the amount of text on different univ pages are not the same.
    text2 = soup1.find_all("p")
    for i in text2:
        All_text = All_text + (i.text.strip()) + " "

All_text_list = All_text.split()

Computing_count = 0
Library_count = 0
for i in All_text_list:
    if str(i).lower() in Computing_unigrams:
        Computing_unigrams_Dict[str(i).lower()] += 1
        Computing_count += 1
    if str(i).lower() in Library_unigrams:
        Library_unigrams_dict[str(i).lower()] += 1
        Library_count += 1
print("total computing count is: ",Computing_count)
print("total library count is: ", Library_count)


################################## Farig's codes

# dictw = {'Health': 54, 'Computational': 8, 'Human': 34, 'Computer': 69, 'Interaction': 35, 'Informatics': 84, 'cyber': 7, 'security': 44, 'Game': 9, 'Design': 151, 'Web': 130, 'Development': 64, 'Machine': 10, 'Learning': 35, 'Technology': 110, 'Digital': 178, 'Graphic': 5, 'NLP': 4, 'software': 94, 'coding': 6, 'programming': 127, 'cryptography': 0, 'data': 532, 'science': 114}
def save_img(sorted_dict, name):
    max_x = len(sorted_dict)
    max_y = sorted_dict[-1][1]

    # print max_x, max_y

    labels = []
    y = []

    for term in sorted_dict:
        labels.append(term[0])
        y.append(term[1])

    N = len(y)
    x = range(N)
    # print x, y
    width = 0.1
    plt.bar(x, y, width, color="blue")
    plt.xticks(x, labels)

    fig = plt.gcf()
    fig.set_size_inches(50, 20)
    fig.savefig(name, dpi=100)


sorted_dict_1 = sorted(Computing_unigrams_Dict.items(), key=operator.itemgetter(1))
sorted_dict_2 = sorted(Library_unigrams_dict.items(), key=operator.itemgetter(1))
save_img(sorted_dict_1, "Computing_unigram_histogram_no_stem.png")
save_img(sorted_dict_2, "Library_unigram_histogram2_no_stem.png")

