import re
from threading import Timer

import sublime_plugin
import sublime

DEFAULT_NAME = 'Find Results'
ALT_NAME_BASE = DEFAULT_NAME + ' '
MAX_QUERY = 16
NEXT_LINE_SYMBOL = '↲'
ELLIPSIS = '…'


def truncate(str):
    return str[:MAX_QUERY].rstrip() + ELLIPSIS if len(str) > MAX_QUERY else str


class OpenSearchInNewTab(sublime_plugin.EventListener):

    # set a bit changed name
    # so the tab won't be bothered
    # during new search
    def on_activated_async(self, view):
        if self.is_search_view(view):
            t = Timer(.001, self.update_view, (view,))
            t.start()

    def get_alt_name(self, view):
        first_line_coords = view.full_line(sublime.Region(0, 0))
        first_line = view.substr(first_line_coords)
        match = re.search('^Searching \d+ files for "(.*?)(")?$', first_line)

        if match:
            query = match.group(1)
            is_multiline = not match.group(2)

            if is_multiline:
                query = query.rstrip() + ' ' + NEXT_LINE_SYMBOL

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