import json
with open("postamil.json","r",encoding="utf-8") as file:
  pos=json.load(file)
class _TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "|_ _ _" if self.parent else "";print()
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        

_root = _TreeNode("பேச்சின் பகுதி")
_verbs=_TreeNode("வினைச்சொல்")
_verbs.add_child(_TreeNode("செயல் வினைகள்(Actionverbs)"))
_verbs.add_child(_TreeNode("நிலையான வினைச்சொற்கள்(Stativeverbs)"))
_verbs.add_child(_TreeNode("இணைக்கும் வினைச்சொற்கள்(Linkingverbs)"))
_verbs.add_child(_TreeNode("உதவும் வினைச்சொற்கள்(Helpingverbs)"))
_verbs.add_child(_TreeNode("மாதிரி வினைச்சொற்கள்(Modalverbs)"))
_verbs.add_child(_TreeNode("வழக்கமான வினைச்சொல்(Regularverbs)"))
_verbs.add_child(_TreeNode("ஒழுங்கற்ற வினைச்சொற்கள்(Irregularverbs)"))
_verbs.add_child(_TreeNode("சொற்றொடர்கள்(Phrasalverbs)"))
_verbs.add_child(_TreeNode("முடிவிலி வினைச்சொற்கள்(Infinitivesverbs)"))


_Adverb=_TreeNode("வினையுரிச்சொல்")
_Adverb.add_child(_TreeNode("விதத்தை விவரிக்கும்(Adverbs of manner)"))
_Adverb.add_child(_TreeNode("இடத்தின் வினையுரிச்சொல்(Adverb of Place)"))
_Adverb.add_child(_TreeNode("நேரத்தின் வினையுரிச்சொல்(Adverb of Time)"))
_Adverb.add_child(_TreeNode("அதிர்வெண் வினையடை(Adverb of Frequency)"))
_Adverb.add_child(_TreeNode("பட்டத்தின் வினையுரிச்சொற்கள்(Adverbs of Degree)"))

_Noun=_TreeNode("பெயர்ச்சொல்")
_Noun.add_child(_TreeNode("சரியான பெயர்ச்சொல்(Proper Noun)"))
_Noun.add_child(_TreeNode("பொதுவான பெயர்ச்சொல்(Common Noun)"))
_Noun.add_child(_TreeNode("ஒருமை பெயர்ச்சொல்(Singular Noun)"))
_Noun.add_child(_TreeNode("பன்மை பெயர்ச்சொல்(Plural Noun)"))
_Noun.add_child(_TreeNode("எண்ணக்கூடிய பெயர்ச்சொல்கள்(Countable Noun)"))
_Noun.add_child(_TreeNode("கணக்கிட முடியாத பெயர்ச்சொல்(Uncountable Noun)"))
_Noun.add_child(_TreeNode("கூட்டு பெயர்ச்சொல்(Collective Noun)"))
_Noun.add_child(_TreeNode("அருவப்பெயர்ச்சொல்(Abstract Noun)"))

_pronoun=_TreeNode("பிரதிபெயர்")
_pronoun.add_child(_TreeNode("உறவினர் பிரதிபெயர்கள்(Relative Pronouns)"))
_pronoun.add_child(_TreeNode("உடைமைப் பெயர்ச்சொல்(Possessive Pronoun)"))
_pronoun.add_child(_TreeNode("பிரதி பெயர்ச்சொற்கள்(Reflexive Pronouns)"))
_pronoun.add_child(_TreeNode("கேள்விக்குரிய பிரதிபெயர்(Interrogative Pronoun)"))
_pronoun.add_child(_TreeNode("காலவரையற்ற பிரதிபெயர்களை(Indefinite Pronouns)"))
_pronoun.add_child(_TreeNode("தனிப்பட்ட பிரதிபெயர்களை(Personal Pronouns)"))
_pronoun.add_child(_TreeNode("பொருள் பிரதிபெயர்கள்(Subject Pronouns)"))
_pronoun.add_child(_TreeNode("பொருள் பிரதிபெயர்கள்(Object Pronouns)"))
_pronoun.add_child(_TreeNode("பரஸ்பர பிரதிபெயர்கள்(Reciprocal Pronouns)"))

