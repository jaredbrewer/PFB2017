3/168: import SeqIO from Bio
3/169: from Bio import SeqIO
3/170: SeqIO
 4/1: import sys
 4/2:
from Bio import SeqIO
from Bio.Alphabet import DNAAlphabet

sprot = SeqIO.parse("uniprot_sprot.fasta", "fasta", DNAAlphabet)
 4/3: len(sprot)
 4/4: sprot
 4/5:
from Bio import SeqIO
from Bio.Alphabet import ProteinAlphabet

sprot = SeqIO.parse("uniprot_sprot.fasta", "fasta", ProteinAlphabet())
 4/6: sprot
 4/7: len(sprot)
 4/8:
from Bio import SeqIO
from Bio.Alphabet import ProteinAlphabet

sprot = SeqIO.parse("uniprot_sprot.fasta", "fasta")
 4/9: sprot
4/10: len(sprot)
4/11: sprot
4/12:
from Bio import SeqIO
from Bio.Alphabet import ProteinAlphabet

sprot_raw = "uniprot_sprot.fasta"
for record in SeqIO.parse(sprot_raw, "fasta"):
    print("ID: {:s}".format(record))
4/13:
from Bio import SeqIO
from Bio.Alphabet import ProteinAlphabet

sprot_raw = "uniprot_sprot.fasta"
for record in SeqIO.parse(sprot_raw, "fasta"):
    print("ID: {:s}".format(record.id))
4/14:
from Bio import SeqIO
from Bio.Alphabet import ProteinAlphabet

sprot_raw = "uniprot_sprot.fasta"
for record in SeqIO.parse(sprot_raw, "fasta"):
    print("ID: {:s}".format(record.id))
    print(len(record))
4/15:
from Bio import SeqIO
from Bio.Alphabet import ProteinAlphabet

sprot_raw = "uniprot_sprot.fasta"
for record in SeqIO.parse(sprot_raw, "fasta"):
    print("ID: {:s}".format(record.id))
print(len(SeqIO.parse(sprot_raw, "fasta")))
4/16:
from Bio import SeqIO
from Bio.Alphabet import ProteinAlphabet

sprot_raw = "uniprot_sprot.fasta"
list_of_ids = []
count = 1
for record in SeqIO.parse(sprot_raw, "fasta"):
    # print("ID: {:s}".format(record.id))
    list_of_ids.append(record.id)
    count +=1
print(count)
4/17: list_of_ids
4/18: len(list_of_ids)
4/19: import re
4/20:
for record in re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", SeqIO.parse(sprot_raw, "fasta"))
    print(record)
4/21:
for record in re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", SeqIO.parse(sprot_raw, "fasta")):
    print(record)
4/22:
for record in re.findall(r"(^OS=[A-Z].+?$)\s([a-z]?$)", SeqIO.parse(sprot_raw, "fasta")):
    print(record)
4/23:
for record in re.findall(r"(^OS=[A-Z].+?$)", SeqIO.parse(sprot_raw, "fasta")):
    print(record)
4/24:
for record in re.findall(r"^OS=[A-Z].+?$ [a-z]?$", SeqIO.parse(sprot_raw, "fasta")):
    print(record)
4/25: sprot_parse = SeqIO.parse(sprot_raw, "fasta")
4/26: sprot_parse
4/27:
for string in re.findall(r"^OS=\w+?", sprot_parse):
    print(string)
4/28: sprot_str = str(sprot_parse)
4/29: sprot_str
4/30:
for string in re.findall(r"^OS=\w+?", sprot_str):
    print(string)
4/31:
for string in re.findall(r"^OS=\w+?", sprot_str):
    print(string)
4/32:
for string in re.findall(r"^OS=\w+", sprot_str):
    print(string)
4/33: string
4/34:
for string in re.findall(r"OS\=\w.+\s[a-z].+?\s", sprot_str):
    print(string)
4/35: species = []
4/36:
for string in re.findall(r"OS\=\w.+\s[a-z].+?\s", sprot_str):
    species.append(string)
