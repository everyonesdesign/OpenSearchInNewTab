import sublime_plugin

DEFAULT_NAME = 'Find Results'
ALT_NAME = 'Find Results '

class OpenSearchInNewTab(sublime_plugin.EventListener):

	# set a bit changed name
	# so the tab won't be bothered
	# during new search
	def on_activated(self, view):
		if view.name() == DEFAULT_NAME:
			view.set_name(ALT_NAME)

	# these hooks will help other plugins
	# to understand that we are in search results file
	def on_text_command(self, view, command_name, args):
		if view.name() == ALT_NAME:
			view.set_name(DEFAULT_NAME)

	def post_text_command(self, view, command_name, args):
		if view.name() == DEFAULT_NAME:
			view.set_name(ALT_NAME)
