import frida
import time

device = frida.get_usb_device()
print("Device connected:", device)

package_name = "com.n1ctf2024.ezapk"

pid = device.spawn([package_name])
session = device.attach(pid)
device.resume(pid)
time.sleep(1)  

hook_script = """
Java.perform(function() {
    var StringClass = Java.use('java.lang.String');
    // Hook phương thức equals của lớp String để luôn trả về true
    StringClass.equals.implementation = function(other) {
        var currentString = this.toString();
        var otherString = other.toString();       
        
        if (otherString === "iRrL63tve+H72wjr/HHiwlVu5RZU9XDcI7A=") {
            console.log('Hooked equals: Comparing "' + currentString + '" with "' + otherString + '"');
            return true; 
        }
        
        return this.equals(other);
    };
});
"""

script = session.create_script(hook_script)
script.load()

print("Hook script loaded. Press Ctrl+C to exit.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
    session.detach()
