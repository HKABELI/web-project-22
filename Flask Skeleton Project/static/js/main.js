



togglestatus=1
        function openNavi() {
            if (togglestatus == 1) {
                document.getElementById("subYoga").innerHTML = ` 
                  <li class= "sub-link" ><a  class= "sub-links"  href="///////yoga.html"" target='_blank'>יוגה</a> </li>
                  <li class= "sub-link" > <a  class= "sub-links" href=Flask.url_for('pranayama', {}) target='_blank' "> אסנה </a></li>
                  <li class= "sub-link"><a   class= "sub-links" href="{{ url_for('templates', filename='meditation.html' )}}" target='_blank'> מדיטציה</a> </li>
                  <li class= "sub-link"><a  class= "sub-links" href="{{ url_for('pranayama')}}" target='_blank'> פרנימה</a> </li>
                                                             `;
                togglestatus=2;
            }

             if (togglestatus == 2)
            {
                document.getElementById("subYoga").innerHTML= ``;
                 togglestatus=1;

            }
            }

   function CloseNavi(x) {
                  document.getElementById("subYoga").innerHTML = ` 
                                                             `;
            }
