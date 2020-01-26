import wx
import ebook_utility_tool as eu
import ebook_list
# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(parent=None, title='Hello World')
#         panel = wx.Panel(self)
#         my_sizer = wx.BoxSizer(wx.VERTICAL)
#         self.text_ctrl = wx.TextCtrl(panel)
#         my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
#         my_btn = wx.Button(panel, label='Press Me')
#         my_btn.Bind(wx.EVT_BUTTON, self.on_press)
#         my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
#         panel.SetSizer(my_sizer)
#         self.Show()
#
#     def on_press(self, event):
#         value = self.text_ctrl.GetValue()
#         if not value:
#             print("You didn't enter anything!")
#         else:
#             print(f'You typed: "{value}"')
class Mp3Frame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                         title='EbookList')
        self.panel = eu.Mp3Panel(self)

        self.Show()


if __name__ == '__main__':
    app = wx.App(False)
    frame = Mp3Frame()
    app.MainLoop()