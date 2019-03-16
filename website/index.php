<html>
<head><title>Expat Audio Inventory</title></head>
<body>


<?php

// Add menu bar
include('topbar.php');


// connect to the database

include('-dbconnect.php');

 
// $sql = "SELECT 'Record ID', 'Description' FROM 'TABLE 1' WHERE 1";
$sql = "SELECT * FROM `TABLE 1`";
$result = $conn->query($sql);
?> 

<!-- // close this PHP bit -->

<center>

<?php
if ($result->num_rows > 0) {
    // echo '<table border="1" cellpadding="0" cellspacing="0">';
    echo '<table border="1" class="blueTable">';
    echo '<thead>
			<tr>  <th>Record ID:</th>
                <th>Product ID</th>
		<th>Sample Storage ID</th>
		<th>Type</th>
		<th>Man P/N</th>
		<th>Manufacturer</th>
		<th>Value</th>
		<th>Package</th>
		<th>Description</th>
		<th>Picture</th>
		<th>View More</th>
		</thead>
		</tr>';// output data of each row
    while($row = $result->fetch_assoc()) {
		
		
		$rowid = $row["Record ID"];
		$image = $row["Picture Link"];
	
		
	
        echo'<tr>';
        echo '<td>', $row["Record ID"], '</td>';
        echo '<td>', $row["Product ID"], '</td>'; 
      
 
		// this was a HOG of a line to debug.
		//Single and Double quotes are a pain to add. onclick needs to be in double quotes
		//but you can only use one at a time, so the html has to be broken down (As you can see below), single quotes are encapsulated 
		// in a pair of double quotes.
		
		echo '<td> <button onclick="inventorywebsocket(', "'", $row["Sample_Storage_ID"], "')", '">', $row["Sample_Storage_ID"], "</button></td>";		 
		
		
		// echo '<td>', $row["Sample_Storage_ID"], '</td>'; 
        echo '<td>', $row["Type"], '</td>';
        echo '<td>', $row["Man P/N"], '</td>';
        echo '<td>', $row["Manufacturer"], '</td>';
        echo '<td>', $row["Value"], '</td>';       
        echo '<td>', $row["Package"], '</td>';
        echo '<td>', $row["Description"], '</td>';
		
		// insert picture
		echo '<td>' ;
		echo "<img width=100 src='";
		echo $image;
		echo "' >";
		echo '</td>';
		
		// insert link to view all details
		echo '<td>' ;
		echo "<a href='viewsingle.php?id=";
		echo $rowid;
		echo "' >";
		echo "All Details";
		echo "</a>";
		echo '</td>';
        echo '</tr>';
		echo "\r\n";
    }
    echo '</table></br>';
} else {
    echo "0 results";
}
$conn->close();
?>

</center>

</body>
</html>
