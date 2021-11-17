#a class that stores methods to compute any boring
#statistics problems that we would otherwise be doing by hand

import math

class Stats_Calc:
    
    #constructor, turns our set of numbers into list of numbers,
    #also computes average for ease of use
    def __init__(self,numbers):
        if numbers is not None:
            self.numbers = numbers.split(",")
            count = 0
            sum = 0
            for i in self.numbers:
                sum += int(i)
                count += 1
            self.avg = (sum / count)
    
    #calculating range
    def range_calc(self):
        """
        Calculates the range of a set of numbers.
        Parameters: 
            None
        Returns:
            result- the range of the numbers
        """
        
        result = int(max(self.numbers)) - int(min(self.numbers))
        return result

    def MAD(self):
        """
        Calculates the mean abololute deviation of a 
        set of numbers.
        Parameters:
            None
        Returns:
            result- the mean absolute deviation of the 
            number
        """
        result = 0
        total = 0
        #computing the average of the set of numbers
        for i in self.numbers:
            total += int(i)
        avg = total / len(self.numbers)

        #now computing MAD
        tot1 = 0.0
        for j in self.numbers:
            tot1 += abs(int(j) - avg)
        Mad = tot1 / len(self.numbers)
        
        return Mad

    def pop_var(self):
        """
        Calculates the population variance
        of a set of numbers.
        Parameters:
            None
        Returns:
            result- the population variance of the set
            of numbers
        """
        sqr_tot = 0
        norm_tot = 0
        for i in self.numbers:
            sqr_tot += (int(i))**2
            norm_tot += int(i)
        
        pop_var_result = (sqr_tot - ((norm_tot**2) / len(self.numbers))) / len(self.numbers)

        return pop_var_result

    def pop_StdDev(self):
        """
        Calculates the population standard
        deviation of a set of comma delimited numbers
        Parameters:
            None
        Returns:
            pop_std_dev- pop standard deviation
        """
        #getting population variance
        sqr_tot = 0
        norm_tot = 0
        for i in self.numbers:
            sqr_tot += (int(i))**2
            norm_tot += int(i)
        
        pop_var_result = (sqr_tot - ((norm_tot**2) / len(self.numbers))) / len(self.numbers)

        #computing stdDev
        result = math.sqrt(pop_var_result)
        
        return result

    def z_scores(self):
        """
        Calculates the x-scores for
        a set of numbers
        Parameters:
            None
        Returns:
            z-scores: a list of the corresponding
            z-scores for each number in the set
        """
        #calculating avg
        total = 0
        for i in self.numbers:
            total += int(i)
        avg = total / len(self.numbers)
        
        #getting population variance
        sqr_tot = 0
        norm_tot = 0
        for i in self.numbers:
            sqr_tot += (int(i))**2
            norm_tot += int(i)
        
        pop_var_result = (sqr_tot - ((norm_tot**2) / len(self.numbers))) / len(self.numbers)
        
        #compiling list of z-scores
        z_score_list = []
        for j in self.numbers:
            individual = []
            individual.append(int(j))
            z_score = (int(j) - avg) / pop_var_result
            individual.append(z_score)
            z_score_list.append(individual)
        
        return z_score_list  

    def pop_coef_var(self):
        """
        Calculates the population coefficient
        of variation from a set of numbers.
        Parameters:
            None
        Returns:
            result - pop coef variation
        """
        #calculating sum of numbers in the set
        sum_x = 0
        sum_x_sqrd = 0
        j = 0
        for i in self.numbers:
            sum_x += int(i)
            sum_x_sqrd += (int(i)) ** 2
            j += 1
        #computing result    
        PSD = math.sqrt((sum_x_sqrd - ((sum_x ** 2) / j)) / j)
        result = (PSD / self.avg) * 100
        
        return result

class Discrete_Distribution:
    #handles a different type of distribution for stats,
    #is slightly more complicated

    def __init__(self,x,p):
        """
        Constructor for discrete distribution class.
        Parameters:
            x: x portion of discrete number distribution
            p: the probability the corresponding x-value
            being that number.
        Returns:
            None
        """
        if (x is not None and p is not None):
            self.x = x.split(",")
            self.p = p.split(",")
            #have to do a different type of computation to
            #get the mean for this type of distribution
            total = 0
            self.avg = 0
            for i in range(len(self.x)):
                self.avg += ((int(self.x[i])) * float(self.p[i]))
        return

    def _variance(self):
        """
        Helper method to compute variance for standard deviation.
        To be used within class only.
        """
        variance = 0
        for i in range(len(self.x)):
            variance += ((int(self.x[i]) - self.avg)**2 * float(self.p[i]))
        
        return variance
    
    def variance(self):
        """
        Computes variance.
        """
        variance = 0
        for i in range(len(self.x)):
            variance += ((int(self.x[i]) - self.avg)**2 * float(self.p[i]))
        
        return variance

    def std_dev(self):
        """
        Computes standard deviation.
        """
        computation = self._variance()
        result = math.sqrt(computation)
        
        return result

    def binomial_single(self,N,P,X):
        """
        Computes the probabilty of an event using
        the binomial formula for a single value of x.
        Helper method, used only within class.
        Parameters:
            int N- number of outcomes
            float P- the probability of the event happening
            int X- the actual number we are computing the probability of.
        Returns:
            p(x)- the answer
        """
        P = float(P)
        N = int(N)
        X = int(X)
        q = 1.0 - P
        return (math.factorial(N) / (math.factorial(X) * math.factorial(N-X))) * (P**X) * (q**(N-X))

    def poisson_solver(self,x,lam):
        """
        Computes values using poisson formula.
        """
        x = int(x)
        lam = float(lam)
        result = ((lam**2) * (math.exp(-abs(lam)))) / math.factorial(x)
        return result
       
        
        

        
