# program-compare

This is a program-comparator for programming competition. It's base on `cyaron`, but some simple encapsulation was made.

When the class `ProgramCompare` was built, you can appoint the `std_cpp` path and the `cmp_cpp` path.
And it is important to `setData` methods, it is a function object for making data according to the problem.
Of course you can set some compile parameter by `compiler` `std` and `optimize`.Then it will compile the source code to exe.

There are 6 methods in this class.

* `osCompare` means using `os.popen()` to get the output from two exe files and comparing the text of two.
* If you only want to gain `test.in` and `test.out` as data from `std_exe`, you can use `makeData`
* `osCompare` is similar as `osCompare`, but it use senior comparator. For example, it can ignore some space ` ` ,tab `	` and line feed `\n` .
* I guess you must have been troubled by overflow errors. So `lower_bound` is made. It names reference c++. It can binary Search the lower bound of overflow. 
* If you want to make many tests at a time, try `run` .
* Finally, to clear the temporary file, `clear` !
