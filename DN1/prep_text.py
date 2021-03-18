alphabet = "abcdefghijklmnopqrstuvwxyz"

def prep(text):
    # text.lower()
    out = ""
    for c in text.lower():
        if c in alphabet:
            out += c
    
    return out
        
text = """-Hello there! -So Uncivilized. -Sith Lords are our specialty! -It's over Anakin I have the high ground. -Another happy landing! -That's why i'm here. -Your move! -Do you have a plan B? -One things for sure the negotiations were short. -Why do I feel you're going to be the death of me? -No nothing too fancy. -Always on the move. -Wait a minute how did this happen? we're smarter than this. -I hate it when he does that. -Only a Sith deals in absolutes. -I will do what I must. -What took you so long? -Oh not good. -You will never find a more wretched hive of scum and villainy. -Who's more foolish the fool or the fool who follows him? -If you strike me down I will become more powerful than you could possibly imagine. -The force will be with you always. -So what I told you was true from a certain point of view. -Another happy landing! -Oh how the mighty Sith have fallen. -Oh this is going to be easy. -Oh I have a bad feeling about this. -Don't try it. -My allegiance is to the republic, to democracy! -Not to worry were still flying half a ship."""



print(prep(text))