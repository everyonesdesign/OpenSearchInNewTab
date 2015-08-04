import sublime_plugin

default_name = 'Find Results'
alt_name = 'Find Results '

class OpenSearchInNewTab(sublime_plugin.EventListener):

	def on_deactivated(self, view):
		if view.name() == 'Find Results':
			# set a name with space
			# so it won't be bothered
			# during new search
			view.set_name(alt_name)

	# these hooks will help other plugins
	# to understand that we are in search results file
	def on_text_command(self, view, command_name, args):
		if view.name() == alt_name:
			view.set_name(default_name)

	def post_text_command(self, view, command_name, args):
		if view.name() == default_name:
			view.set_name(alt_name)
