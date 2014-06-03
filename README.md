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

<h2>tokitou.girl</h2>
<pre>
###
张一苇自恋
TokiTou v1.0.1
Copyright 2014 TokiTou, Inc.
Licensed under http://www.apache.org/licenses/LICENSE-2.0
###

@main_backgroud_color = White
@c51 = rgb(51,51,51)
@body_width = 1000px
@long_col = 70%
@short_col = 30%
@padding_left_right_col = 12px


######Face to All###

body {
    background-color: @main_background_color;
    color: @c51;
    }


######TokiTou Theme###

.nav_bar {
    width: @body_width;
    background-color: Blue;
    border-bottom: 1px solid;
    border-color: Green;
    padding-left: 0px;
    padding-right: 0px;
    }

.main_box {
    width: @body_width;
    }
    
.long_box {
    width: @long_col;
    float: left;
    text-align: left;
    padding-left: @padding_left_right_col;
    padding-right: @padding_left_right_col;
    }
    
.short_box {
    width: @short_col;
    float: left;
    text-align: left;
    padding-left: @padding_left_right_col;
    padding-right: @padding_left_right_col;
    }
</pre>

<h2>tokitou.css</h2>
<pre>
/*!
 *张一苇自恋
 *TokiTou v1.0.1
 *Copyright 2014 TokiTou, Inc.
 *Licensed under http://www.apache.org/licenses/LICENSE-2.0
 */



/*! ###Face to All### */

body {
    background-color: @main_background_color;
    color: rgb(51,51,51);
    }


/*! ###TokiTou Theme### */

.nav_bar {
    width: 1000px;
    background-color: Blue;
    border-bottom: 1px solid;
    border-color: Green;
    padding-left: 0px;
    padding-right: 0px;
    }

.main_box {
    width: 1000px;
    }
    
.long_box {
    width: 70%;
    float: left;
    text-align: left;
    padding-left: 12px;
    padding-right: 12px;
    }
    
.short_box {
    width: 30%;
    float: left;
    text-align: left;
    padding-left: 12px;
    padding-right: 12px;
    }
</pre>
