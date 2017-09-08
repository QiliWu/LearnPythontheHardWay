class Song(object):

    lyrics = 124

    def __init__(self, lyrics):
        self.lyrics = lyrics
        print lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])


happy_bday.sing_me_a_song()   #first init, then sing_me_a_song

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

print happy_bday.lyrics   #just init, no sing_me_a_song

print bulls_on_parade.lyrics
