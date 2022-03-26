import json
import pathlib 
import shutil
import streamlit as st
import streamlit.components.v1 as components

from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import requests  # pip install requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    



lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_r3rzsy9v.json")




st_lottie(lottie_hello, key = "hello")


st.title("jahoperi Chusconoticias")
st.subheader('')
st.header('5 es menor que 1 ? ----------ó bien')
st.subheader('')
st.header('1 es mayor que 5 ?')
st.subheader('Javier Horacio Pérez Ricárdez')    
st.subheader('')
st.subheader('Maestría en Ciencias de la Computación')
st.subheader('')
st.subheader('Cédula: 5290889')
st.subheader('')
st.subheader('Licenciatura en Matemáticas')
st.subheader('')
st.subheader('Cédula: 4431246')


# HACK This only works when we've installed streamlit with pipenv, so the
# permissions during install are the same as the running process
STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
# We create a videos directory within the streamlit static asset directory
# and we write output files to it
VIDEOS_PATH = (STREAMLIT_STATIC_PATH / "videos")
if not VIDEOS_PATH.is_dir():
    VIDEOS_PATH.mkdir()

uno_video = VIDEOS_PATH / "jahoperi-chusconoticias.mp4"
if not uno_video.exists():
    shutil.copy("jahoperi-chusconoticias.mp4", uno_video)  # For newer Python.



st.subheader('')
st.subheader('')
st.subheader('')




def main():
    components.html("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
.main-div h1
{
 font-size: 21px;
}


#color1{color:red;}
#color2{color:blue;}
#color3{color:pink;}
</style>


  </head>
  <body>
   <div class="main-div">
    <video src = "videos/jahoperi-chusconoticias.mp4" width="500" height="400" controls controlsList="nodownload"></video>
<script type="text/javascript">
//Script for disabling right click on mouse
var message="Function Disabled!";
function clickdsb(){
if (event.button==2){
alert(message);
return false;
}
}
function clickbsb(e){
if (document.layers||document.getElementById&&!document.all){
if (e.which==2||e.which==3){
alert(message);
return false;
}
}
}
if (document.layers){
document.captureEvents(Event.MOUSEDOWN);
document.onmousedown=clickbsb;
}
else if (document.all&&!document.getElementById){
document.onmousedown=clickdsb;
}
document.oncontextmenu=new Function("alert(message);return false")
</script>
</div>
</body>


<p></p>
<p></p>
<p></p>
<p></p>
<p></p>
<p></p>
<p></p>
<p></p>

<FONT FACE="impact" SIZE=6 COLOR="red">
 jahoperi@gmail.com</FONT>
 
 
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 <p></p>
 

</html>""", width=1300, height=550)





if __name__ == "__main__":
    main()
    

