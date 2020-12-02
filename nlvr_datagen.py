import json

jsonlist = []
sentence = []
sentence1 = []
type_sent = []

with open('train.json') as f:
    for jsonObj in f:
        jsondict = json.loads(jsonObj)
        jsonlist.append(jsondict)
        sent = jsondict["sentence"]
        if "there is exactly" in sent.lower():
            # print(sent)
            sentence.append(sent.lower())
        else:
            pass

for item in sentence:
    if item in sentence1:
        pass
    else:
        sentence1.append(item)
        print(item)

# 12410 items
# 2215 unique sentences
print(len(sentence))
print(len(sentence1))
sent_list = {}

for sentences in sentence1:
    print(len(sent_list), sent_list)
    if len(sent_list) == 0:
        print("\n")
        print(sentences)
        val = input("Enter sentence type: ")
        sent_list["{}".format(val)] = []
        sent_list["{}".format(val)].append(sentences)

    else:
        a = [x for x in sent_list if x in sentences]
        if len(a) > 0:
            sent_list["{}".format(a[0])].append(sentences)
            print(sent_list["{}".format(a[0])], a, sent_list, '\n')

        else:
            print("\n")
            print(sentences)
            val = input("Enter sentence type: ")
            if "{}".format(val) in sent_list:
                sent_list["{}".format(val)].append(sentences)

            else:
                sent_list["{}".format(val)] = []
                sent_list["{}".format(val)].append(sentences)
