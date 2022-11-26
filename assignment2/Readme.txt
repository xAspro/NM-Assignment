For question2 e part
There are 5 methods to solve.

I am skipping 3 of them for sure, because I was told anything too direct because of use of external aids is not allowed, so one of it I cant do. 
And other is very depricated form of programming. It uses the fact the question asks only for very veryyy specific thing. So skipping that too. 
Note: even the other original method I did actually uses the fact to compensate for time. But otherwise, if given enough time and memory, it can do it for any general arguments though.


So the 5 methods are.

i) one using inbuilt polynomial definition in python. That way I can just directly use polynomial addition and multiplication to find L_i and in the end, express the determined approximate function as a polynomial directly
ii) one using the idea that we just need 4 equations because 4 variables and hence can directly just calculate coeff of x^n and coeff of x^n-1 and x^1 and x^0 by summation of product of roots.

iii) One using lists and expanding the products in each L_i and getting the final polynomial(Note: here, I am not finding the whole polynomial but just the coeffs of few degrees, because of time and memory complexity. But this code can indeed find it though)
iv) One using string representation and expanding the equation by actually solving the operations one by one in terms of strings(using string to compensate for the problem of not having an operatable f(x) in python), but Note: this still can do normal expression calculations easily. But requires extra effort to group same terms of powers together and get a simple looking expression. 
v) Using my own definition of a list for a polynomial and working using that