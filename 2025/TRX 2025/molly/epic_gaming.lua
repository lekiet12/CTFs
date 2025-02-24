local function a(b)
    local c={}
    b=b:sub(5,-2)
    for d in string.gmatch(b,"[^_]+")
        do table.insert(c,d)
    end;
        return c 
    end;
local function e(f)
    if#f~=4 then 
        return 1 
    end;
        local g=100;
        local h=51;
        local i=64;
        local j=114;
        if string.char(g,h,i,j)~=f then return 1 
        end;return 0 end;
    local k=a(flag)
    local l=epic_gaming2(k[1])
    l=l+e(k[2])
    l=l+epic_gaming3(k[3])
    l=l+epic_gaming1(k[4])
    return l
