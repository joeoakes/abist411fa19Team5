import app2Phase2

# content of test_class.py
class TestClass:
	def test_app(benchmark):
		x = True
		result = benchmark(x)
		assert result == True

