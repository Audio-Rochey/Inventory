<html>
<head><title>Expat Audio Inventory Single Item</title>
<link rel="stylesheet" type="text/css" href="mytable.css"></head>
<body>





<?php

// connect to the database

// Add menu bar
include('topbar.php');
echo '<br>';

include('dbconnect.php');


$id = $_GET['id']; # Gets the ID from the URL... e.g. http://2.102.110.219/backup/sandbox.php?id=192


// A whole load of validation and sanitizing to make a PID number into a regular ID number.
//echo 'string in ', $id;
if (filter_var($id, FILTER_VALIDATE_INT) === 0 || !filter_var($id, FILTER_VALIDATE_INT) === false) {
    //echo("Integer is valid");
	//echo '<br>';
} else {
    //echo("Integer is not valid");
	$id = preg_replace( "/[^0-9]/", "", $id );
	//echo '<br>';
	//echo ' ', $id;
}
//echo '<br>';
//echo 'post filter validate and replace char ', $id;
// Trime the zero's off
$id = ltrim($id, '0');
//echo '<br>';
//echo 'post ltrim ', $id;

$sql = "SELECT * FROM `TABLE 1` WHERE `Record ID` = $id "; 
$result = $conn->query($sql);


#`Record ID`, `Product ID`, `Storage ID`, `Type`, 
#`Manufacturer`, `Man P/N`, `Description`, `Temp Coeff`, 

#`accuracy`, `Comment`, `Value`, `Package`, `Quantity`, 
#`Original`, `Real PN`, `price paid (calculate for each)`, 
#`Samples?`, `Datasheet Link`, `Picture Link` 




		 


if ($result->num_rows > 0) {
			
	$row = $result->fetch_assoc(); 		
	echo '<center><button onclick="inventorywebsocket(', "'", $row["Sample_Storage_ID"], "')", '"> Click Here to light up ', $row["Sample_Storage_ID"], "</button></center>";
	echo '
		<table class="blueTable">
		
		<tbody>
		<tr>
		<th>Record ID</td><td>', $row["Record ID"], '</td>
		<th>Description</td><td>', $row["Description"], '</td>
		<th>Quantity in Stock</td><td>', $row["Quantity"], '</td></tr>
		<tr>
		<th>Product ID</td><td>', $row["Product ID"], '</td>
		<th>Temp Coeff`</td><td>', $row["Temp Coeff"], '</td>
		<th>Original?</td><td>', $row["Original"], '</td></tr>
		<tr>
		<th>Sample Storage ID</td><td>', $row["Sample_Storage_ID"], '</td>
		<th>Accuracy</td><td>', $row["accuracy"], '</td>
		<th>Real_PN</td><td>', $row["Real PN"], '</td></tr>
		<tr>
		<th>Type</td><td>', $row["Type"], '</td>
		<th>Comment</td><td>', $row["Comment"], '</td>
		<th>Price (ea)</td><td>', $row["price paid (calculate for each)"], '</td></tr>
		<tr>
		<th>Manufacturer</td><td>', $row["Manufacturer"], '</td>
		<th>Value</td><td>', $row["Value"], '</td>
		<th>Bulk Storage ID</td><td>', $row["Bulk_Storage_ID"], '</td></tr>
		<tr>
		<th>Man P/N</td><td>', $row["Man P/N"], '</td>
		<th>Package</td><td>', $row["Package"], '</td>
		<th>Label Text</td><td>', $row["STORAGELABEL"], '</td></tr>
		</tbody>
		</tr>
		</table> ';
			
			
	
	
	
	
	echo '<center>';
	
	$dsheetlink = $row["Datasheet Link"];
	#echo $dsheetlink;
	echo "<a href='";
	echo $dsheetlink;
	echo "' target='_blank'>";
	echo '<img align=top height=100 src="http://cdn.warer.com/media/Corel-PDF-Fusion-icon-logo.png">';
	echo "</a>";
	
	
	#echo '<BR>';
	
	$image = $row["Picture Link"];
	echo "<img height=200 align=top src='".$image."' /><br />";
	echo '</center>';
	
	#echo "<img src='".$row["Picture Link"]."' />";
}  else {
    echo "0 results";
}
$conn->close();

?>

<table style="width: 80%; margin-left: auto; margin-right: auto;">
<tbody>
<tr>
<td style="width: 20%;">&nbsp;</td>
<td>


</td>
<td style="width: 20%;">&nbsp;</td>


</body>
</html>