_Adjective=_TreeNode("உரிச்சொல்")
_Adjective.add_child(_TreeNode("உடைமை உரிச்சொற்கள்(Possessive Adjectives)"))
_Adjective.add_child(_TreeNode("கேள்விக்குரிய உரிச்சொற்கள்(Interrogative Adjectives)"))
_Adjective.add_child(_TreeNode("ஆர்ப்பாட்ட உரிச்சொற்கள்(Demonstrative Adjectives)"))
_Adjective.add_child(_TreeNode("கூட்டு உரிச்சொற்கள்(Compound Adjectives)"))

_Preposition=_TreeNode("முன்மொழிவுகள்")
_Preposition.add_child(_TreeNode("நேரத்தின் முன்மொழிவுகள்(Prepositions of time)"))
_Preposition.add_child(_TreeNode("இடத்தின் முன்மொழிவுகள்(Prepositions of Place)"))
_Preposition.add_child(_TreeNode("திசையின் முன்மொழிவுகள்(Prepositions of Direction)"))
_Preposition.add_child(_TreeNode("இருப்பிடத்தின் முன்மொழிவுகள்(Prepositions of Location)"))
_Preposition.add_child(_TreeNode("இடஞ்சார்ந்த உறவின் முன்மொழிவுகள்(Prepositions of Spatial Relationship)"))

_Conjunction=_TreeNode("இணைச்சொல்")
_Conjunction.add_child(_TreeNode("ஒருங்கிணைப்பு இணைப்புகள்(Coordinating Conjunctions)"))
_Conjunction.add_child(_TreeNode("துணை இணைப்புகள்(Subordinating Conjunctions)"))
_Conjunction.add_child(_TreeNode("தொடர்பு இணைப்புகள்(Correlative Conjunctions)"))
_Conjunction.add_child(_TreeNode("இணைந்த வினையுரிச்சொற்கள்(Conjunctive Adverbs)"))


_interjection=_TreeNode("இடைச்சொல்")
_interjection.add_child(_TreeNode("முதன்மை இடைச்சொல்(Primary Interjection)"))
_interjection.add_child(_TreeNode("இரண்டாம் நிலை இடைச்சொல்(Secondary Interjection)"))
_interjection.add_child(_TreeNode("லேசான இடைச்சொல்(Mild Interjection)"))
_interjection.add_child(_TreeNode("வலுவான இடைச்சொல்(Strong Interjection)"))
_interjection.add_child(_TreeNode("வோலிட்டிவ் இன்டர்ஜெக்ஷன்(Volitive Interjection)"))
_interjection.add_child(_TreeNode("உணர்ச்சி இடைச்செருகல்(Emotive Interjection)"))
_interjection.add_child(_TreeNode("அறிவாற்றல் இடைச்செருகல்(Cognitive Interjection)"))

class _pp:
    def _display(self):
        _root.add_child(_verbs)
        _root.add_child(_Adverb)
        _root.add_child(_Noun)
        _root.add_child(_pronoun)
        _root.add_child(_Adjective)
        _root.add_child(_Preposition)
        _root.add_child(_Conjunction)
        _root.add_child(_interjection)
        _root.print_tree()




def about_pechin_paguthi():
    print("""நாம் பள்ளியில் இருக்கும்போது அல்லது ஆங்கில மொழி கற்றல் செயல்முறையைத் தொடங்கும் போது நாம் கற்றுக் கொள்ளும் முதல் இலக்கண தலைப்புகளில் பேச்சின் பகுதிகளும் அடங்கும்.பேச்சின் பகுதிகளை ஒரு வாக்கியத்தில் வெவ்வேறு பாத்திரங்களைச் செய்யும் வார்த்தைகளாக வரையறுக்கலாம். பேச்சின் சில பகுதிகள் பேச்சின் மற்ற பகுதிகளின் செயல்பாடுகளையும் செய்ய முடியும்.""")
    x=_pp()
    x._display()
    

def display_vagaigal():
    """Displays the types in pechin paguthi   
    Args:
        None
    Returns:
        None
    """
    for i in pos["POSTypes"]:
        print(i)
def  _vilakkam(gen):
           while True:
                try:
                   user_input = input("Press Enter to see the next item or type 'exit' to quit: ")
                   print("")
                   if user_input.lower() == "exit":
                      break
                   item = next(gen)
                   print(item)
                except StopIteration:
                     print("End of data.")
                     break        
