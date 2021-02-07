        function openNav() {
        document.getElementById("mySidenav").style.width = "500px";
        document.body.style.marginRight = "300px";
        document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
        document.getElementById("headLogo").style.backgroundColor = "#e6e6e6";
        }

        function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
        document.body.style.marginRight= "0";
        document.body.style.backgroundColor = "white";
        document.getElementById("headLogo").style.backgroundColor = "#e9e2e6";
        }

     //
     // var togglestatus=1;
     //    function openNavi(){
     //        if(togglestatus==1){
     //         document.getElementById("subYoga").innerHTML= `
     //                        <"li class= "sub-link" > <a  class= "sub-links"  href="{{ url_for('Yoga.index') }} >יוגה</a> </li>
     //                        <"li class= "sub-link" > <a  class= "sub-links"  href="{{ url_for('Asana.index') }} >אסנה</a> </li>
     //                        <"li class= "sub-link"> <a   class= "sub-links" href="{{ url_for('Exercises.index') }}> מדיטציה</a> </li>
     //                        <"li class= "sub-link"> <a   class= "sub-links" href="{{ url_for('Pranayama.index') }}> פראניאמה </a> </li>
     //
     //                  `;
     //
     //
     //        togglestatus=2;
     //        }
     //        else
     //        {
     //            document.getElementById("subYoga").innerHTML= ``;
     //             togglestatus=1;
     //
     //        }
     //        }
     //
     //
     //            document.getElementById("subYoga").innerHTML = `
     //
     //
