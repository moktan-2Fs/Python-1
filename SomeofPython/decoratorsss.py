# decorators are funcitons that decorate and enhance the base function that 
# we pass as arguments, it takes function as parameters
#   @something is used before a function to imply that the function below
# is to be decorated with the @function

# in programming a function should focus on a single well defined
# responsibility to make code reusable


# for functions with no paramerters 

# import time

# def timer_dec(base_fn):
#     def enhanced_fn():
#         st_time = time.time()
#         base_fn()
#         ed_time = time.time()
#         print(f'Task time: {(ed_time-st_time):.2f}s')
#     return enhanced_fn

# @timer_dec
# def brew_tea():
#     print("Brewing tea.....")
#     time.sleep(1)
#     print("Tea is ready.....")

# brew_tea()

# # dec_brew_tea = timer_dec(brew_tea) # one of the ways of calling decorators in python 
# # dec_brew_tea() # while passing a funcition as parameter only function name is used 

# # # also
# # brew_tea = timer_dec(brew_tea) # same as above but name is of base function
# # brew_tea()

# # @timer_dec
# # def make_pasta():
# #     print("Making pasta....")
# #     time.sleep(1)
# #     print("your pasta is ready...")

# # make_pasta()

# for functinos with parameters 

import time

def timer_dec(base_fn):
    def enhanced_fn(*args,**kwargs):
        st_time = time.time()
        base_fn(*args,**kwargs)
        ed_time = time.time()
        print(f'Task time: {(ed_time-st_time):.2f}s')
    return enhanced_fn

@timer_dec
def brew_tea(tea_type):
    print(f"Brewing {tea_type}tea.....")
    time.sleep(1)
    print(f"{tea_type} tea is ready.....")

brew_tea("milk")

# dec_brew_tea = timer_dec(brew_tea) # one of the ways of calling decorators in python 
# dec_brew_tea() # while passing a funcition as parameter only function name is used 

# # also
# brew_tea = timer_dec(brew_tea) # same as above but name is of base function
# brew_tea()

@timer_dec
def make_pasta():
    print("Making pasta....")
    time.sleep(1)
    print("your pasta is ready...")

make_pasta()