class vinaichsol:
    @staticmethod
    def about_vinaichsol():
        print(pos["verb"]["definition"])
    @staticmethod
    def get_vinaichsol_vagaigal():
                 """Displays the types in vinaichsol(verb)  
                     Args:
                          None
                     Returns:
                          None
                 """
                 _verbs.print_tree()
            
            

    @staticmethod    
    def vagaigalin_vilakkam():
        """Displays the types of explaination for each types in vinaichsol(verb)  
                     Args:
                          None
                     Returns:
                          None
        """
        def vagaigalin_vilakkam_generator():
                for i,j in pos["verb"]["Types Explaination"].items():
                     print(f"{i}--->{j}");print("\n")
                     print("example")
                     for x in pos["verb"]["example"][i]:
                          print(x)
                     yield '\n'
        _vilakkam(vagaigalin_vilakkam_generator())            

    @staticmethod
    def vinaichsol_vagaigal_List():
            """
            Return a list of vinaichsol(verbs) types .

            Returns:
                list: A list containing the vinaichsol(verb) types.
            """
        
            return(pos["verb"]["Types"])


class vinaiyurichsol:
    @staticmethod
    def about_vinaiyurichsol():
        print(pos["Adverb"]["definition"])
    @staticmethod
    def get_vinaiyurichsol_vagaigal():
             """Displays the types in vinaiyurichsol(Adverb)  
                     Args:
                          None
                     Returns:
                          None
             """
     
             _Adverb.print_tree()
    @staticmethod        
    def vagaigalin_vilakkam():
            """Displays the types of explaination for each types in vinaiyurichsol(Adverb)  
                     Args:
                          None
                     Returns:
                          None
            """
            def vagaigalin_vilakkam_generator():
                    for i,j in pos["Adverb"]["Types Explaination"].items():
                     print(i,"--->",j);print("\n")
                     print("example")
                     for x in pos["Adverb"]["example"][i]:
                          print(x)
                     yield ""
            _vilakkam(vagaigalin_vilakkam_generator())         
    @staticmethod         
    def vinaiyurichsol_vagaigal_List():
        """
            Return a list of vinaiyurichsol(Adverbs) types .

            Returns:
                list: A list containing the vinaiyurichsol(Adverb) types.
        """
        
        return(pos["Adverb"]["Types"])



class Peyarchsol:
    @staticmethod
    def about_Peyarchsol():
        print(pos["Noun"]["definition"])
    @staticmethod
    def get_Peyarchsol_vagaigal():
        """Displays the types in Peyarchsol(Noun)  
                     Args:
                          None
                     Returns:
                          None
        """
        _Noun.print_tree()
    @staticmethod        
    def vagaigalin_vilakkam():
         """Displays the types of explaination for each types in Peyarchsol(Noun)  
                     Args:
                          None
                     Returns:
                          None
         """
        
         def vagaigalin_vilakkam_generator():
                for i, j in pos["Noun"]["Types Explaination"].items():
                    print(f"{i} ---> {j}");print()
                    print("\n")
                    print("example")
                    for x in pos["Noun"]["example"][i]:
                        print(x)
                    yield "\n"
         _vilakkam(vagaigalin_vilakkam_generator())
                   
    @staticmethod         
    def Peyarchsol_vagaigal_List():
        """
            Return a list of Peyarsol(Nouns) types .

            Returns:
                list: A list containing the peyarsol(Nouns) types.
        """
        
        return(pos["Noun"]["Types"])


class Piratipeyargal:
    @staticmethod
    def about_Piratipeyargal():
        print(pos["Pronouns"]["definition"])
    @staticmethod
    def get_Piratipeyargal_vagaigal():
        """Displays the types of explaination for each types in Piratipeyargal(Pronouns)  
                     Args:
                          None
                     Returns:
                          None
        """
        
        _pronoun.print_tree()
    @staticmethod        
    def vagaigalin_vilakkam():
         """Displays the types of explaination for each types in Piratipeyargal(Pronoun)  
                     Args:
                          None
                     Returns:
                          None
         """
         def vagaigalin_vilakkam_generator():
                 for i,j in pos["Pronouns"]["Types Explaination"].items():
                     print(i,"--->",j);print("\n")
                     print("example")
                     for x in pos["Pronouns"]["example"][i]:
                          print(x)
                     yield ""
         _vilakkam(vagaigalin_vilakkam_generator())            
    @staticmethod         
    def Piratipeyargal_vagaigal_List():
        """
            Return a list of Piratipeyargal(Pronoun)   types .

            Returns:
                list: A list containing the Piratipeyargal(Pronoun)  types.
        """
        return(pos["Pronouns"]["Types"])
    

