import codecademylib3_seaborn
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 8
#intercept:
b = 65

plt.plot(months, revenue, "o")

y = [m*r + b for r in months]
plt.plot(months, y)

plt.show()

def get_gradient_at_b(x, y, m, b): 
  diff = 0 
  N = len(x) 
  for i in range(0, len(x)): 
    y_val = y[i] 
    x_val = x[i]
    diff += (y_val - ((m * x_val) + b)) 
    
  b_gradient = -2/N * diff
  return b_gradient
