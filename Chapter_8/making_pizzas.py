#Ryan McDowell
#8/5/21
#Practicing importing a module and referencing a function in it.

#import pizza_module

# from pizza_module import make_pizza as mp

# import pizza_module as pm

from pizza_module import *

# pizza_module.make_pizza('16', 'cheese')
# pizza_module.make_pizza('15', 'ham', 'turkey', 'pepperoni')

# mp('16', 'cheese')
# mp('15', 'ham', 'turkey', 'pepperoni')

# pm.make_pizza('16', 'cheese')
# pm.make_pizza('15', 'ham', 'turkey', 'pepperoni')

make_pizza('16', 'cheese')
make_pizza('15', 'ham', 'turkey', 'pepperoni')