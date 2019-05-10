import re
from threading import Timer

import sublime_plugin
import sublime

DEFAULT_NAME = 'Find Results'
ALT_NAME_BASE = 'Find Results '
MAX_QUERY = 8
NEXT_LINE_SYMBOL = '↲'


def truncate(str):
    return str[:MAX_QUERY].rstrip() + '...'if len(str) > MAX_QUERY else str


class OpenSearchInNewTab(sublime_plugin.EventListener):

    # set a bit changed name
    # so the tab won't be bothered
    # during new search
    def on_activated(self, view):
        if self.is_search_view(view):
            t = Timer(.001, self.update_view, (view,))
            t.start()

    # these hooks will help other plugins
    # to understand that we are in search results file
    def on_text_command(self, view, command_name, args):
        if self.is_search_view(view):
            self.update_view(view)

    def get_alt_name(self, view):
        first_line_coords = view.full_line(sublime.Region(0, 0))
        first_line = view.substr(sublime.Region(*first_line_coords))
        match = re.search('^Searching \d+ files for "(.*)("?)$', first_line)

        if match:
            query = truncate(match.group(1))
            is_multiline = not match.group(2)

            if is_multiline:
                query = query + ' ' + NEXT_LINE_SYMBOL

            query = truncate(query)

            return DEFAULT_NAME + ': "' + query + '"'

        return ALT_NAME_BASE

    def update_view(self, view):
        view.set_name(self.get_alt_name(view))

    def is_search_view(self, view):
        name = view.name()

        return (
            name == DEFAULT_NAME or
            name == ALT_NAME_BASE or
            name == self.get_alt_name(view)
            )
