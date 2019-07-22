# StatSeeker
Statistical testing system for analysing the contents of directories using Ent (John Walker), FIPS 140-2 (NIST), and SP800-22 (aka STS 2.1.2 - NIST).

This tool is in the prototype phase and is far from user friendly, but I hope that the following steps will help. I have onlytested this on Ubuntu 18.04.

SETUP

Clone this repo to the directory of your choosing, then cd into the sts-2.1.2 directory and make the program. You will need the latest gcc compiler on your machine for this. 
This step is required for SP800-22 to function correctly.

You should also use pip3 (Python3) to install the following packages: numpy, scipy, and pandas.

You should now be ready to use StatSeeker by typing: python3 StatSeeker --path test_dir/

The minimum file size that can be tested with this tool is 62.5KB. The selected directory will be scanned in its entirety - prepare your samples for testing ahead of time to prevent extremely long execution times. Only SP800-22 is threaded (original NIST implementation) at this time. All other tests execute on a single thread. 

Default parameters for the tests are;

Ent operates over the entire length of the file in bytes mode
FIPS 140-2 will perform 1000 iterations of 20,000-bits, discarding the first 31-bits of each file. If the file is not large enough for this, the file size will dictate the total iterations. 
SP800-22 tests 50,000-bit sequences for 10 iterations. This is substantially lower than the advised settings, and is currently being tested to determine if it is suitable. 

The output csv contains all statistical output of these tests. SP800-22 output is the most complex. For every test, SP800-22 outputs a p-value of the 10 streams tested and a proportion test result. p-values of '---' indicate insufficient stream counts to compute an accurate p-value (RandomExcursions test will report this). So for each test, a list (1 result for each iteration/version of the test performed) is generated containing [p-value, proportion] = eg [0.8453, 10/10]. 

A final statistics.csv file is generated and placed in the results sub-directory alongside all individual test results. 
