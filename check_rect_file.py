import write_python


def check_rect(x,y):
    #global past
    #print(past)
    if((x>20 and x<100) and (y>5 and y<60)):
        #print("CAUGHT")
        #past="erase"
        #return "clean"
        write_python.write_file("clean")
    if((x>130 and x<210) and (y>5 and y<60)):
        #print("HEUYU")
        #past="draw"
        #return "eraser"
        
        write_python.write_file("eraser")
    if((x>240 and x<320) and (y>5 and y<60)):
        
        write_python.write_file("green")
    if((x>350 and x<430) and (y>5 and y<60)):
        write_python.write_file("red")

    if((x>470 and x<550) and (y>5 and y<60)):
        write_python.write_file("blue")

    if((x>590 and x<630) and (y>5 and y<60)):
        write_python.write_file("save")
        
    else:
        pass
