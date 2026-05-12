import pytest

from src.calculations import Calculations

# object created to access
class TestCalculations:
    calc = Calculations()

    # @pytest.fixture(scope='class',autouse=True)
    # def setup(self):
    #     print('Fixture')

    @pytest.mark.parametrize("n1,n2,ex",
                             [(5,5,10),(-5,-5,-10),(0,5,5)])
    def test_add(self, n1,n2,ex):
        res = self.calc.add(n1,n2)
        assert res == ex, 'Addition Err'

    @pytest.mark.parametrize("n1,n2,ex",
                                 [(5, 5, 0), (-5, -5, 0), (0, 5, -5)])
    def test_sub(self,n1,n2,ex):
        res = self.calc.sub(n1,n2)
        assert res == ex, 'Subtraction Err'

    def test_mul(self):
        res = self.calc.mul(10,5)
        assert res == 50, 'Multiplication Err'


    def test_div(self):
        res = self.calc.div(10,5)
        assert res == 2, 'Division Err'

    @pytest.mark.skip
    def test_ne(self):
        res = self.calc.ne(10,10)
        assert res == True, 'NOT Equal'

    @pytest.mark.xfail(reason='Exception not handled!')
    def test_driver(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(10,0)
