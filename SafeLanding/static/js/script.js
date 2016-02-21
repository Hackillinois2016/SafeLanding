$(function(){
	$("#butt1").click(function(){
		var airport = $('#apID').val();
		var node = document.getElementById('plswait1');
		node.appendChild(document.createTextNode("Processing your request. This may take a few seconds."));
		$.ajax({
			url: '/searchAirport',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
				var x = Math.random();
				$('#destID').load("static/txt/destFile.txt?" + x);
				node.removeChild(node.lastChild);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
	
	$("#butt2").click(function(){
		var airport = $('#destID').val();
		var node = document.getElementById('plswait2');
		node.appendChild(document.createTextNode("Compliling your data. This may take a few seconds."));
		$.ajax({
			url: '/searchDest',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
				var x = Math.random();
				$.ajax({
					url: "static/txt/diseases.txt?" + x,
					success: function(response){
						console.log(response);
						node.removeChild(node.lastChild);
						makeDL(response);
					}
				});
			},
			error: function(error){
				console.log(error);
			}
		});
	});	
});

function makeDL(string){
	var node = document.getElementById('dlID');
	while (node.hasChildNodes()) {
		node.removeChild(node.lastChild);
	}
	
	strings = string.split("\n");
	diseases = [];
	
	for( var i = 0; i < strings.length; i++ ) {
		if(strings[i].split(",",2)[0]) {
			diseases.push(strings[i].split(",",2));
		}
	}
	
	if( diseases[0][1] ) {
		max = parseInt(diseases[0][1]);
	}
	else max = 1;
	
	for( var i = 0; i<diseases.length; i++ ) {
		num = Math.round(parseInt(diseases[i][1])*100.0/max);
		if ( num < 1 ) { num = 1; }
		diseases[i].push(num);
	}
	
	var list = document.createElement('DL');
	list.setAttribute("class", "centerAlign");
	var item = document.createElement('DT');
	item.setAttribute("class", "centerAlign");
	var text = document.createTextNode("Most reported contagious diseases near your destination right now");
	item.appendChild(text);
	list.appendChild(item);
	for( var i = 0; i < diseases.length; i++) {
		item = document.createElement('DD');
		item.setAttribute("class", "centerAlign percentage percentage-"+diseases[i][2]);
		span = document.createElement('SPAN');
		span.setAttribute("class", "text");
		span.appendChild(document.createTextNode(diseases[i][0] + ": " + diseases[i][1]));
		item.appendChild(span);
		list.appendChild(item);
	}
	document.getElementById('dlID').appendChild(list);
}