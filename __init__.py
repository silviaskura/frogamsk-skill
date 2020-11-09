from mycroft import MycroftSkill, intent_file_handler


class Frogamsk(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('frogamsk.intent')
    def handle_frogamsk(self, message):
        self.speak_dialog('frogamsk')


def create_skill():
    return Frogamsk()

