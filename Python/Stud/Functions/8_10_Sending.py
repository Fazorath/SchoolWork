Texts = ['Hello loser','Message number 2 in the test program','gangam style was such a banger back then','Message number 4']
sent = []


def showmessages(list):
    for text in list:
        print(text)
def sendMessages(list,sent):
    while Texts:
        sending = Texts.pop()
        print(f"Currently sending: {sending}")
        sent.append(sending)
    print(f"\nNow empty list of texts {Texts}") ## Empty List now of texts
    print(f"\nNow populated list of sent Messages {sent}\n") ## Populated list with the sent messages.


sendMessages(Texts,sent)

