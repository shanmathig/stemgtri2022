currentToggle = true;
var trace1 = {
  x: [],
  y: [],
  name: 'Gain',
  type: 'scatter'
};
var trace2 = {
  x: [],
  y: [],
  name: 'Cutsize',
  type: 'scatter'
};
var data = [trace1, trace2];

var layout = {
  title: {
    text:'Gain and Cutsize',
    font: {
      family: 'Courier New, monospace',
      size: 24
    },
    xref: 'paper',
    x: 0.05,
  },
  xaxis: {
    title: {
      text: 'Iteration',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }
    },
  },
  yaxis: {
    title: {
      text: 'Size',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }
    }
  }
};

Plotly.newPlot('chartContainer', data, layout);

function graphToggle(){
	if(currentToggle){
		document.getElementById("chartContainer").style.display = "none";
		document.getElementById("ghost-button").style.marginTop = "67vh";
		currentToggle = false
	}else{
		document.getElementById("chartContainer").style.display = "block";
		document.getElementById("ghost-button").style.marginTop = "25vh";
		currentToggle = true
	}
}