#    print(string)
print(len(species))
4/37:
for string in re.findall(r"OS\=\w.+\s[a-z].+?\s", sprot_str):
    species.append(string)
#    print(string)
print(len(species))
4/38: matches = re.findall(r"OS\=\w.+\s[a-z].+?\s", sprot_str)
4/39: print(matches)
4/40: matches = re.findall(r"OS\=\w.+\s[a-z].+?\s", sprot_parse)
4/41: matches = re.findall(r"OS\=\w.+\s[a-z].+?\s", sprot_str)
4/42: len(matches)
4/43: len(sprot_str)
4/44: sprot_str
4/45: print(sprot_str)
4/46: matches = re.findall(r"OS\=\w.+\s[a-z].+?\s", sprot_raw)
4/47: matches
4/48: len(matches)
4/49: records = list(SeqIO.parse(sprot_raw, "fasta"))
4/50: len(records)
4/51:
for entry in records:
    matches = re.findall("OS\=\w.+\s[a-z].+?\s", entry)
4/52: records
4/53:
for entry in records:
    matches = re.findall("OS\=\w.+\s[a-z].+?\s", entry[2])
4/54:
for entry in records:
    matches = re.findall("OS\=\w.+\s[a-z].+?\s", entry[3])
4/55: matches = re.findall(r"OS\=\w.+\s[a-z].+?\s", sprot_str[3])
4/56: len(matches)
4/57:
for string in re.findall(r"OS\=\w.+\s[a-z].+?\s", sprot_str[3]):
    species.append(string)
#    print(string)
print(len(species))
4/58: species
4/59: sprot_str = str(SeqIO.parse(sprot_raw, "fasta"))
4/60: sprot_str
4/61: sprot_raw
4/62: sprot_parse
4/63: matches = re.findall(r"OS\=\w.+\s[a-z].+?\s", sprot_str)
4/64: matches
4/65: sprot_dict = SeqIO.to_dict(sprot_parse)
4/66: sprot_dict
4/67: matches = re.findall(r"OS\=\w.+\s[a-z].+?\s", sprot_dict[1])
4/68: species = []
4/69: for record in SeqIO.parse(sprot_raw, "fasta")
4/70:
for record in SeqIO.parse(sprot_raw, "fasta"):
    species.append(record.description)
4/71: species
4/72: matches = []
4/73:
for item in species:
    matches = re.findall(r"OS\=\w.+\s[a-z].+?\s", item)
4/74: matches
4/75:
for item in species:
    list = re.findall(r"OS\=\w.+\s[a-z].+?\s", item)
    matches =+ list
4/76:
for item in species:
    list = re.findall(r"OS\=\w.+\s[a-z].+?\s", item)
    matches.append(list)
4/77: +
4/78:
for key, record in SeqIO.parse(sprot_raw, "fasta"):
    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", record.description)
    print(found)
4/79:
for key in SeqIO.parse(sprot_raw, "fasta"):
    for record in key
        found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", record.description)
        print(found)
4/80:
for key in SeqIO.parse(sprot_raw, "fasta"):
    for record in key:
        found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", record.description)
        print(found)
4/81:
for key, record in SeqIO.parse(sprot_raw, "fasta"):
    print(record.id)
4/82:
for key, record in SeqIO.parse(sprot_raw, "fasta"):
    print(key, record.id)
4/83:
for key, record in SeqIO.parse(sprot_raw, "fasta"):
    print(key, record.id)
4/84: from Bio import SeqIO
4/85:
for key, record in SeqIO.parse(sprot_raw, "fasta"):
    print(key, record)
4/86:
for key, record in sprot_parse:
    print(key, record)
4/87:
for key, record in sprot_parse:
    print(key)
