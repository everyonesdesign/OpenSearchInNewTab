import sublime_plugin

DEFAULT_NAME = 'Find Results'
ALT_NAME = 'Find Results '

class OpenSearchInNewTab(sublime_plugin.EventListener):

	def on_deactivated(self, view):
		if view.name() == 'Find Results':
			# set a name with space
			# so it won't be bothered
			# during new search
			view.set_name(ALT_NAME)

	# these hooks will help other plugins
	# to understand that we are in search results file
	def on_text_command(self, view, command_name, args):
		if view.name() == ALT_NAME:
			view.set_name(DEFAULT_NAME)

	def post_text_command(self, view, command_name, args):
		if view.name() == DEFAULT_NAME:
			view.set_name(ALT_NAME)
