class Solution:
    def totalFine(self, date, car, fine):
        total = 0
        
        for i in range(len(car)):
            if (car[i] % 2) != (date % 2):
                total += fine[i]
        
        return total