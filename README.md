# [Functions](https://github.com/Ankit-Khule/Functions/blob/master/Functions.py)

* Functions are block of code which runs only when it is called.
* You can pass parameters into the function with the help of arguement
* Paramters are the name within the function while argument is the value passed to that function. 
  eg **def func_name(a)** in here **a** is a parameter which is required for this function to run. while the value which will be passed like func_name(2) is an argument. here **2** is an argument. i.e this function requries one argument to run without any errors.
  return statement is used to return some value if the function is called.
  
  ![example](https://github.com/Ankit-Khule/Functions/blob/master/images/functions.JPG)
  
  Here you can see we have created function add -> to add two values. We have created two parameters a,b. The value 1,2 are the arguments which are required to run this code properly. return statement print the value when the function is called.
  
 
 * Passing List is an argument. 
   ![examplel](https://github.com/Ankit-Khule/Functions/blob/master/images/function%20exampleList.JPG)
   
  * if you are not sure about the number of arguments required for the function you can add \* like def func_name(\*args). this is called arbitary argument
   ![examplea](https://github.com/Ankit-Khule/Functions/blob/master/images/arbitary.JPG)
  
  
  * Recursive function - these are function in which the function calls itself till a certain condition is met. recursive function help in reducing calling the same function again and again.
    * factorial is classic example of recursive function
     ![exampler](https://github.com/Ankit-Khule/Functions/blob/master/images/recursive.JPG)
   In this you can see the func fact(n) is called repeatedly. so the multiplication happens till the number reach 1.
   
   
  ## Map, reduce, filter functions
  * These are short hand function help to reduce the line of code and apply functions to all the items in iterables.
  * It helps in avoiding loops and do it in just a single line of code.
  
  ### Map
  * map(func, iterable)
  * map function is used to apply the func argument to each and every item present in the iterables. Here iterables are the arguments required inside the func.
      ![map](https://github.com/Ankit-Khule/Functions/blob/master/images/map.JPG)
  > Here map function is used to apply function **str.upper** to convert all the values in the list to upper case. 
  
  ### Filter
  * filter(func,iterables)
  * filter function takes only are argument.since it requires only one to filter out the values from the range of values provided.
   ![Filter](https://github.com/Ankit-Khule/Functions/blob/master/images/Filter.JPG)
 
 >  Here we have applied the function muiltpes of 5 to all the values in range(1,100) to filter out which numbers are divisible by 5
  
  ### Reduce
  * reduce(func,iterable[, initial])
  * we need to import reduce from functools
  * reduce passes two arguments at a time to the func. 1st it will pass element 1 and 2 then the output of 1 and 2 will be passed as one element and 3rd element from list.
  * it reduces the number of argumnet by iterating one by one.
  * We can also pass the initial value to the range.
  ![reduce](https://github.com/Ankit-Khule/Functions/blob/master/images/reduce.JPG)
 
   
  ## Lambda Function
  * this is one of the important function.
  * Speciality of lambda func is it is never defined. It is used as short hand to write a func and executed as soon as it is created.
  * Most of the times it is used with map,reduce or filter func. It is called within a func.
  * We will replicate above functions of map,reduce and filter using lambda
    ![lambda](https://github.com/Ankit-Khule/Functions/blob/master/images/lambda.JPG)
  
