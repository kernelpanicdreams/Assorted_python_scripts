import random

firstWord = ["Crayon-eating", "Discount", "Emotionally", "Budget", "Malfunctioning", "Overcooked", "Sentient", "Bootleg", "Unlicensed", "Rusty",
 "Quantum", "Low-resolution", "Passive-aggressive", "Misfiring", "Dollar-store", "Glitchy", "Inflated", "Unpaid", "Recycled", "Wannabe",
 "Expired", "Malnourished", "Unstable", "Forgotten", "Derailed", "Emotionally", "Budget", "Unreadable", "Misguided", "Discount",
 "Unfiltered", "Overclocked", "Sentient", "Unlicensed", "Rusty", "Glitchy", "Inflated", "Bootleg", "Passive-aggressive", "Recycled",
 "Wannabe", "Expired", "Malfunctioning", "Forgotten", "Derailed", "Emotionally", "Budget", "Unreadable", "Misguided", "Discount"]
secondWord = ["window", "brain", "bankrupt", "Bond", "sarcasm", "logic", "typo", "thought", "chaos", "meme",
 "clown", "intellect", "spreadsheet", "ego", "philosopher", "moral", "self-worth", "drama", "insult", "wisdom",
 "charm", "brain", "sarcasm", "plot", "logic", "constipated", "villain", "facial", "confidence", "charisma",
 "cringe", "ego", "buzzword", "opinion", "comeback", "personality", "drama", "wisdom", "toaster", "joke",
 "logic", "relevance", "charm", "character", "thought", "bankrupt", "sarcasm", "mood", "roast", "villain"]
thirdWord = ["licker", "emulator", "gremlin", "villain", "detector", "pancake", "generator", "processor", "distributor", "recycler",
 "anomaly", "intellect", "spreadsheet", "cannon", "philosopher", "compass", "self-worth", "intern", "machine", "sponge",
 "coupon", "cell", "reactor", "device", "train", "robot", "arc", "expression", "missile", "pack",
 "dispenser", "chip", "cloud", "launcher", "engine", "patch", "balloon", "module", "toaster", "archive",
 "sponge", "token", "protocol", "arc", "train", "algorithm", "bundle", "ring", "attempt", "monologue"]
def generateinsult() -> str:
    return "You " +random.choice(firstWord) + " " +random.choice(secondWord) + " " +random.choice(thirdWord)
print (generateinsult())