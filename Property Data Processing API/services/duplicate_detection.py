from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, str(a), str(b)).ratio()


def find_duplicates(df):
    duplicates = []

    for i in range(len(df)):
        for j in range(i+1, len(df)):
            score = similarity(df.iloc[i]["address"], df.iloc[j]["address"])

            if score > 0.85:
                duplicates.append((i, j))

    return duplicates