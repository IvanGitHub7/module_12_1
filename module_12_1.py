import unittest
import runner

#Создаем класс для тестов:
    
class RunnerTest(unittest.TestCase):
    
#Создаем тест работы функции 'walk' относительно рассчитанного значения:
    
    def test_walk(self):
        first_walker = runner.Runner('Bob')
        for i in range(10):
            runner.Runner.walk(first_walker)
        distance_first_walker = first_walker.distance
        self.assertEqual(distance_first_walker, 50, 'Fail')

#Создаем тест работы функции 'run' относительно рассчитанного значения: 
                               
    def test_runner(self):
        first_runner = runner.Runner('Petr')
        for i in range(10):
            runner.Runner.run(first_runner)
        distance_first_runner = first_runner.distance
        self.assertEqual(distance_first_runner, 100, 'Fail')
       
#Создаем тест работы функций 'walk' и 'run' относительно друг друга:
          
    def test_challenge(self):
        sec_walker = runner.Runner('Vasya')
        for i in range(10):
            runner.Runner.walk(sec_walker)
        distance_sec_walker = sec_walker.distance
        sec_runner = runner.Runner('Georgy')
        for i in range(10):
            runner.Runner.run(sec_runner)
        distance_sec_runner = sec_runner.distance
        self.assertNotEqual(distance_sec_walker, distance_sec_runner, 'Fail')
        
#Запускаем код при условии, что он запущен из модуля тестирования:

if __name__ == '__main__':
    unittest.main()