4/88: sprot_dict = SeqIO.to_dict(sprot_parse)
4/89: sprot_dict
4/90: sprot_parse
4/91: sprot_dict = SeqIO.to_dict(sprot_parse)
4/92: sprot_dict
4/93: sprot_dict = SeqIO.to_dict(sprot_raw)
4/94: sprot_dict = SeqIO.to_dict(sprot_parse)
4/95: sprot_dict
4/96: sprot_raw
4/97: SeqIO.to_dict(sprot_parse)
4/98: SeqIO.to_dict(sprot_str)
4/99: SeqIO.to_dict(SeqIO.parse("uniprot_sprot.fasta", "fasta"))
4/100: sprot_dict = SeqIO.to_dict(SeqIO.parse("uniprot_sprot.fasta", "fasta"))
4/101: sprot_dit
4/102: sprot_dict
4/103:
for key, value in sprot_dict:
    print(key, value)
4/104:
for key in sprot_dict:
    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", key[1])
    print(found)
4/105:
for key in sprot_dict:
#     found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", key[1])
    print(key[1])
4/106: sprot_dict
4/107:
for key in sprot_dict:
    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key][1])
    print(found)
4/108:
for key in sprot_dict:
#    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key][])
    print(sprot_dict[key][1])
)
4/109:
for key in sprot_dict:
#    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key][])
    print(sprot_dict[key][1])
4/110: sprot_dict[1]
4/111: sprot_dict
4/112: sprot_parse
4/113: sprot_parse.description
4/114: print(sprot_parse.description)
4/115: print(sprot_parse.id)
4/116:
for key in sprot_dict:
#    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key][])
    print(key)
4/117:
for key,value in sprot_dict:
#    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key][])
    print(key)
4/118:
for key,value in sprot_dict:
#    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key][])
    print(value)
4/119:
for key in sprot_dict:
#    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key][])
    print(sprot_dict[key])
4/120:
for key in sprot_dict:
#    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key][])
    print(sprot_dict[key][Description])
4/121:
for key in sprot_dict:
    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
   #  print(sprot_dict[key][Description])
    print(found)
4/122: found = []
4/123:
for key in sprot_dict:
    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
   #  print(sprot_dict[key][Description])
    print(found)
4/124:
for key in sprot_dict:
    found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", str(sprot_dict[key]))
   #  print(sprot_dict[key][Description])
    print(found)
4/125:
for key in sprot_dict:
   # found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
    re.findall(r"OS=", sprot_dict[key])
   #  print(sprot_dict[key][Description])
    print(found)
4/126:
for key in sprot_dict:
   # found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
    print(re.findall(r"^OS=", sprot_dict[key]))
   #  print(sprot_dict[key][Description])
#    print(found)
4/127:
for key in sprot_dict:
   # found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
    print(re.findall(r"", sprot_dict[key]))
   #  print(sprot_dict[key][Description])
#    print(found)
4/128:
for key in sprot_dict:
   # found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
   # print(re.findall(r"", sprot_dict[key]))
   #  print(sprot_dict[key][Description])
#    print(found)
    print(sprot_dict[key].description)
4/129:
for key in sprot_dict:
   # found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
   # print(re.findall(r"", sprot_dict[key]))
   #  print(sprot_dict[key][Description])
#    print(found)
    print(sprot_dict[key].description)

    print(re.findall(r"OS=", sprot_dict[key].description))
4/130:
for key in sprot_dict:
   # found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
   # print(re.findall(r"", sprot_dict[key]))
   #  print(sprot_dict[key][Description])
#    print(found)
    # print(sprot_dict[key].description)

    print(re.findall(r"OS=", sprot_dict[key].description))
4/131:
for key in sprot_dict:
   # found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
   # print(re.findall(r"", sprot_dict[key]))
   #  print(sprot_dict[key][Description])
#    print(found)
    # print(sprot_dict[key].description)

    print(re.findall(r"^OS=", sprot_dict[key].description))
4/132:
for key in sprot_dict:
   # found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
   # print(re.findall(r"", sprot_dict[key]))
   #  print(sprot_dict[key][Description])
#    print(found)
    # print(sprot_dict[key].description)

    print(re.findall(r"OS=[A-Z].+?", sprot_dict[key].description))
4/133:
for key in sprot_dict:
   # found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
   # print(re.findall(r"", sprot_dict[key]))
   #  print(sprot_dict[key][Description])
