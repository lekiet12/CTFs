llc -filetype=asm warmup.ll -o warmup.s -opaque-pointers 
as -o warmup.o warmup.s
gcc -o warmup warmup.o -no-pie
