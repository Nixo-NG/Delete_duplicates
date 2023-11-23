import os

Textfilter = str(input(r"Your combo: "))
if not os.path.isdir("Filtered_Emails"):
    os.mkdir("Filtered_Emails")
else:
    pass

Emails_filtered = open("Filtered_Emails/duplicate_removed.txt", 'a', encoding="utf8", errors="ignore")
set1 = set()

with open(Textfilter, 'r') as file:
    for i in file:
        if i not in set1:
            Emails_filtered.write(i)
            set1.add(i)
        elif i in set1:
            continue
        else:
            continue
