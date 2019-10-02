class Message:
    def __init__(self, username=None, filepath=None, message=None, time=None, likenumber=None, m_num=None, c_number=None
                 , up_ed=None):
        self.username = username
        self.filepath = filepath
        self.message = message
        self.time = time
        self.likenumber = likenumber
        self.m_num = m_num
        self.c_number = c_number
        self.up_ed = up_ed


class Comment:
    def __init__(self, filename=None, username=None, comment=None, time=None, c_num=None, up_ed=None):
        self.filename = filename
        self.username = username
        self.time = time
        self.comment = comment
        self.c_num = c_num
        self.up_ed = up_ed


class Like:
    def __init__(self, filename=None, username=None):
        self.filename = filename
        self.username = username
