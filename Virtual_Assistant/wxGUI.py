import os
import wx
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
import wolframalpha
import wikipedia

#text to speech with py-espeak-ng
import talkey
tts = talkey.Talkey(
    preferred_languages=['en'],
    preferred_factor=80.0,
    engine_preference=['espeak'],
    espeak={
        # Specify the engine options:
        'options': {
            'enabled': True,
        },
        # Specify some default voice options
        'defaults': {
                'words_per_minute': 150,
                'variant': 'f4',
        },
        # Here you specify language-specific voice options
        'languages': {
            'en': {
                'voice': 'english-mb-en1',
                'words_per_minute': 130
            }
        }
    }
)

path           = '~/Desktop/Completed_Projects/python_projects/Virtual_Assistant'
from dotenv import load_dotenv
project_folder = os.path.expanduser(path)
load_dotenv(os.path.join(project_folder, '.env'))
WOLFRAM_APP_ID = os.getenv("WOLFRAM_APP_ID")

client         = wolframalpha.Client(WOLFRAM_APP_ID)

tts.say('Welcome ask me anything')
class MyFrame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(
            self,
            None,
            pos   = wx.DefaultPosition,
            size  = wx.Size(450,450),
            title = 'Virtual Assistant',
            style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                    wx.CLOSE_BOX | wx.CLIP_CHILDREN
        )

        panel     = wx.Panel(self)
        my_sizer  = wx.BoxSizer(wx.VERTICAL)

        lbl       = wx.StaticText(
            panel,
            label ="Ask your Question!"
        )

        my_sizer.Add(lbl,0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):

        input = self.txt.GetValue()
        input = input.lower()

        try:
            res            = client.query(input)
            answer         = next(res.results).text
            print answer
            tts.say(answer)
        except:
            input = input.split(' ')
            input = " ".join(input[2:])
            tts.say("Searched for "+ input)
            print wikipedia.summary(input, sentences=2)



if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()