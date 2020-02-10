def solution(brown, red):
    for r in range(1,red+1):
        if red%r == 0:
            r_width = red//r
            r_height = r
            b_width = r_width+2
            if brown-((b_width*2)+(r_height*2)) == 0:
                return [b_width,r_height+2]
