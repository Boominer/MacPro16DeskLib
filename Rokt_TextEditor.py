class TextEditor: 
	def __init__(self):
		self.text_stack = []      	# main content stack
		self.delete_stack = [] 		# delete contrent for undo
		self.snapshot = {}			
		self.snapshot_id = 0 

	def add_text(self, text):
		if self.text_stack:
			self.text_stack.append(self.text_stack[-1] + text)
		else:
			self.text_stack.append(text)
		self.delete_stack.clear()

	def delete_text(self):
		current = self.text_stack[-1]	
		prev = self.text_stack[-2]
		self.delete_stack.append(self.text_stack.pop()[len(prev):])

	def undo_delete(self):
		if self.delete_stack:
			self.text_stack.append(self.text_stack[-1] + self.delete_stack.pop())

	def take_snapshot(self):
		self.snapshot[self.snapshot_id] = self.text_stack[-1]
		self.snapshot_id += 1 
		return self.snapshot_id - 1

	def restore_snapshot(self, snapshot_id):
		if snapshot_id in self.snapshot: 
			self.text_stack.append(self.snapshot[snapshot_id])
			self.delete_stack.clear()

	def get_text(self):
		return self.text_stack[-1]



editor = TextEditor()
editor.add_text("hello")
editor.add_text(" world")
print(editor.get_text())  # "hello world"

editor.delete_text()
print(editor.get_text())  # "hello"

editor.undo_delete()
print(editor.get_text())  # "hello world"

snap = editor.take_snapshot()
editor.delete_text()
editor.restore_snapshot(snap)
print(editor.get_text())  # "hello world"