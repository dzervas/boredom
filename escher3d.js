function parse() {
	var data = document.getElementById("all-probe-data").value;
	var regex = /Bed X: ([0-9.-]+) Y: ([0-9.-]+) Z: ([0-9.-]+)/g;
	var buff;
	var probedata = [];
	
	while((buff = regex.exec(data)) !== null) {
		probedata.push([buff[1], buff[2], buff[3]]);
	}
	
	document.getElementById("numPoints").value = probedata.length;
	setPoints();
	
	for (var i = 0, len = probedata.length; i < len; i++) {
		document.getElementById("probeX" + i).value = probedata[i][0];
		document.getElementById("probeY" + i).value = probedata[i][1];
		document.getElementById("probeZ" + i).value = probedata[i][2];
	}
}

document.getElementById("suggestButton").outerHTML = "<tr><textarea id='all-probe-data'></textarea><button type='button' onclick='parse()'>Go</button></tr>" + document.getElementById("suggestButton").outerHTML; 