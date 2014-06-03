#coding=utf-8
dic = {}
switch = '' # None means not a label, # means a label.

def tokitou(input_name):
    
    global dic
    
    #闭包：是否有@
    def get_arg():
        if line[0] == "@":
            line_no_space = line.replace( ' ', '' )
            index_equal = line_no_space.index( '=' )
            key = line_no_space[ :index_equal ]
            value = line_no_space[ index_equal+1:]
            dic[ key ] = value[:-1] #delete \n
            return True
        else: return False

    #闭包：判断是否是注释、替换@
    def compiler( line_change ):
        global switch
        
        #before compiler it should be tested
        #whether this sentense is a label
        if line_change[:3] == "###":
            if len( line_change ) > 4:
                return "/*! {} */\n".format( line_change[3:-1] )
            else:
                if switch == '':
                    switch = '#'
                    return "/*!\n"
                else:
                    switch = ''
                    return " */\n"
        if switch == '#':
            return " *{}".format( line_change )
    
        for k,v in dic.iteritems():
            line_change = line_change.replace( k, v )
        return line_change
    
    #tokitou核心代码开始
    
    #get the output name from input name
    output_name = "{}.css".format( input_name[:input_name.index('.')] )
    
    #open the input file
    input_file = open( input_name )
    all_lines = input_file.readlines()
    input_file.close()
    
    #if disget arg then compiler
    result_lines = []
    for line in all_lines:
        if not get_arg():
            result_lines.append( compiler(line) )
    
    #write the output file
    output_file = open( output_name, "w" )
    output_file.writelines( result_lines )
    output_file.close()

if __name__ == "__main__":
    tokitou("tokitou.girl")