#    print(found)
    # print(sprot_dict[key].description)

    print(re.findall(r"OS=[A-Z].+?\s[a-z]?\s", sprot_dict[key].description))
4/134:
for key in sprot_dict:
   # found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
   # print(re.findall(r"", sprot_dict[key]))
   #  print(sprot_dict[key][Description])
#    print(found)
    # print(sprot_dict[key].description)

    print(re.findall(r"OS=[A-Z].+?\s[a-z].+?\s", sprot_dict[key].description))
4/135:
for key in sprot_dict:
   # found = re.findall(r"^OS=[A-Z].+?$\s[a-z]?$", sprot_dict[key])
   # print(re.findall(r"", sprot_dict[key]))
   #  print(sprot_dict[key][Description])
#    print(found)
    # print(sprot_dict[key].description)

    print(re.finditer(r"OS=[A-Z].+?\s[a-z].+?\s", sprot_dict[key].description))
4/136: sprot_dict = SeqIO.to_dict(SeqIO.parse("uniprot_sprot.fasta", "fasta"))
4/137: organisms = ''
4/138:
for key in sprot_dict:
    organisms += re.findall(r"OS=[A-Z].+?\s[a-z].+?\s", sprot_dict[key].description)
4/139: organisms = []
4/140:
for key in sprot_dict:
    organisms += re.findall(r"OS=[A-Z].+?\s[a-z].+?\s", sprot_dict[key].description)
4/141: organisms
4/142: organisms.lstrip("OS=")
4/143:
for organism in organisms:
    organism.lstrip("OS=")
    print(organism)
4/144:
for organism in organisms:
    organism.lstrip()
    organim.lstrip("OS=")
    print(organism)
4/145:
for organism in organisms:
    organism.lstrip()
    organism.lstrip("OS=")
    print(organism)
4/146: organism_list = []
4/147:
for organism in organisms:
    organism.lstrip()
    organism.lstrip("OS=")
    organism_list += organism
4/148: organism_list
4/149:
for organism in organisms:
    organism.lstrip()
    organism.lstrip("OS=")
    organism_list += list(organism)
4/150:
for organism in organisms:
    organism.lstrip()
    organism.lstrip("OS=")
    print(organism)
4/151:
for organism in organisms:
    organism.lstrip()
    organism.lstrip("OS=")
    organism_list = organism.split("OS=")
4/152: organism_list
4/153:
for organism in organisms:
    organism.lstrip()
    organism.lstrip("OS=")
    organism_list += organism.split("OS=")
4/154: organism_list
4/155:
for organism in organisms:
    organism.strip()
    organism_list += organism.split("OS=")
4/156: organism_list
4/157: organisms
4/158:
for organism in organisms:
    organism.strip("")
    organism_list += organism.split("OS=")
4/159: organism_list
4/160: organism_list = []
4/161:
for organism in organisms:
    organism.strip("")
    organism_list += organism.split("OS=")
4/162: organism_list
4/163:
for organism in organisms:
    organism.strip(" ")
    organism_list += organism.split("OS=")
4/164: organism_list
4/165: organism_list = []
4/166:
for organism in organisms:
    organism.strip(" ")
    organism_list += organism.split("OS=")
4/167: organism_list
4/168:
for organism in organisms:
    organism.strip("")
    organism_list += organism.split(" OS=")
4/169: organism_list
4/170:
for entry in organism_list:
    organism = entry.strip()
    organism_list += organism
4/171:
for entry in organism_list:
    organism = entry.strip()
     += organism
4/172: orgs = []
4/173:
for entry in organism_list:
    organism = entry.strip()
    orgs += organism
4/174: morgs
4/175: orgs
4/176:
for entry in organism_list:
    organism = entry.strip().split()
    organism_list += organism
4/177: organism_list = []
4/178:
for organism in organisms:
    organism.strip("")
    organism_list += organism.split(" OS=")
4/179:
for entry in organism_list:
    organism = entry.strip()
    orgs += organism
4/180: orgs
4/181:
for entry in organism_list:
    organism = entry.strip()
    orgs += organism.split()
4/182: orgs
   1: history
   2: %history -g