class vurichsol:
    @staticmethod  
    def about_vurichsol():
        print(pos["Adjective"]["definition"])
        
    @staticmethod
    def get_vurichsol_vagaigal():
        """Displays the types of explaination for each types in vurichsol(Adjective)  
                     Args:
                          None
                     Returns:
                          None
        """
       
        _Adjective.print_tree()
    @staticmethod        
    def vagaigalin_vilakkam():
        """Displays the types of explaination for each types in vurichsol(Adjective)  
                     Args:
                          None
                     Returns:
                          None
        """
        def vagaigalin_vilakkam_generator():
                for i,j in pos["Adjective"]["Types Explaination"].items():
                     print(i,"--->",j);print("\n")
                     print("example")
                     for x in pos["Adjective"]["example"][i]:
                          print(x)
                     yield ""
        _vilakkam(vagaigalin_vilakkam_generator())             
    @staticmethod 
    def vurichsol_vagaigal_List():
        """
            Return a list of vurichsol(Adjective)   types .

            Returns:
                list: A list containing the vurichsol(Adjective)  types.
        """
        
        return(pos["Adjective"]["Types"])

class Munmolivu:
    @staticmethod
    def about_Munmolivu():
        print(pos["Preposition"]["definition"])
    @staticmethod
    def get_Munmolivu_vagaigal():
        """Displays the types of explaination for each types in Munmolivu(Preposition)  
                     Args:
                          None
                     Returns:
                          None
        """
        _Preposition.print_tree()
    @staticmethod         
    def vagaigalin_vilakkam():
        """Displays the types of explaination for each types in Munmolivu(Preposition)  
                     Args:
                          None
                     Returns:
                          None
        """
        def vagaigalin_vilakkam_generator() :
                for i,j in pos["Preposition"]["Types Explaination"].items():
                     print(i,"--->",j);print("\n")
                     print("example")
                     for x in pos["Preposition"]["example"][i]:
                          print(x)
                     yield ""
        _vilakkam(vagaigalin_vilakkam_generator())
      
    @staticmethod
    def Munmolivu_vagaigal_List():
        """
            Return a list of Munmolivu(Preposition)   types .

            Returns:
                list: A list containing the Munmolivu(Preposition)  types.
        """
        
        return(pos["Preposition"]["Types"])


class Inaippukal:
    @staticmethod
    def about_Inaippukal():
        print(pos["Conjunctions"]["definition"])
    @staticmethod
    def get_Inaippukal_vagaigal():
        """Displays the types of explaination for each types in Inaippukal(Conjunctions)  
                     Args:
                          None
                     Returns:
                          None
        """
        _Conjunction.print_tree()
    @staticmethod         
    def vagaigalin_vilakkam():
        """Displays the types of explaination for each types in Inaippukal(Conjunctions)  
                     Args:
                          None
                     Returns:
                          None
        """
        def vagaigalin_vilakkam_generator():
                for i,j in pos["Conjunctions"]["Types Explaination"].items():
                     print(i,"--->",j);print("\n")
                     print("example")
                     for x in pos["Conjunctions"]["example"][i]:
                          print(x)
                     yield "\n"
        _vilakkam(vagaigalin_vilakkam_generator())             
    @staticmethod         
    def Inaippukal_Inaippukal_List():
        """
            Return a list of Inaippukal(Conjunctions)    types .

            Returns:
                list: A list containing the Inaippukal(Conjunctions)   types.
        """
        return(pos["Conjunctions"]["Types"])


class idaichsol:
    @staticmethod
    def about_idaichsol():
        print(pos["interjection"]["definition"])
    @staticmethod
    def get_idaichsol_vagaigal():
        """Displays the types of explaination for each types in idaichsol(interjection)  
                     Args:
                          None
                     Returns:
                          None
        """
        _interjection.print_tree()
    @staticmethod        
    def vagaigalin_vilakkam():
         """Displays the types of explaination for each types in idaichsol(interjection)  
                     Args:
                          None
                     Returns:
                          None
         """
         def vagaigalin_vilakkam_generator():
                 for i, j in pos["interjection"]["Types Explaination"].items():
                            print(f"{i} ---> {j}");print("\n")
                            print("example")
                            for x in pos["interjection"]["example"][i]:
                                print(x)
                            yield ""
          
         _vilakkam(vagaigalin_vilakkam_generator())
    @staticmethod         
    def idaichsol_Inaippukal_List():
        """
            Return a list of idaichsol(interjection)    types .

            Returns:
                list: A list containing the idaichsol(interjection)   types.
        """
        return(pos["interjection"]["Types"])
    

