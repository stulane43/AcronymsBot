import json

class Acronyms():
    
    def __init__(self):
        with open('configuration/acronyms.json', 'r') as file:
            self.keyTerms = json.load(file)
    
    def searchAcronym(self, acronym):
        acronym = acronym.strip()
        if acronym in self.keyTerms.keys():
            try:
                definition = f"*{self.keyTerms[acronym]['definition']}*\n"
            except:
                definition = f" "
            try:
                description = f"```{self.keyTerms[acronym]['description']}```"
            except:
                description = "`No Description Available`"
            return {'found': True, 'acronym': acronym, 'definition': definition, 'description': description}
        else:
            return {'found': False, 'acronym': acronym}
        
    def getAllAcronyms(self):
        acronymList = []
        allAcronyms = []
        acronymnKeys = list(self.keyTerms.keys())
        acronymnKeys.sort()
        for acronym in acronymnKeys:
            try:
                definition = f"*{self.keyTerms[acronym]['definition']}*\n"
            except:
                definition = " "
            try:
                description = f"```{self.keyTerms[acronym]['description']}```"
            except:
                description = "`No Description Available`"
            acronymList.append(f"*`{acronym}`* {definition}{description}")
            if len(acronymList) > 19:
                acronyms = '\n\n\n'.join(acronymList)
                allAcronyms.append(acronyms)
                acronymList = []
                print(len(acronyms))
        acronyms = '\n\n\n'.join(acronymList)
        allAcronyms.append(acronyms)
        print(len(acronyms))    
        return allAcronyms