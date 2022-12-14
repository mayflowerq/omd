class Color:
	END = '\033[0'
	START = '\033[1;38;2'
	MOD = 'm'

	def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
		if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
			raise ValueError('Incorrect input')
		self.rgb = (red, green, blue)

	def __repr__(self):
		return (
			f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}{self.MOD}'
			f'●'
			f'{self.END}{self.MOD}'
		)

	def __eq__(self, other):
		if not isinstance(other, self.__class__):
			return False
		return self.rgb == other.rgb

	def __add__(self, other):
		return Color(min(255, self.rgb[0] + other.rgb[0]), min(255, self.rgb[1] +
								other.rgb[1]), min(255, self.rgb[2] + other.rgb[2]))

	def __hash__(self):
		return hash(self.rgb)

	def __mul__(self, c: float):
		if not 0 <= c <= 1:
			raise ValueError('Contrast must be between 0.0 and 1.0.')
		cl = 256 * (c-1)
		F = 259 * (cl + 255) / 255 / (259 - cl)
		return Color(*(int(F * (color - 128)) + 128 for color in self.rgb))

	def __rmul__(self, c: float):
		return self.__mul__(c)


if __name__ == '__main__':
	orange1 = Color(255, 165, 0)
	red = Color(255, 0, 0)
	green = Color(0, 255, 0)
	orange2 = Color(255, 165, 0)
	color_list = [orange1, red, green, orange2]
	print(set(color_list))
	print(red, red * 0.5, 0.5 * red)
