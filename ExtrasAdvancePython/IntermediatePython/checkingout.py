# MRO = Methon Resolution Order-> its the order python follows when lookign for a methond

# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# print(C.__mro__)

# Output -> (C, B, A, object)

# So python serches methods in this order.
# C → B → A → object -> search B class then A class and so on..

# super() -> start loogin for methods after the current class in the MRO

# MRO = (Child, Parent, object)

# super() inside Child means:
#  “Go to the next class after Child → that’s Parent

# The instance created from the child class is used as self for all method calls,
#  and super() ensures that methods in the MRO chain operate on that same object