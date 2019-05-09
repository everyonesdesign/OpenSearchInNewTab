import re
from threading import Timer

import sublime_plugin
import sublime

DEFAULT_NAME = 'Find Results'
ALT_NAME_BASE = 'Find Results '


class OpenSearchInNewTab(sublime_plugin.EventListener):

    # set a bit changed name
    # so the tab won't be bothered
    # during new search
    def on_activated(self, view):
        if self.is_search_view(view):
            self.apply_alt_name(view)

    # these hooks will help other plugins
    # to understand that we are in search results file
    def on_text_command(self, view, command_name, args):
        if self.is_search_view(view):
            self.apply_default_name(view)

    def post_text_command(self, view, command_name, args):
        if self.is_search_view(view):
            self.apply_alt_name(view)

    def get_alt_name(self, view):
        first_line_coords = view.full_line(sublime.Region(0, 0))
        first_line = view.substr(sublime.Region(*first_line_coords))
        match = re.search('Searching \d+ files for "(.*)"$', first_line)

        if match:
            query = match.group(1)
            return ALT_NAME_BASE + '"' + query + '"'

        return ALT_NAME_BASE

    def apply_alt_name(self, view):
        t = Timer(.1, self.apply_alt_name_async, (view,))
        t.start()

    def apply_alt_name_async(self, view):
        view.set_name(self.get_alt_name(view))

    def apply_default_name(self, view):
        view.set_name(DEFAULT_NAME)
        self.apply_alt_name(view)

    def is_search_view(self, view):
        name = view.name()

        print('name ' + name)
        print('alt_name ' + self.get_alt_name(view))

        return (
            name == DEFAULT_NAME or
            name == ALT_NAME_BASE or
            name == self.get_alt_name(view)
            )
