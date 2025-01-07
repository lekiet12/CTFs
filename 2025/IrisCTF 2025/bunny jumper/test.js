r = "irisctf{this_is_a_fake_flag}"
f = { d: 2, e: 2, u: 3, f: 3, i: 3, n: 3 }
l = Object.entries(f).sort(((r, f) => r[1] - f[1] || r[0].localeCompare(f[0]))), C = 27489;
console.log(l);