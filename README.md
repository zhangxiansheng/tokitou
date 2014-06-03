tokitou
=======

simple css preprocessing via python

It only has two functions.

One is to replace all the arg with "@XXX" at its value.
The other one is use the "###" to mean this is one or several labels to explain something.

How to use tokitou?
Easy.

<h2>Installation</h2>
<pre>
$ pip install tokitou
</pre>

<h2>PreProcessing</h2>
<pre>
$ ls
tokitou.girl

$ python
>>> from tokitou import *
>>> tokitou( "tokitou.girl" )

$ ls
tokitou.girl tokitou.css
</pre>
tokitou.css is the file preprocessed from tokitou.girl via the function of tokitou.
