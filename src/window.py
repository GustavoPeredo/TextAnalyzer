# window.py
#
# Copyright 2022 Gustavo Peredo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, Adw


@Gtk.Template(resource_path='/xyz/gustavomachadoperedo/TextAnalyzer/window.ui')
class TextanalyzerWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'TextanalyzerWindow'

    #label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def text_updated_cb(self, *args):
        print("hello")

    @Gtk.Template.Callback()
    def show_review_cb(self, *args):
        print("hello2")

    @Gtk.Template.Callback()
    def hide_review_cb(self, *args):
        print("hello3")

    @Gtk.Template.Callback()
    def folds_cb(self, *args):
        print("hello4")


class AboutDialog(Gtk.AboutDialog):

    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = 'textanalyzer'
        self.props.version = "0.1.0"
        self.props.authors = ['Gustavo Peredo']
        self.props.copyright = '2022 Gustavo Peredo'
        self.props.logo_icon_name = 'xyz.gustavomachadoperedo.TextAnalyzer'
        self.props.modal = True
        self.set_transient_for(parent)
