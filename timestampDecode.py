import sublime, sublime_plugin, pytz, time
from datetime import datetime
from calendar import timegm

class TimestampEncodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		i_panel = self.view.window().show_input_panel(
			# caption
			"Date format string:",
			# initial_text
			"%Y/%m/%d %H:%M:%S",
			# on_done
			self.convert,
			# on_change (unused)
			None,
			# on_cancel
			self.convert
		)

		i_panel.sel().clear()
		i_panel.sel().add(sublime.Region(0, i_panel.size()))
	def convert(self, format):
		self.view.run_command(
			'timestamp_encode_real',
			{'format': format}
		)

class TimestampDecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		i_panel = self.view.window().show_input_panel(
			# caption
			"Date format string:",
			# initial_text
			"%Y/%m/%d %H:%M:%S",
			# on_done
			self.convert,
			# on_change (unused)
			None,
			# on_cancel
			self.convert
		)

		i_panel.sel().clear()
		i_panel.sel().add(sublime.Region(0, i_panel.size()))
	def convert(self, format):
		self.view.run_command(
			'timestamp_decode_real',
			{'format': format}
		)

class TimestampDecodeRealCommand(sublime_plugin.TextCommand):
	def run(self, edit, format):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s)

			timestamp = 0

			try:
				timestamp = float(selected)
				if timestamp > 31536000000:
					timestamp = timestamp / 1000
				txt = datetime.fromtimestamp(timestamp, tz=pytz.utc).strftime(format)
			except ValueError:
				txt = "Invalid timestamp"

			self.view.replace(edit, s, txt)

class TimestampEncodeRealCommand(sublime_plugin.TextCommand):
	def run(self, edit, format):
		for s in self.view.sel():
			if s.empty():
				s = self.view.word(s)

			selected = self.view.substr(s)
			print(selected)
			print(format)

			try:
				txt = str(round(timegm(datetime.strptime(str(selected), format).timetuple())))
			except ValueError:
				txt = "Invalid date string"

			self.view.replace(edit, s, txt)
