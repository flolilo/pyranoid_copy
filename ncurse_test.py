#!/usr/bin/env python
'''
    CREDIT: Derived from https://bitbucket.org/npcole/npyscreen/src/default/examples/EXAMPLE-multiple-screens.py
    Copyright (c) 2004--2009, Nicholas P. S. Cole (n@npcole.com)
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
        * Redistributions of source code must retain the above copyright
        notice, this list of conditions and the following disclaimer.
        * Redistributions in binary form must reproduce the above copyright
        notice, this list of conditions and the following disclaimer in the
        documentation and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDER ''AS IS'' AND ANY
    EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY
    DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
    ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
import npyscreen
import curses


class MyTestApp(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.ElegantTheme)
        # When Application starts, set up the Forms that will be used.
        # These two forms are persistent between each edit.
        self.addForm("MAIN", MainForm, name="Screen 1", color="IMPORTANT",)
        self.addForm("SECOND", MainForm, name="Screen 2", color="IMPORTANT",)
        # This one will be re-created each time it is edited.
        self.addFormClass("ABOUT", MainForm, name="Screen 3", color="WARNING",)

    def onCleanExit(self):
        npyscreen.notify_wait("Goodbye!")

    def change_form(self, name):
        # Switch forms.  NB: Do *not* call the .edit() method directly (which would lead to a memory leak and
        # ultimately a recursion error). Instead, use the method .switchForm to change forms:
        self.switchForm(name)

        # By default the application keeps track of every form visited.
        # There's no harm in this, but we don't need it so:
        self.resetHistory()


class MainForm(npyscreen.ActionFormV2):
    def create(self):
        self.add(npyscreen.TitleText, name="Text:", value="Press ^T to change screens")
        self.add_handlers({"^T": self.change_forms})
        if(self.name == "Screen 1"):
            self.add(npyscreen.CheckBox)

    def on_ok(self):
        # TODO: Print something if OK button is pressed:
        print("print")

    def on_cancel(self):
        # Exit the application if the cancel button is pressed.
        self.parentApp.switchForm(None)

    def change_forms(self, *args, **keywords):
        if self.name == "Screen 1":
            change_to = "SECOND"
        elif self.name == "Screen 2":
            change_to = "ABOUT"
        else:
            change_to = "MAIN"

        # Tell the MyTestApp object to change forms.
        self.parentApp.change_form(change_to)


def main():
    TA = MyTestApp()
    TA.run()


if __name__ == '__main__':
    main()
