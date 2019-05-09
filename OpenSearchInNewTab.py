import sublime_plugin

DEFAULT_NAME = 'Find Results'
ALT_NAME = 'Find Results '


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
            view.set_name(DEFAULT_NAME)

    def post_text_command(self, view, command_name, args):
        if self.is_search_view(view):
            self.apply_alt_name(view)

    def apply_alt_name(self, view):
        view.set_name(ALT_NAME)

    def is_search_view(self, view):
        name = view.name()
        return name == ALT_NAME or name == DEFAULT_NAME
