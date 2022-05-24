let  xValues = [10,20,30,40,50,60,70];
let  yValues = [0,0,0,0,0,0,0];


let secondxValues = [10,20,30,40,50,60,70]
let secondyValues = [0,0,0,0,0,0,0];

let refetchFiles = (who)=>{
  fetch(who)
  .then(response => response.text())
  .then((text) => {
    console.log(text)
      let str_arr = text.split('\n')
      if(str_arr.length > 10)
        str_arr = str_arr.slice(-9)

      console.log(str_arr.length)

      let numbers = str_arr.map((el)=>{
      return Number(el)
      })
      console.log(numbers);
      let increment = 5;
      let index = -1;
      let x_axis = numbers.map((el)=>{
        index +=1;
        return index*increment;
      })
            if(who == 'Temperatura.txt')
            {
              yValues = numbers
              xValues = x_axis
            }
            else
            {
              secondyValues = numbers
              secondxValues = x_axis
            }
  })

}

setInterval(()=>{
refetchFiles('Temperatura.txt');
refetchFiles('Umiditate.txt');

new Chart("myChart", {
 type: "line",
 data: {
   labels: xValues,
   datasets: [{
     fill: false,
     lineTension: 0,
     backgroundColor: "rgba(255,255,255,1.0)",
         borderColor: "rgba(255,255,255,0.1)",
     data: yValues
   }]
 },
 options: {
   legend: {display: false},
   scales: {
     yAxes: [{ticks: {min: 0, max:60}}],
   },
animation: {
duration: 0
   }
 }
});

new Chart("myChart2", {
     type: "line",
     data: {
       labels: secondxValues,
       datasets: [{
         fill: false,
         lineTension: 0,
         backgroundColor: "rgba(255,255,255,1.0)",
         borderColor: "rgba(255,255,255,0.1)",
         data: secondyValues
       }]
     },
     options: {
       legend: {display: false},
       scales: {
         yAxes: [{ticks: {min: 0, max:60}}],
       },
    animation: {
    duration: 0
       }
     }
    });

},2000)