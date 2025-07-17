# Python Data Types
# Built-in Data Types:-

# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:
'''
        Text Type: 	        str
        Numeric Types:	        int, float, complex  
        Sequence Types:	        list, tuple, range
        Mapping Type:	        dict
        Set Types:	        set, frozenset
        Boolean Type:	        bool
        Binary Types:	        bytes, bytearray, memoryview
        None Type:	        NoneType
'''
#///////////////////////////////////
        
# Setting the Data Type:-

# In Python, the data type is set when you assign a value to a variable:
# Example :-
'''
a = "Hello World"	                                    str	
b = 20	                                                    int	
c = 20.5                	                            float	
d = 1j	                                                    complex	
e = ["apple", "banana", "cherry"]          	            list	
f = ("apple", "banana", "cherry")	                    tuple	
g = range(6)	                                            range	
h = {"name" : "John", "age" : 36}	                    dict	
i = {"apple", "banana", "cherry"}	                    set	
j = frozenset({"apple", "banana", "cherry"})	            frozenset	
k = True , False                                            bool	
l = b"Hello"	                                            bytes	
m = bytearray(5)	                                    bytearray	
n = memoryview(bytes(5))	                            memoryview	
o = None	                                            NoneType
'''

#///////////////////////////////////

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

# Example	:-
'''
a = "Hello World"	                                                str	
b = 20	                                                                int	
c = float(20.5)	                                                        float	
d = complex(1j)	                                                        complex	
e = ["apple", "banana", "cherry"]	                                list	
f = tuple(("apple", "banana", "cherry"))	                        tuple	
g = range(6)	                                                        range	
h = dict(name="John", age=36)	                                        dict	
i = set(("apple", "banana", "cherry"))	                                set	
j = frozenset(("apple", "banana", "cherry"))	                        frozenset	
k = bool(5)	                                                        bool	
l = bytes(5)	                                                        bytes	
m = bytearray(5)	                                                bytearray	
n = memoryview(bytes(5))	                                        memoryview
'''

#///////////////////////////////////