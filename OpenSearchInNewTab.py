import sublime_plugin

class OpenSearchInNewTab(sublime_plugin.EventListener):
	def on_deactivated(self, view):
		if view.name() == 'Find Results':
			# set a name with space
			# so it won't be bothered
			# during new search
			view.set_name('Find Results ')