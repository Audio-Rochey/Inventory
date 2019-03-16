<!-- This is where the top menu part of the page lives, and where I keep the Javascript for the websockets -->

<html>
<head> <link rel="stylesheet" type="text/css" href="mytable.css">

<script type = "text/javascript" >
    function inventorywebsocket(message) {

        if ("WebSocket" in window) {

            // Let us open a web socket
            var ws = new WebSocket("ws://192.168.1.180:80");

            ws.onopen = function() {

                // Web Socket is connected, send data using send()
                ws.send(message);
                alert(message);
                //ws.close();
            };

            ws.onmessage = function(evt) {
                var received_msg = evt.data;
                alert("I got data: " + evt.data)
                if (evt.data = "disconnect") { // this waits for the server to send a message back to discueect
                    ws.close();
                }
            };



            ws.onclose = function() {

                // websocket is closed.
                //alert("Connection is closed..."); 
            };
        } else {

            // The browser doesn't support WebSocket
            alert("WebSocket NOT supported by your Browser!");
        }
    } </script>






</head>
<body>
<!--// <center><h1>Expat Audio Inventory Viewer</h1>
// <img src="http://www.expataudio.com/expatwiki/images/d/d5/Logo135by135.png"></Center>
-->

<table style="width: 80%; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="width: 20%;">&nbsp;</td>
<td style="vertical-align:top">

<h1>Expat Audio Inventory Viewer</h1>
<form action="viewsingle.php" method="get">
<p> <a href="index10.php"> Index </a> : <a href="exportlabels.php">Export Labels</a> : PIDLookup

<!-- dd form for updating storageID -->

<input type="text" name="id" value=""/>
<!-- <strong>Last Name: *</strong> <input type="text" name="lastname" value="<?php echo $lastname; ?>"/><br/>
-->
<input type="submit" name="submit" value="Submit">

</form>
</P>



</td>
<td style="width:135px;"><img src="http://www.expataudio.com/expatwiki/images/d/d5/Logo135by135.png"></td>
<td style="width: 20%;">&nbsp;</td>
</tr>
</tbody>
</table>
<!-- DivTable.com -->


</body>
</html>
