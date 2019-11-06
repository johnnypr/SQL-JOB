entry = "Apple Inc."
mod_entry = None
abbreviations = '''Ltd S.A. SA A.G AG N.V.NV Ltee BV B.V. 
GmbH L.L.C. LLC Inc. Inc Corporation Corp 
Pte. Ltd Holdings HLDGNS incorporated ass association cl -a etf'''

for index in entry.split(" "):
    for abb in abbreviations.split(' '):
        if index == abb:
            mod_entry= entry.replace(abb,'')

print("Before: ", entry)
print("After: ",mod_entry)